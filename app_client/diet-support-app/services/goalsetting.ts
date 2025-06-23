import type { GoalSettingItems } from "~/model/goalsettingitem";

export const GetGoalSettingServise = async (id: string) => {
  try {
    return await $fetch<GoalSettingItems | null>(
      `http://127.0.0.1:8000/api/goalsetting/${id}`
    );
  } catch {
    return mockData;
  }
};

const mockData : GoalSettingItems ={
  userId: 'test',
  height: 170,
  weight: 65,
  problem: null,
  startDate: null,
  goalDate: null,
  goalWeight: null
}

export const UpdateGoalSettingServise = async (
  goalSettingItems: GoalSettingItems
) => {
  try {
    if (!goalSettingItems.userId) {
      throw new Error("userId is required");
    }
    const res = await $fetch(`http://127.0.0.1:8000/api/goalsetting/${goalSettingItems.userId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        problem: goalSettingItems.problem,
        startDate: goalSettingItems.startDate,
        goalDate: goalSettingItems.goalDate,
        goalWeight: goalSettingItems.goalWeight,
      }),
    });

    return res;
  } catch {
    return false;
  }
};
