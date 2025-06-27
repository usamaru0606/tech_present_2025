import { unref } from "vue";
import type { GoalSettingItems } from "~/model/goalsettingitem";
import { UpdateGoalSettingService } from "~/services/goalsetting";

export const useUpdateGoalSetting = () => {
  const Execute = async (goalSettingItems: any) => {
    const goalSettingItem: GoalSettingItems = {
      userId: unref(goalSettingItems.userId),
      height: goalSettingItems.height,
      weight: goalSettingItems.weight,
      startDate: goalSettingItems.startDate,
      problem: goalSettingItems.problem,
      goalWeight: goalSettingItems.goalWeight,
      goalDate: goalSettingItems.goalDate,
    };

    return UpdateGoalSettingService(goalSettingItem);
  };

  return {
    Execute,
  };
};
