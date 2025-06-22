import { GetWeightCardItemService } from "~/services/getWeightCardItem";

export const useGetWeightCardItem = () => {
  const Execute = async (userId:string) => {

    return GetWeightCardItemService(userId);
  };

  return {
    Execute,
  };
};
