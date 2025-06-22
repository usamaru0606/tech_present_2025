import { GetToDayMenuService } from "~/services/meal";

export const useGetToDayMenu = () => {
  const Execute = async (userId:string) => {

    return GetToDayMenuService(userId);
  };

  return {
    Execute,
  };
};
