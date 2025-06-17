export const RegisterSubViewModel = () => {
  const router = useRouter();
  const userInfo = reactive({
    height: 100,
    weight: 40,
    startDate: new Date().toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }) as string | null,
    selectedProblem: "" as string | null,
    goalWeight: 0 as number | null,
    goaldate: "" as string | null,
  });
  const error = ref("");
  const expandedIndex = ref(null);
  const problemOptions = [
    "",
    "体重を減らしたい",
    "筋肉をつけたい",
    "健康を維持したい",
    "生活習慣を改善したい",
    "その他",
  ];

  const goaldate = reactive({
    year: new Date().getFullYear(),
    month: new Date().getMonth() + 1,
    day: new Date().getDate(),
  });

  const RegisterGoal = async () => {
    if (!Validate()) return;

    SetGoalItems();
    try {
      const res = await useAddUser().Execute(userInfo);
      if (!res) return (error.value = "登録に失敗しました");
      await router.push("/login");
    } catch (e) {
      error.value = "登録に失敗しました";
    }
  };

  const SetGoalItems = () => {
    if (!expandedIndex.value) {
      userInfo.startDate = null;
      userInfo.selectedProblem = null;
      userInfo.goalWeight = null;
      userInfo.goaldate = null;
    } else {
      userInfo.goaldate = new Date(
        goaldate.year,
        goaldate.month,
        goaldate.day
      ).toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      });
    }
  };

  const Validate = (): boolean => {
    if (expandedIndex.value != null) {
      if (
        !userInfo.selectedProblem ||
        !userInfo.goalWeight ||
        !userInfo.goaldate
      ) {
        error.value = "すべての項目を入力してください";
        return false;
      }
    }
    error.value = "";
    return true;
  };

  return {
    userInfo,
    error,
    problemOptions,
    goaldate,
    expandedIndex,
    RegisterGoal,
  };
};
