import { useGetChartDataServise } from "~/services/getChartData";

export const useGetChartData = () => {
  const Execute = async (userId:string) => {

    return useGetChartDataServise(userId);
  };

  return {
    Execute,
  };
};
