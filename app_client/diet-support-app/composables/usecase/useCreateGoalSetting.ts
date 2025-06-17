import type { GoalSettingItems } from "~/model/goalsettingitem";
import { CreateGoalSettingServise } from "~/services/goalsetting";

export const useCreateGoalSetting = () => {
  const Execute = async (goalSettingItems: any) => {
    const goalSettingItem: GoalSettingItems = {
      userId: null,
      height: goalSettingItems.height,
      weight: goalSettingItems.weight,
      startDate: goalSettingItems.startDate,
      problem: goalSettingItems.selectedProblem,
      goalWeight: goalSettingItems.goalWeight,
      goalDate: goalSettingItems.goalDate,
    };

    return CreateGoalSettingServise(goalSettingItem);
  };

  return {
    Execute,
  };
};
