import type { ChartData } from "chart.js";

export const GetChartDataServise = async (id: string) => {
  type chartDataType = ChartData<"line">;
  try {
    return await $fetch<chartDataType | null>(
      `http://127.0.0.1:8000/recordweight/${id}`
    );
  } catch {
    return mockChartData;
  }
};

const startDate = new Date(2025, 4, 1)
const mockChartData: ChartData<'line'> = {
  labels: Array.from({ length: 365 }, (_, i) => {
  const d = new Date(startDate);
  d.setDate(startDate.getDate() + i);
  return `${d.getMonth() + 1}/${d.getDate()}`;
}),
  datasets: [
    {
      label: '体重 (kg)',
      data: Array.from({ length: 365 }, () => +(60 + Math.random() * 5).toFixed(1)),
    },
  ],
}
