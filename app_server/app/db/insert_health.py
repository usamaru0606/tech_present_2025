import sqlite3
import pandas as pd
import numpy as np
import random

# 各年齢層・性別ごとの平均身長・体重およびその標準偏差
age_groups = {
    "20-29歳": {"male": (171.2, 6.3, 66.1, 12.1), "female": (157.6, 5.2, 51.7, 7.6)},
    "30-39歳": {"male": (171.5, 5.5, 70, 13.0), "female": (158.2, 5.5, 54.3, 9.5)},
    "40-49歳": {"male": (171.5, 5.8, 72.8, 12.8), "female": (158.1, 5.4, 55.6, 10.0)},
    "50-59歳": {"male": (169.9, 6.0, 71.0, 11.4), "female": (156.9, 5.2, 55.2, 9.1)},
    "60-69歳": {"male": (167.4, 6.0, 67.3, 10.9), "female": (154.0, 5.7, 54.7, 9.2)},
    "70歳以上": {"male": (163.1, 6.1, 62.4, 9.9), "female": (149.4, 6.0, 51.1, 8.6)},
}

# 運動時間カテゴリと、それぞれの年齢層・性別における確率分布
exercise_time_categories = ["30分未満", "30～60分", "60～120分", "120～180分", "180分以上"]

exercise_times = {
    "male": {
        "20-29歳": [0.00, 0.225, 0.325, 0.375, 0.075],
        "30-39歳": [0.043, 0.383, 0.404, 0.106, 0.064],
        "40-49歳": [0.029, 0.265, 0.412, 0.176, 0.118],
        "50-59歳": [0.148, 0.311, 0.377, 0.115, 0.049],
        "60-69歳": [0.073, 0.331, 0.384, 0.113, 0.099],
        "70歳以上": [0.145, 0.261, 0.35, 0.127, 0.117]
    },
    "female": {
        "20-29歳": [0.095, 0.429, 0.238, 0.238, 0.000],
        "30-39歳": [0.111, 0.267, 0.444, 0.178, 0.000],
        "40-49歳": [0.103, 0.241, 0.483, 0.115, 0.057],
        "50-59歳": [0.152, 0.33, 0.339, 0.107, 0.071],
        "60-69歳": [0.194, 0.351, 0.319, 0.11, 0.026],
        "70歳以上": [0.149, 0.331, 0.346, 0.125, 0.048]
    }
}

# 運動日数カテゴリと、その確率分布
exercise_day_categories = ["運動なし", "1日/週", "2日/週", "3日/週", "4日/週", "5日/週", "6日/週", "7日/週"]

exercise_days = {
    "20-29歳": {
        "male":  [0.403, 0.194, 0.164, 0.090, 0.045, 0.060, 0.000, 0.045],
        "female": [0.661, 0.129, 0.113, 0.065, 0.000, 0.032, 0.000, 0.000]
    },
    "30-39歳": {
        "male":  [0.447, 0.235, 0.082, 0.082, 0.035, 0.047, 0.012, 0.059],
        "female": [0.676, 0.122, 0.072, 0.050, 0.029, 0.022, 0.007, 0.022]
    },
    "40-49歳": {
        "male":  [0.567, 0.134, 0.096, 0.064, 0.006, 0.051, 0.019, 0.064],
        "female": [0.627, 0.133, 0.060, 0.030, 0.034, 0.039, 0.009, 0.069]
    },
    "50-59歳": {
        "male":  [0.585, 0.082, 0.095, 0.054, 0.034, 0.041, 0.007, 0.102],
        "female": [0.545, 0.106, 0.081, 0.073, 0.033, 0.049, 0.033, 0.081]
    },
    "60-69歳": {
        "male":  [0.474, 0.070, 0.084, 0.101, 0.042, 0.059, 0.031, 0.139],
        "female": [0.480, 0.104, 0.076, 0.087, 0.044, 0.035, 0.016, 0.158]
    },
    "70歳以上": {
        "male":  [0.404, 0.057, 0.074, 0.074, 0.057, 0.044, 0.027, 0.263],
        "female": [0.390, 0.120, 0.102, 0.098, 0.046, 0.046, 0.036, 0.162]
    },
}

# サンプル数
num_samples = 500
data = []

# 各年齢層・性別に対して合成データを生成
for age_group, genders in age_groups.items():
    for gender, (h_mean, h_std, w_mean, w_std) in genders.items():
        heights = np.random.normal(h_mean, h_std, num_samples).round(1)
        weights = np.random.normal(w_mean, w_std, num_samples).round(1)
        bmi_values = (weights / (heights / 100) ** 2).round(1)

        # 運動日数と運動時間カテゴリを確率に基づいてランダムに選択
        days = random.choices(
            exercise_day_categories,
            weights=exercise_days[age_group][gender],
            k=num_samples
        )
        durations = random.choices(
            exercise_time_categories,
            weights=exercise_times[gender][age_group],
            k=num_samples
        )

        # 外れ値フィルター（体重 35～150kg, BMI 14～45）
        for h, w, bmi, d, dur in zip(heights, weights, bmi_values, days, durations):
            if 35 <= w <= 150 and 14 <= bmi <= 45:
                data.append((age_group, gender, float(h), float(w), float(bmi), d, dur))

# DataFrame作成
df = pd.DataFrame(data, columns=[
    "age_group", "gender", "height", "weight", "bmi", "exercise_days", "exercise_duration"
])

# SQLite保存
db_path = "D:/my-weight-app/app/data/processed/health_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義
cursor.execute("DROP TABLE IF EXISTS user_data")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age_group TEXT,
    gender TEXT,
    height REAL,
    weight REAL,
    bmi REAL,
    exercise_days TEXT,
    exercise_duration TEXT
)
""")

# データ挿入
df.to_sql("user_data", conn, if_exists="append", index=False)

# 登録件数確認
total = cursor.execute("SELECT COUNT(*) FROM user_data").fetchone()[0]
print("登録完了: 件数 =", total)

conn.commit()
conn.close()