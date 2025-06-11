import type { GoalSettingItems } from "~/model/goalsettingitem";
import { UpdateGoalSettingServise } from "~/services/goalsetting";

export const useUpdateGoalSetting = () => {
  const Execute = async (goalSettingItems: any) => {
    const goalSettingItem: GoalSettingItems = {
      userId: goalSettingItems.userId,
      problem: goalSettingItems.selectedProblem,
      goalWeight: goalSettingItems.goalWeight,
      goalDate: goalSettingItems.goalDate,
    };

    return UpdateGoalSettingServise(goalSettingItem);
  };

  return {
    Execute,
  };
};
