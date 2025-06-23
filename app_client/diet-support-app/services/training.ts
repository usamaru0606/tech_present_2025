import type { Exercise } from "~/model/training";

export const GetTrainingMenuService = async (id: string) => {
  try {
    return await $fetch<Exercise[] | null>(
      `http://127.0.0.1:8000/trainingmenu/${id}`
    );
  } catch {
    return mockExercises;
  }
};

const mockExercises: Exercise[] = [
  { trainingMenu: "ジョギング", trainingTime: 30, calories: 200 },
  { trainingMenu: "腕立て伏せ", trainingTime: 20, calories: 100 },
  { trainingMenu: "肩ストレッチ", trainingTime: 10, calories: 20 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
];
