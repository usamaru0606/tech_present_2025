import { GetWeeklyMealService, GenerateWeeklyMealService } from "~/services/meal";

export const useGetWeeklyMeal = () => {
  const Execute = async (userId:string) => {

    return GetWeeklyMealService(userId);
  };

  return {
    Execute,
  };
};

export const useGenerateWeeklyMeal = () => {
  const Execute = async (userId: string) => {
    return GenerateWeeklyMealService(userId);
  };
  return { Execute };
};
