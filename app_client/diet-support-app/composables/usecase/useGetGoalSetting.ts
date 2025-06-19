import { GetGoalSettingServise } from "~/services/goalsetting";

export const useGetGoalSetting = () => {
  const Execute = async (userId:string) => {

    return GetGoalSettingServise(userId);
  };

  return {
    Execute,
  };
};
