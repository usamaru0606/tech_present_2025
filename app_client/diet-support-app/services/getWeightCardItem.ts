import type { CardItem } from "~/model/weightCardItem";

export const GetWeightCardItemService = async (id: string) => {
  try {
    return await $fetch<CardItem | null>(
      `http://127.0.0.1:8000/weightcarditem/${id}`
    );
  } catch {
    return mockCardItemData;
  }
};

const mockCardItemData: CardItem= {
    weight: 60,
    lastMonthWeight: 58,
    goalWeight: 55,
    goalDate: '2026/01/01',
    startDate: '2025/01/01'
}
