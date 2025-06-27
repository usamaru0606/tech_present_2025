import type { Meal, MealCategoryKey, MealKey } from "../../model/meal"; // 任意で分離した型をインポート

export const MealCardViewModel = () => {
    const router = useRouter();
  const userId = useUserIdStore().getUserId();
  const isOpenRecordMealDialog = ref(false);
  const mealTabs: { key: MealKey; label: string }[] = [
    { key: "breakfast", label: "朝食" },
    { key: "lunch", label: "昼食" },
    { key: "dinner", label: "夕食" },
  ];

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

  const selectedMeal = ref<MealKey>("breakfast");

  const initialMeal: Meal = {
    stapleFood: null,
    mainDish: null,
    sideDish: null,
    soup: null,
    other: null,
    totalCalories: null,
  };

  const menuItem: Record<MealKey, Ref<Meal>> = {} as Record<MealKey, Ref<Meal>>;

  for (const key of mealTabs.map((tab) => tab.key)) {
    menuItem[key] = ref({ ...initialMeal });
  }

  // 時間帯に応じて初期選択を変更
  onMounted(async () => {
    const hour = new Date().getHours();
    if (hour >= 3 && hour < 10) selectedMeal.value = "breakfast";
    else if (hour >= 10 && hour < 15) selectedMeal.value = "lunch";
    else selectedMeal.value = "dinner";

    await GetMenu();
  });

  const GetMenu = async () => {
    if (!userId) return;

    const res = await useGetToDayMenu().Execute(userId);
    if (!res) return;

    for (const key of mealTabs.map((tab) => tab.key)) {
      if (res[key]) {
        menuItem[key].value = {
          ...menuItem[key].value,
          ...res[key],
        };
      }
    }
  };

  const GoWeeklyMealPage = () => {
    if(!userId) return;
    router.push("/weeklymeal")
  };

  const OpenRecordMealDialog = () => {
    if(!userId) return;
    isOpenRecordMealDialog.value = true;
  };

  return {
    isOpenRecordMealDialog,
    mealTabs,
    mealCategories,
    selectedMeal,
    menuItem,
    OpenRecordMealDialog,
    GoWeeklyMealPage,
    GetMenu,
  };
};
