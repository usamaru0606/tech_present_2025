export type Exercise = { trainingMenu: string|null; trainingTime: number|null; calories: number|null };

export type Training = {
 exercises: Exercise[];
  totalCalories: number|null;
};
