export interface CardItem {
  initialWeight: number | null;
  currentWeight: number | null;
  lastMonthWeight: number | null;
  goalWeight: number | null;
  weightDiff: number | null;
  weightDiffAllDate: number | null;
  continuationDays: number | null;
  goalDate: string;
  today: string;
};