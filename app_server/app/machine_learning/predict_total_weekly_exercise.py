import sqlite3
import numpy as np
import pandas as pd
import joblib

# ---------- 事前準備 ----------
# 予測対象のユーザーID（FastApiでidを指定）
target_user_id = "u001"

# 学習済みモデルとエンコーダの読み込み
model = joblib.load("model_total_minutes_per_week.pkl")
encoder = joblib.load("gender_encoder.pkl")

# ---------- DBから対象ユーザーのデータを取得 ----------
conn = sqlite3.connect("health_data.db")
cursor = conn.cursor()

query = """
SELECT id, height, weight, goal_weight, gender, age_group
FROM user_health_data
WHERE id = ?
"""
df = pd.read_sql_query(query, conn, params=(target_user_id,))

# ユーザーが存在しない場合の処理
if df.empty:
    print(f"ユーザーID '{target_user_id}' のデータが見つかりません。")
    conn.close()
    exit()

# ---------- 特徴量の前処理 ----------
# gender, age_group を One-Hot エンコード
encoded_cats = encoder.transform(df[["gender", "age_group"]])

# 数値データ（身長・体重・目標体重）を取得
numerical_features = df[["height", "weight", "goal_weight"]].values

# モデルの入力にするため、特徴量を結合
X = np.hstack([numerical_features, encoded_cats])

# ---------- 予測 ----------
predicted_minutes = model.predict(X)[0]  # 結果は1件だけ

# ---------- カラム追加（初回だけ必要） ----------
try:
    cursor.execute("ALTER TABLE user_health_data ADD COLUMN predicted_total_minutes_per_week REAL")
except sqlite3.OperationalError:
    pass  # カラムが既にある場合は無視

# ---------- DBを更新（対象ユーザーのみ） ----------
cursor.execute("""
    UPDATE user_health_data
    SET predicted_total_minutes_per_week = ?
    WHERE id = ?
""", (predicted_minutes, target_user_id))

conn.commit()
conn.close()

# ---------- 完了メッセージ ----------
print(f"ユーザー '{target_user_id}' の運動量予測値 {predicted_minutes:.2f} 分/週 をDBに登録しました。")