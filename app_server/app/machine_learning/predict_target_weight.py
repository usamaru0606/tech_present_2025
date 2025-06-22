import sqlite3
import pandas as pd
import numpy as np
import joblib

# 保存済みの学習済みモデルとOneHotEncoderをロード
model = joblib.load("linear_regression_model.pkl")
encoder = joblib.load("onehot_encoder.pkl")

# SQLiteのDBファイルとテーブル名を指定
db_path = "../db/health_data.db"
table_name = "user_data"

# DB接続を確立
conn = sqlite3.connect(db_path)

# user_dataテーブルから必要なカラムを読み込み
# 予測に使う特徴量のみ選択（カテゴリはエンコーダーで処理するため含める）
query = f"""
SELECT id, age_group, gender, days_per_week, minutes_per_day, weight
FROM {table_name}
"""
df = pd.read_sql_query(query, conn)

# 学習時のカテゴリに変換
age_group_map = {
    "20-29歳": "20-29",
    "30-39歳": "30-39",
    "40-49歳": "40-49",
    "50-59歳": "50-59",
    "60-69歳": "60-69",
    "70歳以上": "70"
}
df["age_group"] = df["age_group"].map(age_group_map)

# 予測に使うカテゴリ変数（age_group, gender）をOne-Hotエンコーディング
categorical_features = df[["age_group", "gender"]]
encoded_cats = encoder.transform(categorical_features)

# 数値特徴量（運動頻度と運動時間）を抽出
numerical_features = df[["days_per_week", "minutes_per_day"]].values

# エンコードしたカテゴリ特徴量と数値特徴量を結合してモデル入力用の行列を作成
X = np.hstack([encoded_cats, numerical_features])

# 予測を実行（weight_loss = 減量量を予測）
predicted_weight_loss = model.predict(X)

# 現在の体重から予測減量量を引いて目標体重を計算
target_weight = df["weight"].values - predicted_weight_loss

# 新しいカラムとして予測値をDataFrameに追加
df["predicted_weight_loss"] = predicted_weight_loss
df["target_weight"] = target_weight

# DBに新しいカラムを追加（もしまだ存在しなければ）
cursor = conn.cursor()
try:
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN predicted_weight_loss REAL")
except sqlite3.OperationalError:
    # カラムがすでに存在する場合は何もしない
    pass
try:
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN target_weight REAL")
except sqlite3.OperationalError:
    pass

# 予測結果をDBに更新するためのループ
for _, row in df.iterrows():
    cursor.execute(
        f"""
        UPDATE {table_name}
        SET predicted_weight_loss = ?, target_weight = ?
        WHERE id = ?
        """,
        (row["predicted_weight_loss"], row["target_weight"], row["id"])
    )

# 変更をコミットしてDB接続を閉じる
conn.commit()
conn.close()

print("目標体重の予測値をDBに更新しました。")