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
    // if(!userId.value) return;
    router.push('/goalsetting');
  }

  return {
    userId,
    chartData,
    Reload,
    GoGoalSetting
  };
};
