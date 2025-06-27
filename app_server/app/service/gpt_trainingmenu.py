import openai
import os
import sqlite3
import datetime
from dotenv import load_dotenv

# .env ファイルから API キーを読み込む
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_user_info(user_id: str):
    """
    指定されたユーザーIDの健康情報をDBから取得する関数

    :param user_id: ユーザーの一意なID
    :return: 辞書形式のユーザーデータ（存在しない場合は None）
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

def generate_training_menu_text(user_data: dict) -> str:
    """
    GPTでユーザーに合ったトレーニングメニューを生成する関数

    :param user_data: 辞書形式のユーザー情報（身長、体重など）
    :return: GPT出力のトレーニングメニュー（文字列）
    """
    prompt = f"""
    性別: {user_data['gender']}、年齢: {user_data['age']}歳、
    身長: {user_data['height']}cm、体重: {user_data['weight']}kg、目標体重: {user_data['goal_weight']}kg、悩み: {user_data['problem']}。
    この人に合った1日のトレーニングメニューを提案してください。
    種目と回数（または時間）をわかりやすくリスト形式で出力してください。
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたはプロのフィットネストレーナーです。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]

def parse_training_menu(menu_text: str):
    """
    GPT出力を整形する関数

    :param menu_text: GPTからの出力
    :return: [{"exercise": ..., "quantity": ...}, ...]
    """
    lines = menu_text.strip().split("\n")
    parsed = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "：" in line:
            parts = line.split("：", 1)
        elif ":" in line:
            parts = line.split(":", 1)
        else:
            continue
        exercise = parts[0].strip("1234567890. ").strip()
        quantity = parts[1].strip()
        parsed.append({"exercise": exercise, "quantity": quantity})
    return parsed

def save_training_menu_to_db(user_id: str, parsed_menu: list):
    """
    トレーニングメニューをDBに登録する関数

    :param user_id: 対象ユーザーのID
    :param parsed_menu: 整形済みのメニューリスト
    """
    today = datetime.date.today().isoformat()
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()

    for item in parsed_menu:
        cursor.execute("""
            INSERT INTO training_menu (user_id, date, exercise, quantity)
            VALUES (?, ?, ?, ?)
        """, (user_id, today, item["exercise"], item["quantity"]))

    conn.commit()
    conn.close()

# ========== 実行部 ==========

user_id = "u001"  # ←対象のユーザーIDを指定

# ユーザー情報を取得
user_info = get_user_info(user_id)
if not user_info:
    print(f"ユーザーID {user_id} は見つかりませんでした。")
else:
    # GPTでメニュー生成
    gpt_menu_text = generate_training_menu_text(user_info)

    # 整形してDBに登録
    menu_list = parse_training_menu(gpt_menu_text)
    save_training_menu_to_db(user_id, menu_list)

    print(f"ユーザー '{user_id}' のトレーニングメニューを登録しました。")