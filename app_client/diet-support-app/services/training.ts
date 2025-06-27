import type { RecordTraining } from "~/model/recordtraining";
import type { TrainingSet } from "~/model/training";

export const GetTrainingMenuService = async (id: string) => {
  try {
    return await $fetch<TrainingSet[] | null>(
      `http://127.0.0.1:8000/api/trainingmenu/${id}`
    );
  } catch {
    return mockExercises;
  }
};

const mockExercises: TrainingSet[] = [
  { trainingMenu: "ジョギング", trainingTime: 30, calories: 200 },
  { trainingMenu: "腕立て伏せ", trainingTime: 20, calories: 100 },
  { trainingMenu: "肩ストレッチ", trainingTime: 10, calories: 20 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
  { trainingMenu: "準備運動", trainingTime: 5, calories: 10 },
];

export const RecordTrainingService = async(recordTraining:RecordTraining) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/api/recordtraining", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: recordTraining.userId,
        recordDate: recordTraining.recordDate,
        training:recordTraining.trainingMenu
      }),
    });

    return res;
  } catch {
    return false;
  }
}