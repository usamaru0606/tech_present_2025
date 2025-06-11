import { useRouter } from "vue-router";

export const GoalSettingViewModel = () => {
  const router = useRouter();
  const userWeightStore = useUserWeightStore();
  const userIdStore = useUserIdStore();

  const settingItem = reactive({
    userId: userIdStore.getUserId(),
    selectedProblem: "",
    goalWeight: userWeightStore.getUserWeight() ?? 0,
    goaldate: new Date().toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }),
  });
  const today = computed(() =>
    new Date().toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    })
  );
  const problemOptions = [
    "",
    "体重を減らしたい",
    "筋肉をつけたい",
    "健康を維持したい",
    "生活習慣を改善したい",
    "その他",
  ];
  const currentWeight = ref(userWeightStore.getUserWeight() ?? 0);
  const goaldate = reactive({
    year: new Date().getFullYear(),
    month: new Date().getMonth() + 1,
    day: new Date().getDate(),
  });
  const problemError = ref(false);

  const OnConfirm = async () => {
    if (!settingItem.selectedProblem) {
      return (problemError.value = true);
    }
    problemError.value = false;

    if (!(await SaveGoalSettings())){
       return alert('設定に失敗しました');
    } 
    await router.push("/");
  };

  const SaveGoalSettings = async () => {
    settingItem.goaldate = new Date(
      goaldate.year,
      goaldate.month,
      goaldate.day
    ).toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });

    try {
      var res = await useUpdateGoalSetting().Execute(settingItem);
      return res;
    } catch {
      return false;
    }
  };

  return {
    today,
    settingItem,
    problemOptions,
    problemError,
    currentWeight,
    goaldate,
    OnConfirm,
  };
};
