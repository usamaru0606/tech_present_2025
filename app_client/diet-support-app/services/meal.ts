import type { DayMeal, Meal, MealKey } from "~/model/meal";
import type { RecordMeal } from "~/model/recoradmeal";

export const GetToDayMenuService = async (id: string) => {
  try {
    return await $fetch<Record<MealKey, Meal> | null>(
      `http://127.0.0.1:8000/api/todaymenu/${id}`
    );
  } catch {
    return null;
  }
};

export const RecordMealService = async (recordMeal: RecordMeal) => {
  try {
    // バックエンドのMealRecordRequestスキーマに合わせて変換
    const payload = {
      id: recordMeal.userId,
      recordDate: recordMeal.recordDate,
      mealTiming: recordMeal.mealTiming,
      content: {
        主食: recordMeal.stapleFood ?? "",
        主菜: recordMeal.mainDish ?? "",
        副菜: recordMeal.sideDish ?? "",
        汁物: recordMeal.soup ?? "",
        その他: recordMeal.other ?? "",
        カロリー: recordMeal.totalCalories ?? 0,
      },
    };
    const res = await $fetch("http://127.0.0.1:8000/api/recordmeal", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    return res;
  } catch {
    return false;
  }
};

export const GetWeeklyMealService = async (id: string) => {
  try {
    const res = await $fetch<{ weekMeals: DayMeal[] }>(
      `http://127.0.0.1:8000/api/weeklymeal/${id}`,
      { method: "GET" }
    );
    return res.weekMeals;
  } catch {
    return null;
  }
};

export const GenerateWeeklyMealService = async (id: string) => {
  try {
    return await $fetch<any>(
      `http://127.0.0.1:8000/api/generate_weekly_meal/${id}`,
      { method: "POST" }
    );
  } catch (e) {
    return false;
  }
};
