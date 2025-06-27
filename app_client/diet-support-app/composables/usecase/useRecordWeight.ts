import type { RecordWeight } from "~/model/recordweight";
import { RecordWeightService } from "~/services/recordWeight";

export const useRecordWeight = () => {
  const Execute = async (recordWeight: any) => {
    const Recordweight: RecordWeight = {
      userId: recordWeight.userId,
      recordWeight: recordWeight.currentWeight,
      recordDate: recordWeight.recordDate.toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }),
    };

    return RecordWeightService(Recordweight);
  };

  return {
    Execute,
  };
};
