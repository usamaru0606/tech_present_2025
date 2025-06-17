import { useRouter } from "vue-router";
import type { GoalSettingItems } from "~/model/goalsettingitem";

export const GoalSettingViewModel = () => {
  const router = useRouter();
  const userIdStore = useUserIdStore();

  const formatDate = (date: Date) =>
    date.toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });

  const parseDateString = (
    str: string | null
  ): { year: number; month: number; day: number } => {
    if (!str) {
      const now = new Date();
      return {
        year: now.getFullYear(),
        month: now.getMonth() + 1,
        day: now.getDate(),
      };
    }
    const [y, m, d] = str.split("/").map(Number);
    return { year: y, month: m, day: d };
  };

  const today = formatDate(new Date());

  const goaldate = reactive({
    year: new Date().getFullYear(),
    month: new Date().getMonth() + 1,
    day: new Date().getDate(),
  });

  const problemError = ref(false);

  const settingItem = reactive<GoalSettingItems>({
    userId: userIdStore.getUserId(),
    height: 0,
    weight: 0,
    startDate: today,
    problem: "",
    goalDate: today,
    goalWeight: 0,
  });

  const problemOptions = [
    "",
    "体重を減らしたい",
    "筋肉をつけたい",
    "健康を維持したい",
    "生活習慣を改善したい",
    "その他",
  ];

  const loadInitialSettings = async () => {
    const userId = userIdStore.getUserId();
    if (!userId) return;

    try {
      const data: GoalSettingItems | null =
        await useGetGoalSettingServise().Execute(userId);
      if (!data) return console.error("目標設定データの取得に失敗しました");

      Object.assign(settingItem, {
        ...data,
        userId,
      });

      const parsed = parseDateString(data.goalDate);
      goaldate.year = parsed.year;
      goaldate.month = parsed.month;
      goaldate.day = parsed.day;
    } catch (e) {
      console.error("目標設定データの取得に失敗しました", e);
    }
  };

  const OnConfirm = async () => {
    if (!settingItem.problem) {
      problemError.value = true;
      return;
    }

    problemError.value = false;

    const success = await saveGoalSettings();
    if (!success) {
      alert("設定に失敗しました");
      return;
    }

    await router.push("/");
  };

  const saveGoalSettings = async () => {
    const formattedGoalDate = formatDate(
      new Date(goaldate.year, goaldate.month - 1, goaldate.day)
    );

    const payload: GoalSettingItems = {
      ...settingItem,
      goalDate: formattedGoalDate,
    };

    try {
      return await useUpdateGoalSetting().Execute(payload);
    } catch (e) {
      console.error("保存に失敗:", e);
      return false;
    }
  };

  onMounted(loadInitialSettings);

  return {
    settingItem,
    problemOptions,
    problemError,
    goaldate,
    OnConfirm,
  };
};
