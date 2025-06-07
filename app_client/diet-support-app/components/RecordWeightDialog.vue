<template>
  <CIconBtn
    label="体重を記録"
    icon="mdi-pencil"
    :isTextPrimary="true"
    @click="dialog = true"
  />

  <CDialog
    v-model="dialog"
    title="体重を記録する"
    emitBtnLabel="記録する"
    @confirm="OnConfirm"
  >
    <!-- 記録日 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録日</strong>
        <CDateSelector
          v-model:Year="currentDate.year"
          v-model:Month="currentDate.month"
          v-model:Day="currentDate.day"
          @vue:updated="UpdateBirthday"
        />
      </v-col>
    </v-row>

    <!-- 目標体重 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録体重</strong>
        <WeightSelector v-model="recordWeight.currentWeight" />
      </v-col>
    </v-row>
  </CDialog>
</template>

<script setup lang="ts">
const dialog = ref(false);
const recordWeight = reactive({
  currentWeight: 64.5,
  recordDate: new Date(),
})
const today = new Date();
const currentDate = reactive({
  year: today.getFullYear(),
  month: today.getMonth() + 1,
  day: today.getDate(),
});

const OnConfirm = async () => {
  try {
      const res = await useRecordWeight().Execute(recordWeight);
      if(!res) return alert('記録に失敗しました');
    } catch (e) {
      alert('記録に失敗しました');
    }
  dialog.value = false;
};

const UpdateBirthday = async () => {
    recordWeight.recordDate = new Date(Number(currentDate.year),Number(currentDate.month) - 1, Number(currentDate.day));
  };

function ResetForm() {
  currentDate.year = today.getFullYear();
  currentDate.month = today.getMonth() + 1;
  currentDate.day = today.getDate();
}

watch(dialog, (val) => {
  if (!val) {
    ResetForm();
  }
});
</script>
