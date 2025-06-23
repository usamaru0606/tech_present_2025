<template>
  <CIconBtn
    label="体重を記録"
    icon="mdi-pencil"
    :isTextPrimary="true"
    :onClick="Open"
  />

  <CDialog
    v-model="dialog"
    :width="450"
    :height="400"
    title="体重を記録する"
    emitBtnLabel="記録する"
    @confirm="OnConfirm"
  >
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録日</strong>
        <CDateSelector
          v-model:Year="currentDate.year"
          v-model:Month="currentDate.month"
          v-model:Day="currentDate.day"
          @vue:updated="UpdateBirthday"
          :minmode="true"
        />
      </v-col>
    </v-row>

    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <strong>記録体重</strong>
        <WeightSelector v-model="recordWeight.currentWeight" />
      </v-col>
    </v-row>
  </CDialog>
</template>

<script setup lang="ts">
const userIdStore = useUserIdStore();
const userWeightStore = useUserWeightStore();
const router = useRouter();
const dialog = ref(false);
const recordWeight = reactive({
  userId: userIdStore.getUserId()?.guid ?? userIdStore.getUserId() ?? "",
  currentWeight: userWeightStore.getUserWeight() ?? 64,
  recordDate: new Date(),
});
const today = new Date();
const currentDate = reactive({
  year: today.getFullYear(),
  month: today.getMonth() + 1,
  day: today.getDate(),
});

const OnConfirm = async () => {
  console.log("[調査] OnConfirm called", JSON.stringify(recordWeight));
  try {
    if (userIdStore.userId == "test") {
      userWeightStore.setUserWeight(recordWeight.currentWeight);
      dialog.value = false;
      console.log("[調査] test user, set weight and close dialog");
      return;
    }
    console.log("[調査] before Execute", JSON.stringify(recordWeight));
    const res = await useRecordWeight().Execute(recordWeight);
    console.log("[調査] after Execute", res);
    if (!res) return alert("記録に失敗しました");
    userWeightStore.setUserWeight(recordWeight.currentWeight);
  } catch (e) {
    console.log("[調査] catch error", e);
    alert("記録に失敗しました");
  }
  console.log("[調査] dialog.value = false");
  dialog.value = false;
};

const Open = async () => {
  if (!recordWeight.userId) return;
  dialog.value = true;
};

const UpdateBirthday = async () => {
  recordWeight.recordDate = new Date(
    Number(currentDate.year),
    Number(currentDate.month) - 1,
    Number(currentDate.day)
  );
};

function ResetForm() {
  currentDate.year = today.getFullYear();
  currentDate.month = today.getMonth() + 1;
  currentDate.day = today.getDate();
}

watch(dialog, (val) => {
  if (val) {
    ResetForm();
  }
});
</script>
