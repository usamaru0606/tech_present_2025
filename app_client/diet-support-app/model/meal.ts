export type MealCategoryKey =
  | "stapleFood"
  | "mainDish"
  | "sideDish"
  | "soup"
  | "other";

export type MealKey = "breakfast" | "lunch" | "dinner";

export type Meal = {
  [key in MealCategoryKey]: string|null;
} & {
  totalCalories: number|null;
};

export type DayMeal = {
  date: string;
} & Record<MealKey, Meal>;