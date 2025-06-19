import { GetToDayMenuServise } from "~/services/getMenu";

export const useGetToDayMenu = () => {
  const Execute = async (userId:string) => {

    return GetToDayMenuServise(userId);
  };

  return {
    Execute,
  };
};
