import type { ChartData } from "chart.js";

export const IndexViewModel = () => {
  const router = useRouter();
  const userIdStore = useUserIdStore();
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
    try{
    userId.value = userIdStore.userId;
    if(!userId.value) return;

    const newChartData = await useGetChartData().Execute(userId.value);
    if(!newChartData) return;
    chartData.value = newChartData
    }
    catch{
      return;
    }
  };

  const GoGoalSetting = async () =>{
    if(!userId.value) return;
    await router.push('/goalsetting');
  }

  onMounted(loadChartData);

  return {
    userId,
    chartData,
    loadChartData,
    GoGoalSetting
  };
};
