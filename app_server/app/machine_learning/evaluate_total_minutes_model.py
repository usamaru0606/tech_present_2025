import sqlite3
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score

# ==========================
# 1. 保存済みモデルの読み込み
# ==========================

# 線形回帰モデルを読み込む（学習時に保存したもの）
model = joblib.load("model_total_minutes_per_week.pkl")

# gender（性別）カラムのOne-Hotエンコーダも読み込む
encoder = joblib.load("gender_encoder.pkl")

# ==========================
# 2. データベースからデータ取得
# ==========================

# SQLiteデータベースに接続（パスは必要に応じて変更）
conn = sqlite3.connect("../db/health_data.db")

# 必要なカラムを選んでSQLでデータを取得（欠損を除外）
query = """
SELECT height, weight, gender, target_weight, days_per_week, minutes_per_day
FROM sample_user_data
WHERE target_weight IS NOT NULL
"""
df = pd.read_sql_query(query, conn)

# DB接続は不要なので閉じておく（メモリ節約のため）
conn.close()

# ==========================
# 3. 特徴量と目的変数の準備
# ==========================

# total_minutes_per_week = days_per_week × minutes_per_day
# → 週あたりの総運動時間（分）を目的変数とする
df["total_minutes_per_week"] = df["days_per_week"] * df["minutes_per_day"]

# gender列（カテゴリ変数）をエンコード（学習時と同じ方法）
encoded_gender = encoder.transform(df[["gender"]])

# 数値系の特徴量（身長、体重、目標体重）
numerical_features = df[["height", "weight", "target_weight"]].values

# 最終的な説明変数（X） = 数値 + One-Hotエンコーディング
X = np.hstack([numerical_features, encoded_gender])

# 目的変数（y）= 週の総運動時間（分）
y = df["total_minutes_per_week"].values

# ==========================
# 4. モデルによる予測と評価
# ==========================

# モデルを使って運動時間を予測
pred = model.predict(X)

# 評価指標1：平均二乗誤差（小さいほどよい）
mse = mean_squared_error(y, pred)

# 評価指標2：決定係数R²（1に近いほどよい）
r2 = r2_score(y, pred)

# ==========================
# 5. 結果出力
# ==========================

print("【モデル評価：週あたりの総運動時間（分）予測】")
print(f"平均二乗誤差 (MSE): {mse:.2f}")
print(f"決定係数 (R²スコア): {r2:.3f}")