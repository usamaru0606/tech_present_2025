import { GetChartDataService } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (
    id: string,
  ) => {
    return GetChartDataService(id);
  };

  return {
    Execute,
  };
};
