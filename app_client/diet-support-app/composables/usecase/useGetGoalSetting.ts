import { GetGoalSettingService } from "~/services/goalsetting";

export const useGetGoalSetting = () => {
  const Execute = async (id: string) => {
    return GetGoalSettingService(id);
  };

  return {
    Execute,
  };
};
