import type { Exercise, Training } from "~/model/training";

export const TrainingCardViewModel = () => {
  const userId = useUserIdStore().getUserId();
  const isOpenRecordTrainingDialog = ref(false);

  // 今日のトレーニングメニュー（単一セッション）
  const trainingMenu = ref<Training>({
    exercises: [],
    totalCalories: null,
  });

  const CalculateTotalCalories = (exercises: Exercise[]): number => {
    return exercises.reduce((sum, item) => sum + (item.calories ?? 0), 0);
  };

  // APIから取得してtrainingMenuを更新する処理例
  onMounted(async () => {
    if (!userId) return;
    const res = await useGetTrainingMenu().Execute(userId);
    if (!res) return;
    trainingMenu.value = { ...trainingMenu.value, ...res };
    trainingMenu.value.totalCalories = CalculateTotalCalories({...res});
  });

  const OpenRecordTrainingDialog = () => {
    if (!userId) return;
    isOpenRecordTrainingDialog.value = true;
  };

  return {
    isOpenRecordTrainingDialog,
    trainingMenu,
    OpenRecordTrainingDialog,
  };
};
