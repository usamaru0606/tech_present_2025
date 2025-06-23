import { GetGoalSettingService } from "~/services/goalsetting";

export const useGetGoalSetting = () => {
  const Execute = async (userId:string) => {

    return GetGoalSettingService(userId);
  };

  return {
    Execute,
  };
};
