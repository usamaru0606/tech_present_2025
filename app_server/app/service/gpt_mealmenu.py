import openai
import os
import sqlite3
import datetime
from dotenv import load_dotenv

# .env から環境変数を読み込む
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_user_info(user_id: str):
    """
    指定されたユーザーIDの健康情報をDBから取得する関数
    :param user_id: ユーザーID
    :return: 辞書形式のユーザー情報 or None
    """
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT gender, age, height, weight, goal_weight, problem
        FROM user_health_data
        WHERE id = ?
    """, (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "gender": row[0],
            "age": row[1],
            "height": row[2],
            "weight": row[3],
            "goal_weight": row[4],
            "problem": row[5]
        }
    else:
        return None

def generate_meal_menu_text(user_data: dict) -> str:
    """
    GPTでユーザーに合った1週間分の食事メニューを生成する関数
    :param user_data: ユーザー情報（辞書）
    :return: GPTが生成したメニュー文字列
    """
    age = user_data['age']
    age_note = "\n※年齢が12歳以下の場合も、13~19歳と同じ基準で食事を考えてください。" if age <= 12 else ""
    prompt = f"""
    性別: {user_data['gender']}、年齢: {user_data['age']}歳、\n身長: {user_data['height']}cm、体重: {user_data['weight']}kg、目標体重: {user_data['goal_weight']}kg、\n悩み: {user_data['problem']}。\nこの人に合った本日から一週間分の食事メニュー（朝食・昼食・夕食）を提案してください。\n各日付ごとに「朝食」「昼食」「夕食」それぞれに「主食」「主菜」「副菜」「汁物」「その他」と「カロリー（数値, kcal）」を含めてください。\n以下のJSON形式で出力してください。\n[\n  {{"date": "YYYY-MM-DD", "朝食": {{"主食": "ごはん", "主菜": "焼き魚", "副菜": "サラダ", "汁物": "味噌汁", "その他": "果物", "カロリー": 450}}, "昼食": {{...}}, "夕食": {{...}}}},\n  ...（7日分）\n]\n各食の例: {{"主食": "ごはん", "主菜": "焼き魚", "副菜": "サラダ", "汁物": "味噌汁", "その他": "果物", "カロリー": 450}}{age_note}\n"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは栄養士です。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

def parse_meal_menu(menu_text: str):
    """
    GPTの出力を分解して辞書形式に整形する関数
    :param menu_text: GPTの出力文字列
    :return: [{'timing': ..., 'staple_food': ..., ...}, ...]
    """
    meals = []
    current_meal = {}
    lines = menu_text.strip().split("\n")

    for line in lines:
        line = line.strip()
        if line.endswith("食："):
            if current_meal:
                meals.append(current_meal)
            current_meal = {"timing": line.replace("：", "")}
        elif "主食：" in line:
            current_meal["staple_food"] = line.replace("主食：", "").strip()
        elif "主菜：" in line:
            current_meal["main_dish"] = line.replace("主菜：", "").strip()
        elif "副菜：" in line:
            current_meal["side_dish"] = line.replace("副菜：", "").strip()
        elif "汁物：" in line:
            current_meal["soup"] = line.replace("汁物：", "").strip()
        elif "その他：" in line:
            current_meal["others"] = line.replace("その他：", "").strip()

    if current_meal:
        meals.append(current_meal)

    return meals

def save_meal_menu_to_db(user_id: str, parsed_menu: list):
    """
    整形されたメニューを meal_menu テーブルに登録する関数
    :param user_id: ユーザーID
    :param parsed_menu: GPT出力を整形したリスト
    """
    today = datetime.date.today().isoformat()
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()

    for meal in parsed_menu:
        cursor.execute("""
            INSERT INTO meal_menu (
                user_id, date, timing,
                staple_food, main_dish, side_dish, soup, others
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, today, meal.get("timing", ""),
            meal.get("staple_food", ""), meal.get("main_dish", ""),
            meal.get("side_dish", ""), meal.get("soup", ""), meal.get("others", "")
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    user_id = "u001"  # ← 対象ユーザーIDを指定

    # DBからユーザー情報を取得
    user_info = get_user_info(user_id)

    if not user_info:
        print(f"ユーザーID '{user_id}' は見つかりませんでした。")
    else:
        # GPTで食事メニューを生成
        meal_text = generate_meal_menu_text(user_info)

        # 整形して登録
        parsed = parse_meal_menu(meal_text)
        save_meal_menu_to_db(user_id, parsed)

        print(f"ユーザー '{user_id}' の食事メニューをDBに登録しました。")