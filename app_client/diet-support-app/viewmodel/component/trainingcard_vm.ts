import { ref, onMounted } from "vue";
import type { Exercise, Training } from "~/model/training";
import { GetTrainingMenuService } from '~/services/training';

export const TrainingCardViewModel = () => {
  const userIdStore = useUserIdStore();
  const userId = userIdStore.getUserId();
  const isOpenRecordTrainingDialog = ref(false);

  // 今日のトレーニングメニュー（単一セッション）
  const trainingMenu = ref<Training>({
    exercises: [],
    totalCalories: null,
  });

  const CalculateTotalCalories = (exercises: Exercise[] | null): number => {
    if (!Array.isArray(exercises)) {
      return 0;
    }
    return exercises.reduce((sum, item) => sum + (item.calories ?? 0), 0);
  };

  const totalCalories = computed(() => CalculateTotalCalories(trainingMenu.value.exercises));

  // APIから取得してtrainingMenuを更新する処理例
  onMounted(async () => {
    if (!userId) return;
    const exercises = await GetTrainingMenuService(userId);
    if (!exercises) return;
    trainingMenu.value.exercises = exercises;
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
