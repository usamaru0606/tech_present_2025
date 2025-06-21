import type { Meal, MealKey } from "~/model/meal";
import type { RecordMeal } from "~/model/recoradmeal";

export const GetToDayMenuServise = async (id: string) => {
  try {
    return await $fetch<Record<MealKey, Meal> | null>(
      `http://127.0.0.1:8000/todaymenu/${id}`
    );
  } catch {
    return mock;
  }
};

const mock: Record<MealKey, Meal> = {
  breakfast: {
    stapleFood: "パン",
    mainDish: "目玉焼き",
    sideDish: "フルーツ",
    soup: "スープ",
    other: "コーヒー",
    totalCalories: 450,
  },
  lunch: {
    stapleFood: "パスタ",
    mainDish: "ミートソース",
    sideDish: "サラダ",
    soup: "コンソメスープ",
    other: "ヨーグルト",
    totalCalories: 650,
  },
  dinner: {
    stapleFood: "白ごはん",
    mainDish: "焼き鮭",
    sideDish: "お浸し",
    soup: "味噌汁",
    other: "なし",
    totalCalories: 500,
  },
};

export const RecordMealServise = async(recordMeal:RecordMeal) =>{
  try {
    const res = await $fetch("http://127.0.0.1:8000/recordweight", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: recordMeal.userId,
        recordDate: recordMeal.recordDate,
        mealTiming: recordMeal.mealTiming,
        stapleFood: recordMeal.stapleFood,
        mainDish: recordMeal.mainDish,
        sideDish: recordMeal.sideDish,
        soup: recordMeal.soup,
        other: recordMeal.other,
        totalCalories: recordMeal.totalCalories,
      }),
    });
    return res;
  } catch {
    return false;
  }
}
