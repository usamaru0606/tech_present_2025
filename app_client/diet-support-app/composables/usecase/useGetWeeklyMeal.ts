import { GetWeeklyMealService } from "~/services/meal";

export const useGetWeeklyMeal = () => {
  const Execute = async (userId:string) => {

    return GetWeeklyMealService(userId);
  };

  return {
    Execute,
  };
};
