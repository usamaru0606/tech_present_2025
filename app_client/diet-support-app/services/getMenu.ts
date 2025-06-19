import type { Meal, MealKey } from "~/model/meal";

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
