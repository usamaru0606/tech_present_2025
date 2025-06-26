import type { TrainingSet, Training } from "~/model/training";
import { GetTrainingMenuService } from '~/services/training';

export const TrainingCardViewModel = () => {
  const userIdStore = useUserIdStore();
  const userId = userIdStore.getUserId();
  const isOpenRecordTrainingDialog = ref(false);

  // 今日のトレーニングメニュー（単一セッション）
  const trainingMenu = ref<Training>({
    trainings: [],
    totalCalories: null,
  });

  const CalculateTotalCalories = (exercises: TrainingSet[] | null): number => {
    if (!Array.isArray(exercises)) {
      return 0;
    }
    return exercises.reduce((sum, item) => sum + (item.calories ?? 0), 0);
  };

  // APIから取得してtrainingMenuを更新する処理例
  onMounted(async () => {
    if (!userId) return;
    const exercises = await GetTrainingMenuService(userId);
    if (!exercises) return;
    trainingMenu.value.trainings = exercises;
    trainingMenu.value.totalCalories = CalculateTotalCalories(exercises);
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
