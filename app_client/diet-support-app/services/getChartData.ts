import type { ChartData } from "chart.js";

export const GetChartDataService = async (
  id: string,
) => {
  try {
    return await $fetch<ChartData<"line"> | null>(
      `http://127.0.0.1:8000/api/recordweight/${id}?period=yearly`
    );
  } catch (e) {
    return null;
  }
};

const mockChartData = {
  labels: [
    "1月",
    "2月",
    "3月",
    "4月",
    "5月",
    "6月",
    "7月",
    "8月",
    "9月",
    "10月",
    "11月",
    "12月",
  ],
  datasets: [
    {
      label: "体重(kg)",
      data: [65, 66, 65.5, 66.5, 67, 66, 67.5, 68, 67, 66, 65, 64],
      borderColor: "#36A2EB",
      backgroundColor: "#9BD0F5",
    },
  ],
};
