export type Exercise = { trainingMenu: string; trainingTime: number; calories: number };

export type Training = {
 exercises: Exercise[];
  totalCalories: number|null;
};
