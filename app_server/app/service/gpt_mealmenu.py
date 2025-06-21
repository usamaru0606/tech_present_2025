import openai
import os
import sqlite3
import datetime

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_meal_menu_text(height: float, weight: float, goal_weight: float, problem: str) -> str:
    """
    ユーザーの情報をもとにGPTで食事メニューを生成する関数。
    :param height: 身長（cm）
    :param weight: 現在の体重（kg）
    :param goal_weight: 目標体重（kg）
    :param problem: ユーザーの悩み（例：夜食をやめられない）
    :return: GPTの生成した食事メニュー（文字列）
    """
    prompt = f"""
    身長: {height}cm、体重: {weight}kg、目標体重: {goal_weight}kg、悩み: {problem}。
    この人に合った1日の食事メニュー（朝・昼・夜）を提案してください。
    各食に「主食」「主菜」「副菜」「汁物」「その他」が含まれるようにしてください。
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたは栄養士です。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]

def parse_menu(menu_text: str):
    """
    GPTの出力テキストから、朝昼夜の食事メニューを辞書リストに整形する関数。
    :param menu_text: GPTが出力した生の文字列
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



def save_meal_menu_to_db(user_id: str, menu_text: str):
    """
    GPTの出力をもとに食事メニューをDBに登録する関数。
    :param user_id: 対象のユーザーID
    :param menu_text: GPTの出力テキスト
    """
    meals = parse_menu(menu_text)  # 整形して辞書に

    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()

    for meal in meals:
        cursor.execute("""
            INSERT INTO meal_menu (
                user_id, date, timing,
                staple_food, main_dish, side_dish, soup, others
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, today, meal["timing"],
            meal.get("staple_food", ""), meal.get("main_dish", ""),
            meal.get("side_dish", ""), meal.get("soup", ""), meal.get("others", "")
        ))

    conn.commit()
    conn.close()

# ユーザーから送られてきたデータ
# ここにフロントから入力されたデータorデータベースから取得
user_id = "u001"
height = 170
weight = 75
goal_weight = 65
problem = "夜食をやめられない"

# 1. GPTでメニュー生成
menu_text = generate_meal_menu_text(height, weight, goal_weight, problem)

# 2. メニューをDBへ登録
save_meal_menu_to_db(user_id, menu_text)