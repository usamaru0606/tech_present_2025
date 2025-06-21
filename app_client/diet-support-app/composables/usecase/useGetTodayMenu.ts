import { GetToDayMenuServise } from "~/services/meal";

export const useGetToDayMenu = () => {
  const Execute = async (userId:string) => {

    return GetToDayMenuServise(userId);
  };

  return {
    Execute,
  };
};
