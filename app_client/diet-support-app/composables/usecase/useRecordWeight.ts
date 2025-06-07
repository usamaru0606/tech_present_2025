import type { RecordWeight } from "~/model/recordweight";
import { RecordWeightServise } from "~/services/recordWeight";

export const useRecordWeight = () => {
  const Execute = async (recordWeight: any) => {
    const Recordweight: RecordWeight = {
        recordWeight: recordWeight.currentWeight,
        recordDate: recordWeight.currentDate
    };

    return RecordWeightServise(Recordweight);
  };

  return {
    Execute,
  };
};
