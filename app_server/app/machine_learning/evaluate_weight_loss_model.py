import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score

# ==========================
# 1. 学習済みモデルとエンコーダの読み込み
# ==========================

# 学習済みの線形回帰モデルを読み込む
model = joblib.load("linear_regression_model.pkl")

# 学習時に使ったOneHotEncoder（カテゴリ変数のエンコード用）も読み込む
encoder = joblib.load("onehot_encoder.pkl")

# ==========================
# 2. 評価用のデータを読み込み・前処理
# ==========================

# トレーニング時と同じCSVデータを読み込む
df = pd.read_csv("../db/weight_loss_data.csv")

# 入力に使う特徴量の列と、目的変数（減量量）を指定
features = ["age_group", "gender", "days_per_week", "minutes_per_day"]
target = "weight_loss"

# カテゴリ変数を抽出してOne-Hotエンコード（学習時と同じエンコーダを使用）
categorical_features = df[["age_group", "gender"]]
encoded_cats = encoder.transform(categorical_features)

# 数値系特徴量を抽出
numerical_features = df[["days_per_week", "minutes_per_day"]].values

# 最終的な入力データ（X）をカテゴリと数値で結合
X = np.hstack([encoded_cats, numerical_features])

# 目的変数（y）をNumPy配列で抽出
y = df[target].values

# ==========================
# 3. モデルによる予測と評価
# ==========================

# 保存済みモデルを使って予測を実施
y_pred = model.predict(X)

# 平均二乗誤差（MSE）を計算：小さいほど誤差が少ない
mse = mean_squared_error(y, y_pred)

# 決定係数（R²）を計算：1に近いほど予測精度が高い
r2 = r2_score(y, y_pred)

# ==========================
# 4. 評価結果を出力
# ==========================

print("【モデル評価：減量量（kg）予測】")
print(f"平均二乗誤差 (MSE): {mse:.2f}")
print(f"決定係数 (R²スコア): {r2:.3f}")