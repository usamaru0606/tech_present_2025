import type { Meal, MealKey } from "~/model/meal";
import type { RecordMeal } from "~/model/recoradmeal";

export const GetToDayMenuService = async (id: string) => {
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

export const RecordMealService = async (recordMeal: RecordMeal) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/recordmeal", {
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
};

export const GetWeeklyMealService = async (id: string) => {
  try {
    return await $fetch<Record<MealKey, Meal>[] | null>(
      `http://127.0.0.1:8000/weeklymeal/${id}`
    );
  } catch {
    return weeklyMockMeals;
  }
};

const weeklyMockMeals: Record<MealKey, Meal>[] = [
  {
    breakfast: {
      stapleFood: "トースト",
      mainDish: "スクランブルエッグ",
      sideDish: "バナナ",
      soup: "コーンスープ",
      other: "コーヒー",
      totalCalories: 420,
    },
    lunch: {
      stapleFood: "うどん",
      mainDish: "天ぷら",
      sideDish: "小松菜のおひたし",
      soup: "味噌汁",
      other: "みかん",
      totalCalories: 610,
    },
    dinner: {
      stapleFood: "白ごはん",
      mainDish: "鶏の照り焼き",
      sideDish: "ほうれん草の胡麻和え",
      soup: "わかめスープ",
      other: "ヨーグルト",
      totalCalories: 530,
    },
  },
  {
    breakfast: {
      stapleFood: "おにぎり",
      mainDish: "焼き鮭",
      sideDish: "卵焼き",
      soup: "味噌汁",
      other: "お茶",
      totalCalories: 480,
    },
    lunch: {
      stapleFood: "スパゲッティ",
      mainDish: "ミートソース",
      sideDish: "グリーンサラダ",
      soup: "野菜スープ",
      other: "プリン",
      totalCalories: 680,
    },
    dinner: {
      stapleFood: "玄米",
      mainDish: "豚の生姜焼き",
      sideDish: "キャベツ炒め",
      soup: "玉ねぎスープ",
      other: "果物",
      totalCalories: 550,
    },
  },
  {
    breakfast: {
      stapleFood: "クロワッサン",
      mainDish: "ベーコンエッグ",
      sideDish: "ヨーグルト",
      soup: "トマトスープ",
      other: "ミルク",
      totalCalories: 460,
    },
    lunch: {
      stapleFood: "ラーメン",
      mainDish: "チャーシュー",
      sideDish: "もやしナムル",
      soup: "ラーメンスープ",
      other: "杏仁豆腐",
      totalCalories: 700,
    },
    dinner: {
      stapleFood: "雑穀米",
      mainDish: "サバの味噌煮",
      sideDish: "ひじき煮",
      soup: "味噌汁",
      other: "キウイ",
      totalCalories: 520,
    },
  },
  {
    breakfast: {
      stapleFood: "ホットケーキ",
      mainDish: "ウインナー",
      sideDish: "フルーツミックス",
      soup: "コーンスープ",
      other: "オレンジジュース",
      totalCalories: 500,
    },
    lunch: {
      stapleFood: "そば",
      mainDish: "かき揚げ",
      sideDish: "ほうれん草おひたし",
      soup: "けんちん汁",
      other: "バナナ",
      totalCalories: 630,
    },
    dinner: {
      stapleFood: "白ごはん",
      mainDish: "ハンバーグ",
      sideDish: "ブロッコリーサラダ",
      soup: "わかめスープ",
      other: "ゼリー",
      totalCalories: 540,
    },
  },
  {
    breakfast: {
      stapleFood: "ベーグル",
      mainDish: "ハムエッグ",
      sideDish: "りんご",
      soup: "ポタージュ",
      other: "紅茶",
      totalCalories: 430,
    },
    lunch: {
      stapleFood: "チャーハン",
      mainDish: "餃子",
      sideDish: "春雨サラダ",
      soup: "中華スープ",
      other: "杏仁豆腐",
      totalCalories: 690,
    },
    dinner: {
      stapleFood: "白ごはん",
      mainDish: "麻婆豆腐",
      sideDish: "もやし炒め",
      soup: "卵スープ",
      other: "みかん",
      totalCalories: 510,
    },
  },
  {
    breakfast: {
      stapleFood: "サンドイッチ",
      mainDish: "ツナマヨ",
      sideDish: "キャロットラペ",
      soup: "野菜スープ",
      other: "牛乳",
      totalCalories: 440,
    },
    lunch: {
      stapleFood: "カレーライス",
      mainDish: "チキンカレー",
      sideDish: "ピクルス",
      soup: "コンソメスープ",
      other: "ヨーグルト",
      totalCalories: 710,
    },
    dinner: {
      stapleFood: "白ごはん",
      mainDish: "鮭のホイル焼き",
      sideDish: "煮物",
      soup: "味噌汁",
      other: "梨",
      totalCalories: 540,
    },
  },
  {
    breakfast: {
      stapleFood: "フレンチトースト",
      mainDish: "目玉焼き",
      sideDish: "オレンジ",
      soup: "オニオンスープ",
      other: "紅茶",
      totalCalories: 460,
    },
    lunch: {
      stapleFood: "冷やし中華",
      mainDish: "蒸し鶏",
      sideDish: "きゅうりとトマト",
      soup: "中華スープ",
      other: "アイス",
      totalCalories: 670,
    },
    dinner: {
      stapleFood: "白ごはん",
      mainDish: "照り焼きチキン",
      sideDish: "サラダ",
      soup: "味噌汁",
      other: "ぶどう",
      totalCalories: 530,
    },
  },
];
