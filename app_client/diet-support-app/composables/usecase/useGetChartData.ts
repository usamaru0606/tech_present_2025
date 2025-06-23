import { GetChartDataService } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (userId:string) => {

    return GetChartDataService(userId);
  };

  return {
    Execute,
  };
};
