import type { GoalSettingItems } from "~/model/goalsettingitem";

export const GetGoalSettingServise = async (id: string) => {
  try {
    return await $fetch<GoalSettingItems | null>(
      `http://127.0.0.1:8000/goalsetting/${id}`
    );
  } catch {
    return null;
  }
};

export const CreateGoalSettingServise = async (
  goalSettingItems: GoalSettingItems
) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/goalsetting/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: goalSettingItems.userId,
        height: goalSettingItems.height,
        weight: goalSettingItems.weight,
        startDate: goalSettingItems.startDate,
        problem: goalSettingItems.problem,
        goalWeight: goalSettingItems.goalWeight,
        goalDate: goalSettingItems.goalDate,
      }),
    });

    return res;
  } catch {
    return false;
  }
};

export const UpdateGoalSettingServise = async (
  goalSettingItems: GoalSettingItems
) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/goalsetting/update", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: goalSettingItems.userId,
        height: goalSettingItems.height,
        weight: goalSettingItems.weight,
        startDate: goalSettingItems.startDate,
        problem: goalSettingItems.problem,
        goalWeight: goalSettingItems.goalWeight,
        goalDate: goalSettingItems.goalDate,
      }),
    });

    return res;
  } catch {
    return false;
  }
};
