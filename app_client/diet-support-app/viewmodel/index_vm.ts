import type { ChartData } from "chart.js";

export const IndexViewModel = () => {
  const router = useRouter();
  const userIdStore = useUserIdStore();
  const isDialogOpen = ref(false);
  const userId = ref<string | null>(null);
  type chartDataType = ChartData<"line">;
  var chartData = ref<chartDataType>({
    labels: [],
    datasets: [
      {
        label: "",
        data: [0],
      },
    ],
  });

  const loadChartData = async () => {
    try {
      userId.value = userIdStore.userId;
      if (!userId.value) return;

      const newChartData = await useGetChartData().Execute(userId.value);
      if (!newChartData) return;
      chartData.value = newChartData;
    } catch {
      return;
    }
  };

  const GoGoalSetting = async () => {
    if (!userId.value) return;
    await router.push("/goalsetting");
  };

  function OpenRecordWeightDialog() {
    if (!userId.value) return;
    isDialogOpen.value = true;
  }

  const OnRecordWeightDialogClosed = async(val: boolean) =>{
    if (!val) {
    await nextTick(); // ダイアログ閉じた直後に
    if (loadChartData) await loadChartData();
  }
  }

  onMounted(loadChartData);

  return {
    userId,
    chartData,
    isDialogOpen,
    loadChartData,
    GoGoalSetting,
    OpenRecordWeightDialog,
    OnRecordWeightDialogClosed
  };
};
