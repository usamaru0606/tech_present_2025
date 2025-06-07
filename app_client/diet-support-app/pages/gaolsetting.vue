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
    <!-- 今日の日付 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-0">
        <strong>今日の日付</strong>
        <div>{{ today }}</div>
      </v-col>
    </v-row>

    <!-- 目標日付 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <CDateSelector
          label="目標期日"
          v-model:Year="birthdayItems.year"
          v-model:Month="birthdayItems.month"
          v-model:Day="birthdayItems.day"
          :feature="true"
          :minmode="true"
        />
      </v-col>
    </v-row>

    <!-- 現在の体重 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-0">
        <strong>現在の体重</strong>
        <div>{{ currentWeight }} kg</div>
      </v-col>
    </v-row>

    <!-- 目標体重 -->
    <v-row dense class="ma-0">
      <v-col cols="12" class="py-2">
        <WeightSelector
          v-model="goalWeight"
          :currentWeight="64"
          label="目標体重"
        />
      </v-col>
    </v-row>
  </CDialog>
</template>

<script setup lang="ts">
import { ref, computed, reactive, onMounted } from "vue";

const dialog = ref(false);
const today = computed(() => new Date().toLocaleDateString());
const currentWeight = ref(64);
const goalWeight = ref(64);
const birthdayItems = reactive({
  year: "",
  month: "",
  day: "",
});

onMounted(() => {
  birthdayItems.year = "";
  birthdayItems.month = "";
  birthdayItems.day = "";
});

const OnConfirm = () => {
  console.log("記録を実行しました");
  dialog.value = false;
};
</script>
