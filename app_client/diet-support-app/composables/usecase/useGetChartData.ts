import { GetChartDataServise } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (userId:string) => {

    return GetChartDataServise(userId);
  };

  return {
    Execute,
  };
};
