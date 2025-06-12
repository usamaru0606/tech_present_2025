import type { CardItem } from "~/model/weightCardItem";

export const RecordWeightCardViewModel = () => {
  const cardItem = reactive<CardItem>({
    initialWeight: null,
    currentWeight: null,
    lastMonthWeight: null,
    goalWeight: null,
    weightDiff: null,
    weightDiffAllDate: null,
    goalDate: "",
    today: "",
    continuationDays: null,
  });
  const registeredDate = new Date("2025-05-01");
  const todayDate = new Date();

  onMounted(async() =>{
    if(cardItem.currentWeight&&cardItem.lastMonthWeight){
        cardItem.weightDiff = +(cardItem.currentWeight - cardItem.lastMonthWeight).toFixed(1);
    }
    if(cardItem.currentWeight&&cardItem.initialWeight){
        cardItem.weightDiffAllDate = +(cardItem.currentWeight - cardItem.initialWeight).toFixed(1);
    }
    cardItem.today = new Date().toLocaleDateString("ja-JP", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  });
  const diffTime = todayDate.getTime() - registeredDate.getTime();
  cardItem.continuationDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  });

  return{
    cardItem,
  }
};
