<template>
  <CDialog v-model="internalValue" :width="450" :height="400" title="体重を記録する" emitBtnLabel="記録する" @confirm="onConfirm">
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録日</strong>
        <CDateSelector v-model:Year="currentDate.year" v-model:Month="currentDate.month" v-model:Day="currentDate.day"
          @vue:updated="updateRecordDate" :minmode="true" />
      </v-col>
    </v-row>

    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録体重</strong>
        <WeightSelector v-model="tempWeight" />
      </v-col>
    </v-row>
  </CDialog>
</template>

<script setup lang="ts">
const props = defineProps<{
  modelValue: boolean;
}>();

const emit = defineEmits<{
  (e: "update:modelValue", val: boolean): void;
}>();

const internalValue = computed({
  get: () => props.modelValue,
  set: (val: boolean) => emit("update:modelValue", val),
});

const userIdStore = useUserIdStore();
const userWeightStore = useUserWeightStore();
const today = new Date();

const currentDate = reactive({
  year: today.getFullYear(),
  month: today.getMonth() + 1,
  day: today.getDate(),
});

const tempWeight = ref<number>(userWeightStore.getUserWeight() ?? useUserInitWeightStore().getUserInitWeight()!);
const recordDate = ref<Date>(today);

watch(
  () => props.modelValue,
  (opened) => {
    if (opened) {
      tempWeight.value = userWeightStore.getUserWeight()?? useUserInitWeightStore().getUserInitWeight()!;
      recordDate.value = today;
      currentDate.year = recordDate.value.getFullYear();
      currentDate.month = recordDate.value.getMonth() + 1;
      currentDate.day = recordDate.value.getDate();
    }
  },
  { immediate: true }
);

const updateRecordDate = () => {
  recordDate.value = new Date(
    currentDate.year,
    currentDate.month - 1,
    currentDate.day
  );
};

const onConfirm = async () => {
  try {
    const userId = userIdStore.getUserId();
    if (!userId) return;

    const payload = {
      userId,
      currentWeight: tempWeight.value,
      recordDate: recordDate.value,
    };

    if (userId === "test") {
      if (isToday(payload.recordDate)) {
        userWeightStore.setUserWeight(payload.currentWeight);
      }
      emit("update:modelValue", false);
      return;
    }

    const res = await useRecordWeight().Execute(payload);
    if (!res) return alert("記録に失敗しました");

    if (isToday(payload.recordDate)) {
      userWeightStore.setUserWeight(payload.currentWeight);
    }
  } catch (e) {
    alert("記録に失敗しました");
  }
  finally {
    emit("update:modelValue", false);
  }
};

function isToday(date: Date) {
  const now = new Date();
  return (
    now.getFullYear() === date.getFullYear() &&
    now.getMonth() === date.getMonth() &&
    now.getDate() === date.getDate()
  );
}
</script>
