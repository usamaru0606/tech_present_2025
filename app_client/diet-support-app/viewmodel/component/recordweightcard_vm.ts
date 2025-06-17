import type { CardItem } from "~/model/weightCardItem";

export const RecordWeightCardViewModel = () => {
  const userWeightStore = useUserWeightStore();
  const userIdStore = useUserIdStore();

  const todayDate = new Date();
  const MS_PER_DAY = 1000 * 60 * 60 * 24;
  const currentWeight = ref<number | null>(null);
  const continuationDays = ref<number | null>(0);
  const weightDiff = ref<number | null>(null);
  const weightDiffAllDate = ref<number | null>(null);
  const cardItem = reactive<CardItem>({
    weight: null,
    lastMonthWeight: null,
    goalWeight: null,
    goalDate: null,
    startDate: null,
  });

  const loadCardItem = async () => {
    const userId = userIdStore.getUserId();
    if (!userId) return;

    try {
      const res = await useGetWeightCardItem().Execute(userId);
      Object.assign(cardItem, res);
    } catch (e) {
      console.error("体重カードデータの取得に失敗しました", e);
    }
  };

  watchEffect(() => {
    const cw = currentWeight.value;
    const { lastMonthWeight, weight } = cardItem;

    if (cw != null && lastMonthWeight != null) {
      weightDiff.value = +(cw - lastMonthWeight).toFixed(1);
    } else {
      weightDiff.value = null;
    }

    if (cw != null && weight != null) {
      weightDiffAllDate.value = +(cw - weight).toFixed(1);
    } else {
      weightDiffAllDate.value = null;
    }

    if (cardItem.startDate) {
      const diffTime =
        todayDate.getTime() - parseDateString(cardItem.startDate).getTime();
      continuationDays.value = Math.max(0, Math.floor(diffTime / MS_PER_DAY));
    } else {
      continuationDays.value = 0;
    }
  });

  function parseDateString(str: string): Date {
    const [y, m, d] = str.split("/").map(Number);
    return new Date(y, m - 1, d);
  }

  watch(
    () => userWeightStore.userWeight,
    (newWeight) => {
      currentWeight.value = newWeight;
    },
    { immediate: true }
  );

  watch(
    () => userIdStore.userId,
    (newUserId) => {
      if (newUserId) loadCardItem();
    }
  );

  onMounted(loadCardItem);

  return {
    cardItem,
    currentWeight,
    continuationDays,
    weightDiff,
    weightDiffAllDate,
  };
};
