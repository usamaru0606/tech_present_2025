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