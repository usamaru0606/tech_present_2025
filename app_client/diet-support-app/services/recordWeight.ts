import type { RecordWeight } from "~/model/recordweight";

export const RecordWeightServise = async (recordWeight: RecordWeight) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/recordweight", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: recordWeight.userId,
        recordDate: recordWeight.recordDate,
        weight: recordWeight.recordWeight,
      }),
    });

    return res;
  } catch {
    return false;
  }
};
