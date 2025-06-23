import type { CardItem } from "~/model/weightCardItem";

export const GetWeightCardItemService = async (id: string) => {
  try {
    return await $fetch<CardItem | null>(
      `http://127.0.0.1:8000/api/weightcarditem/${id}`
    );
  } catch (e) {
    return null;
  }
};

const mockData: CardItem = {
  weight: 65,
  lastMonthWeight: 67,
  goalWeight: 60,
  goalDate: "2024-12-31",
  startDate: "2024-01-01",
};
