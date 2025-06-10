import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# DBに接続
conn = sqlite3.connect("../db/health_data.db")

# データ取得：必要なカラムだけ、かつ欠損を除外
query = """
SELECT height, weight, gender, target_weight, days_per_week, minutes_per_day
FROM user_data
WHERE target_weight IS NOT NULL
"""
df = pd.read_sql_query(query, conn)

# 目的変数：週の総運動時間（分） = days_per_week × minutes_per_day
df["total_minutes_per_week"] = df["days_per_week"] * df["minutes_per_day"]

# カテゴリ変数 'gender' を One-Hot エンコーディング
encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
encoded_gender = encoder.fit_transform(df[["gender"]])

# 数値の説明変数（身長・体重・目標体重）
numerical_features = df[["height", "weight", "target_weight"]].values

# 説明変数 = 数値 + One-Hot エンコード
X = np.hstack([numerical_features, encoded_gender])

# 目的変数（週の運動総時間）
y = df["total_minutes_per_week"].values

# データをトレーニング用とテスト用に分割（80:20）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 線形回帰モデルの学習
model = LinearRegression()
model.fit(X_train, y_train)

# テストデータで予測
pred = model.predict(X_test)

# 精度評価：MSE（誤差）と R²（説明力）
mse = mean_squared_error(y_test, pred)
r2 = r2_score(y_test, pred)

# 精度を出力
print("【予測：週あたりの必要運動総時間（分）】")
print(f"平均二乗誤差 (MSE): {mse:.2f}")
print(f"決定係数 (R²スコア): {r2:.3f}\n")

# モデルとエンコーダの保存
joblib.dump(model, "model_total_minutes_per_week.pkl")
joblib.dump(encoder, "gender_encoder.pkl")

print(" モデルとエンコーダを保存しました。")