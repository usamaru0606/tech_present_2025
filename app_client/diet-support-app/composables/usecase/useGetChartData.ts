import { useGetChartDataServise } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (userId:number) => {

    return useGetChartDataServise(userId);
  };

  return {
    Execute,
  };
};
