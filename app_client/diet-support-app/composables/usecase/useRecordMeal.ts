import type { RecordMeal } from "~/model/recoradmeal";
import { RecordMealService } from "~/services/meal";

export const useRecordMeal= () => {
  const Execute = async (id:string, mealitem:any, mealTiming:string) => {
    const RecordMeal: RecordMeal = {
        userId: id,
        recordDate: new Date().toLocaleDateString("ja-JP", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
        }),
        mealTiming: mealTiming,
        stapleFood: mealitem.selectedMeal,
        mainDish: mealitem.mainDish,
        sideDish: mealitem.sideDish,
        soup: mealitem.soup,
        other: mealitem.other,
        totalCalories: mealitem.totalCalories,
    };

    return RecordMealService(RecordMeal);
  };

  return {
    Execute,
  };
};
