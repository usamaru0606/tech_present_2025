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

  onMounted(async () => {
    const userId = useUserIdStore().getUserId();
    if (!userId) return;

    const res = await useGetWeeklyMeal().Execute(userId);
    if (!res) return;

    weeklyMeals.value = res.map((day: any, i: number) => {
      // 日付・曜日は自分で再セットしても良いし、
      // APIに入っていればそちらを優先してもOK
      const date = addDays(today, i);
      return {
        date: day.date ?? format(date, "M月d日", { locale: ja }),
        label: day.label ?? daysOfWeek[date.getDay()],
        meals: day.meals ?? {
          breakfast: { ...initMeal, ...day.breakfast },
          lunch: { ...initMeal, ...day.lunch },
          dinner: { ...initMeal, ...day.dinner },
        },
      };
    });
  });

  return {
    currentTab,
    mealCategories,
    mealTabs,
    weeklyMeals,
    GetTotalCalories,
  };
};
