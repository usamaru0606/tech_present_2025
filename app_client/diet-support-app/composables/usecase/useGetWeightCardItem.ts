import { GetWeightCardItemService } from "~/services/getWeightCardItem";

export const useGetWeightCardItem = () => {
  const Execute = async (id: string) => {
    return GetWeightCardItemService(id);
  };

  return {
    Execute,
  };
};
