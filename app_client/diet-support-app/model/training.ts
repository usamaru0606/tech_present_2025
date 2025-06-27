export type TrainingSet = { trainingMenu: string | null; trainingTime: number | null; calories: number | null };

export type Training = {
  trainings: TrainingSet[];
  totalCalories: number | null;
};
