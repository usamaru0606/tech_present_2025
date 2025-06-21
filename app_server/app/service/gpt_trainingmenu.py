import openai
import os
import sqlite3
import datetime

# 環境変数からOpenAI APIキーを取得（.envファイルなどで設定しておく）
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_training_menu_text(height: float, weight: float, goal_weight: float, problem: str) -> str:
    """
    GPTを使ってユーザーに合ったトレーニングメニューを生成する関数。

    :param height: ユーザーの身長（cm）
    :param weight: ユーザーの現在の体重（kg）
    :param goal_weight: ユーザーの目標体重（kg）
    :param problem: ユーザーの悩み（例：運動が続かない など）
    :return: GPTが生成したトレーニングメニュー（文字列）
    """
    # ユーザー情報をもとにGPTに送るプロンプトを作成
    prompt = f"""
    身長: {height}cm、体重: {weight}kg、目標体重: {goal_weight}kg、悩み: {problem}。
    この人に合った1日のトレーニングメニューを提案してください。
    種目と回数（または時間）を分かりやすくリスト形式で出力してください。
    """

    # GPTへ問い合わせて、トレーニングメニューを生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用モデル。コストを抑えたい場合は3.5推奨
        messages=[
            {"role": "system", "content": "あなたはプロのフィットネストレーナーです。"},
            {"role": "user", "content": prompt}
        ]
    )

    # GPTから返されたテキストを取得
    return response.choices[0].message["content"]

def parse_training_menu(menu_text: str):
    """
    GPTが生成したメニューの文章を分解し、データベース登録しやすい形式に整形する関数。

    :param menu_text: GPTから出力された生のメニュー文字列
    :return: [{'exercise': 'スクワット', 'quantity': '15回 × 3セット'}, ...] の形式のリスト
    """
    lines = menu_text.strip().split("\n")  # 行ごとに分割
    parsed = []

    for line in lines:
        line = line.strip()
        if not line:
            continue  # 空行はスキップ

        # 「番号. 種目：量」 または「種目:量」の形式を想定して分割
        if "：" in line:
            parts = line.split("：", 1)
        elif ":" in line:
            parts = line.split(":", 1)
        else:
            continue  # 区切りがない場合はスキップ

        # 種目名から数字やドットを除去してクリーンに
        exercise = parts[0].strip("1234567890. ").strip()
        quantity = parts[1].strip()
        parsed.append({"exercise": exercise, "quantity": quantity})

    return parsed

def save_training_menu_to_db(user_id: str, menu_text: str):
    """
    整形したトレーニングメニューをデータベースの training_menu テーブルに登録する関数。

    :param user_id: 対象ユーザーのID（文字列）
    :param menu_text: GPTが生成したメニュー（まだ整形されていないテキスト）
    """
    parsed_menu = parse_training_menu(menu_text)  # 整形関数でリスト化
    today = datetime.date.today().isoformat()  # 今日の日付を取得（例：2025-06-21）

    # SQLiteデータベースに接続
    conn = sqlite3.connect("health_data.db")
    cursor = conn.cursor()

    # 各種目をDBに1件ずつINSERT
    for item in parsed_menu:
        cursor.execute("""
            INSERT INTO training_menu (user_id, date, exercise, quantity)
            VALUES (?, ?, ?, ?)
        """, (user_id, today, item["exercise"], item["quantity"]))

    conn.commit()  # 変更を保存
    conn.close()   # 接続を閉じる

# ↓↓↓ 実行部分 ↓↓↓

# 仮のユーザー入力（本来はDBから取得 or フロントエンドから渡される）
user_id = "u001"
height = 170
weight = 75
goal_weight = 65
problem = "運動が長続きしません"

# 1. GPTに問い合わせてトレーニングメニューを生成
menu_text = generate_training_menu_text(height, weight, goal_weight, problem)

# 2. 出力されたメニューを整形し、データベースに登録
save_training_menu_to_db(user_id, menu_text)