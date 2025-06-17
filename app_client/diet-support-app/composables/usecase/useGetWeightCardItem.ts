import { GetWeightCardItemServise } from "~/services/getWeightCardItem";

export const useGetWeightCardItem = () => {
  const Execute = async (userId:string) => {

    return GetWeightCardItemServise(userId);
  };

  return {
    Execute,
  };
};
