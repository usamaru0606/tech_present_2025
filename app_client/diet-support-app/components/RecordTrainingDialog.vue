<template>
  <CDialog
    v-model="internalValue"
    title="トレーニングを記録"
    emitBtnLabel="保存"
    :width="800"
    :height="600"
    @confirm="emitConfirm"
  >
    <v-container fluid class="pa-0 d-flex flex-column container">
      <v-row class="px-4 pt-2" align="center">
        <v-icon color="primary" size="32">mdi-dumbbell</v-icon>
        <p class="title ml-3 mb-0">トレーニング内容</p>
      </v-row>

      <v-row dense class="px-4 pt-4 flex-grow-1 scroll-y">
        <template v-for="train in tempTraining.trainings">
        <v-col cols="6" class="pb-4">
          <CTextField
            icon="mdi-dumbbell"
            icon-color="blue"
            label="種目"
            v-model="train.trainingMenu"
          />
        </v-col>

        <v-col cols="3" class="pb-4">
          <CTextField
            icon="mdi-timer"
            icon-color="green"
            label="時間（分）"
            type="number"
            v-model.number="train.trainingTime"
          />
        </v-col>

        <v-col cols="3" class="pb-4">
          <CTextField
            icon="mdi-fire"
            icon-color="deep-orange"
            label="消費カロリー"
            type="number"
            v-model.number="train.calories"
          />
        </v-col>
        </template>
      </v-row>
    </v-container>
  </CDialog>
</template>

<script setup lang="ts">
import type { Training } from "~/model/training";

const props = defineProps<{
  modelValue: boolean;
  modelTraining: Training;
}>();

const emit = defineEmits<{
  (e: "update:modelValue", val: boolean): void;
  (e: "update:modelTraining", val: Training): void;
}>();

const internalValue = computed({
  get: () => props.modelValue,
  set: (val: boolean) => emit("update:modelValue", val),
});

// 入力対象
const tempTraining = reactive<Training>({
  trainings: [{ trainingMenu: null, trainingTime: null, calories: null }],
  totalCalories: 0,
});


// 保存処理
const emitConfirm = async () => {
  try {
    const userId = useUserIdStore().getUserId()!;
    const res = await useRecordTraining().Execute(userId, tempTraining);
    if (!res) alert("記録できませんでした");
  } catch {
    alert("記録できませんでした");
  } finally {
    emit("update:modelValue", false);
  }
};

// ダイアログが開いたら props からコピー
watch(
  () => props.modelValue,
  (opened) => {
    if (opened && props.modelTraining) {
      tempTraining.trainings = JSON.parse(JSON.stringify(props.modelTraining.trainings));
      tempTraining.totalCalories = props.modelTraining.totalCalories;
    }
  },
  { immediate: true }
);
</script>

<style scoped>
.container {
  height: 100%;
}

.scroll-y {
  overflow-y: auto;
}

.title {
  font-weight: 600;
  font-size: 1.4rem;
}

.v-row[style*="overflow-y: auto"]::-webkit-scrollbar {
  width: 8px;
}
.v-row[style*="overflow-y: auto"]::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}
</style>
