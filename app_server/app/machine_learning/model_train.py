import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# CSVデータの読み込み
df = pd.read_csv("../db/weight_loss_data.csv")

# 特徴量として使う列を選択（ここではカテゴリ変数を含む）
features = ["age_group", "gender", "days_per_week", "minutes_per_day"]
target = "weight_loss"  # 予測したい目的変数（減量量）

# カテゴリ変数をOne-Hotエンコーディング（機械学習で使いやすい数値に変換）
# age_groupとgenderを変換するためにOneHotEncoderを使用
encoder = OneHotEncoder(sparse=False)
categorical_features = df[["age_group", "gender"]]
encoded_cats = encoder.fit_transform(categorical_features)

# 数値特徴量の抽出
numerical_features = df[["days_per_week", "minutes_per_day"]].values

# エンコード済みカテゴリ特徴量と数値特徴量を結合
import numpy as np
X = np.hstack([encoded_cats, numerical_features])

# 目的変数
y = df[target].values

# データを訓練用とテスト用に分割（訓練80%、テスト20%）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 線形回帰モデルをインスタンス化
model = LinearRegression()

# 訓練データでモデルを学習
model.fit(X_train, y_train)

# テストデータで予測
y_pred = model.predict(X_test)

# モデル性能を評価（平均二乗誤差と決定係数）
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# モデル評価結果を出力
# 平均二乗誤差は小さい程誤差がない。
# 決定係数は1に近いほどモデルの数値として良い
print(f"Mean Squared Error: {mse:.3f}")
print(f"R2 Score: {r2:.3f}")

# モデル保存（例：joblib）
import joblib
joblib.dump(model, "linear_regression_model.pkl")

# OneHotEncoderも一緒に保存しておくと本番推論で便利
joblib.dump(encoder, "onehot_encoder.pkl")