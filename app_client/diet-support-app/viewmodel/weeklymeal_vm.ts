import { format, addDays } from "date-fns";
import { ja } from "date-fns/locale";
import type { Meal, MealCategoryKey, MealKey } from "~/model/meal";

export const WeeklyMealViewModel = () => {
  const currentTab = ref(0);

  const mealCategories: {
    key: MealCategoryKey;
    label: string;
    icon: string;
  }[] = [
    { key: "stapleFood", label: "主食", icon: "mdi-rice" },
    { key: "mainDish", label: "主菜", icon: "mdi-silverware-fork-knife" },
    { key: "sideDish", label: "副菜", icon: "mdi-leaf" },
    { key: "soup", label: "汁物", icon: "mdi-bowl" },
    { key: "other", label: "その他", icon: "mdi-dots-horizontal" },
  ];

  const mealTabs = [
    { key: "breakfast", label: "朝食" },
    { key: "lunch", label: "昼食" },
    { key: "dinner", label: "夕食" },
  ] as const;

  const initMeal: Meal = {
    stapleFood: "",
    mainDish: "",
    sideDish: "",
    soup: "",
    other: "",
    totalCalories: 0,
  };

  const daysOfWeek = ["日", "月", "火", "水", "木", "金", "土"] as const;
  const today = new Date();

  const weeklyMeals = ref(
    Array.from({ length: 7 }, (_, i) => {
      const date = addDays(today, i);
      return {
        date: format(date, "M月d日", { locale: ja }),
        label: daysOfWeek[date.getDay()],
        meals: {
          breakfast: { ...initMeal },
          lunch: { ...initMeal },
          dinner: { ...initMeal },
        },
      };
    })
  );

  const GetTotalCalories = (day: { meals: Record<MealKey, Meal> }) =>
    mealTabs.reduce(
      (sum, tab) => sum + (day.meals[tab.key].totalCalories ?? 0),
      0
    );

  const fetchWeeklyMeals = async () => {
    const userId = useUserIdStore().getUserId();
    if (!userId) return;
    const res = await useGetWeeklyMeal().Execute(userId);
    if (!res || !res.weekMeals) return;

    // APIのデータと「今日からの日付」を結びつけて表示
    weeklyMeals.value = Array.from({ length: 7 }, (_, i) => {
      const date = addDays(today, i);
      const dayOfWeek = daysOfWeek[date.getDay()];
      const mealData = res.weekMeals[i] || {};

      const normalizeMeal = (meal: any) => {
        if (!meal) return { ...initMeal };
        return {
          ...initMeal,
          ...meal,
          totalCalories: meal.totalCalories ?? meal.calories ?? 0,
        };
      };

      return {
        date: format(date, "M月d日", { locale: ja }),
        label: dayOfWeek,
        meals: {
          breakfast: normalizeMeal(mealData.breakfast),
          lunch: normalizeMeal(mealData.lunch),
          dinner: normalizeMeal(mealData.dinner),
        },
      };
    });
  };

  onMounted(fetchWeeklyMeals);

  return {
    currentTab,
    mealCategories,
    mealTabs,
    weeklyMeals,
    GetTotalCalories,
    fetchWeeklyMeals,
  };
};
