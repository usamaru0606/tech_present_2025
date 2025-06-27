#機械学習用の教師ありデータ作成


import numpy as np
import pandas as pd
import random

# パーソナル情報定義
age_groups = ["20-29", "30-39", "40-49", "50-59", "60-69", "70"]
genders = ["male", "female"]
exercise_days = ["運動なし", "1日/週", "2日/週", "3日/週", "4日/週", "5日/週", "6日/週", "7日/週"]
exercise_times = ["30分未満", "30〜60分", "60〜120分", "120〜180分", "180分以上"]

# 運動日数と運動時間カテゴリを数値に変換
# 運動日数
day_to_count = {
    "運動なし": 0, "1日/週": 1, "2日/週": 2, "3日/週": 3,
    "4日/週": 4, "5日/週": 5, "6日/週": 6, "7日/週": 7
}
# 運動時間
time_to_minutes = {
    "30分未満": 15, "30〜60分": 45, "60〜120分": 90,
    "120〜180分": 150, "180分以上": 210
}

# サンプル数
n_samples = 3000
data = []

for _ in range(n_samples):
    # パーソナル情報をランダム生成
    gender = random.choice(genders)
    age_group = random.choice(age_groups)
    # 平均身長：男性:172cm 女性:165cm 標準偏差は共通で5cm
    height = np.random.normal(165 if gender == "female" else 172, 5)
    # 平均体重：
    weight = np.random.normal(60 if gender == "female" else 70, 10)
    
    # 運動日数をランダム生成
    day = random.choice(exercise_days)
    # 数値化
    days_per_week = day_to_count[day]

    # 運動日数が0の場合、運動時間も0分とする、それ以外はランダム生成
    if days_per_week == 0:
        time = "0分"
        minutes_per_day = 0
    else:
        time = random.choice(exercise_times)
        minutes_per_day = time_to_minutes[time]

    # 運動日数×運動時間で総合運動時間を算出
    total_minutes_per_week = days_per_week * minutes_per_day

    # BMIを算出
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # 性別係数：女性の方が0.3kg多く減量しやすい（仮定）
    gender_bias = 0.3 if gender == "female" else 0.0

    # 減量量の仮想的な計算式（重回帰的な構造）
    # - 低頻度より高頻度の方が多く減量する
    # - 高齢ほど減りづらい
    # - 女性は少し多めに減る
    noise = np.random.normal(0, 0.5)
    weight_loss = (
        0.02 * total_minutes_per_week  # 運動時間に比例
        + 0.4 * (days_per_week <= 3)  # 低頻度に補正（仮想）
        - 0.01 * int(age_group.split("-")[0])  # 年齢による減衰
        + gender_bias
        + noise
    )

    # 減量後体重と目標体重
    target_weight = max(45.0, weight - weight_loss)
    weight_loss = weight - target_weight

    data.append({
        "age_group": age_group,
        "gender": gender,
        "height": round(height, 1),
        "weight": round(weight, 1),
        "bmi": round(bmi, 1),
        "exercise_days": day,
        "exercise_time": time,
        "days_per_week": days_per_week,
        "minutes_per_day": minutes_per_day,
        "total_minutes_per_week": total_minutes_per_week,
        "target_weight": round(target_weight, 1),
        "weight_loss": round(weight_loss, 1)
    })

# DataFrameに変換
df = pd.DataFrame(data)

# CSV保存（必要なら）
df.to_csv("weight_loss_data.csv", index=False)

# 確認用表示
print(df.head(10))