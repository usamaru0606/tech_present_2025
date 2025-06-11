import type { GoalSettingItems } from "~/model/goalsettingitem";


export const UpdateGoalSettingServise = async (goalSettingItems: GoalSettingItems) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/goalsetting/update", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: goalSettingItems.userId,
        problem:goalSettingItems.problem,
        goalDate: goalSettingItems.goalDate,
        goalWeight: goalSettingItems.goalWeight,
      }),
    });

    return res;
  } catch {
    return false;
  }
};