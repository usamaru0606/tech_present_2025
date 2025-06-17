import { GetGoalSettingServise } from "~/services/goalsetting";

export const useGetGoalSettingServise = () => {
  const Execute = async (userId:string) => {

    return GetGoalSettingServise(userId);
  };

  return {
    Execute,
  };
};
