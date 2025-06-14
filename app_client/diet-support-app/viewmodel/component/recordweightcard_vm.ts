import type { CardItem } from "~/model/weightCardItem";

export const RecordWeightCardViewModel = () => {
  const userInfoStore = useUserInfoStore();
  const userWeightStore = useUserWeightStore();
  const cardItem = reactive<CardItem>({
    initialWeight: null,
    currentWeight: computed(() => userWeightStore.userWeight).value,
    lastMonthWeight: null,
    goalWeight: null,
    weightDiff: null,
    weightDiffAllDate: null,
    goalDate: "",
    today: new Date().toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }),
    registeredDate: new Date(userInfoStore.userInfo.signinDate),
    continuationDays: 0,
  });

  const todayDate = new Date();

  onMounted(async () => {
    cardItem.initialWeight = userInfoStore.userInfo.weight;
    if (cardItem.currentWeight && cardItem.lastMonthWeight) {
      cardItem.weightDiff = +(
        cardItem.currentWeight - cardItem.lastMonthWeight
      ).toFixed(1);
    }
    if (cardItem.currentWeight && cardItem.initialWeight) {
      cardItem.weightDiffAllDate = +(
        cardItem.currentWeight - cardItem.initialWeight
      ).toFixed(1);
    }
    const diffTime = todayDate.getTime() - cardItem.registeredDate!.getTime();
    if(!diffTime) {return cardItem.continuationDays = 0;} 
    cardItem.continuationDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
  });

  return {
    cardItem,
  };
};
