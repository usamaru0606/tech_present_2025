import { GetTrainingMenuService } from "~/services/training";

export const useGetTrainingMenu = () => {
  const Execute = async (userId:string) => {

    return GetTrainingMenuService(userId);
  };

  return {
    Execute,
  };
};
