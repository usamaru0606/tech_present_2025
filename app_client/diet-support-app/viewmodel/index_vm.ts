import type { ChartData } from "chart.js";

export const IndexViewModel = () => {
  const userIdStore = useUserIdStore();
  const userId = ref<number | null>(null);
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

  onMounted(async () => {
    userId.value = userIdStore.getUserId();
    Reload();
  });


  const Reload = async () => {
    if(!userId.value) return;

    const newChartData = await useGetChartData().Execute(userId.value);
    if(!newChartData) return;
    chartData.value = newChartData
  };

  const GoGoalSetting = async () =>{
    if(!userId.value) return;
  }

  return {
    userId,
    chartData,
    Reload,
    GoGoalSetting
  };
};
