import type { RecordTraining } from "~/model/recordtraining";
import type { Training } from "~/model/training";
import { RecordTrainingService } from "~/services/training";

export const useRecordTraining = () => {
  const Execute = async (userid: string, traing: Training) => {
    const RecordTraining: RecordTraining = {
      userId: userid,
      recordDate: new Date().toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }),
      trainingMenu: traing,
    };

    return RecordTrainingService(RecordTraining);
  };

  return {
    Execute,
  };
};
