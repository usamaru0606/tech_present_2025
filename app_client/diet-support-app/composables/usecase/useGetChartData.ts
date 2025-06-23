import { GetChartDataService } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (
    id: string,
    period: "weekly" | "monthly" | "yearly"
  ) => {
    return GetChartDataService(id, period);
  };

  return {
    Execute,
  };
};
