import { useGetWeeklyMealService } from "~/services/meal";

export const useGetWeeklyMeal = () => {
  const Execute = async (userId:string) => {

    return useGetWeeklyMealService(userId);
  };

  return {
    Execute,
  };
};
