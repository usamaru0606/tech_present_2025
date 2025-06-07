import type { RecordWeight } from "~/model/recordweight";

export const RecordWeightServise = async (recordWeight: RecordWeight) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/recordweight", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        recordDate: recordWeight.recordDate.toLocaleDateString("ja-JP"),
        weight: recordWeight.recordWeight,
      }),
    });

    return res;
  } catch {
    return false;
  }
};
