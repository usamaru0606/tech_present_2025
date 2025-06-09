<template>
  <v-container class="fill-height d-flex align-center justify-center">
    <div class="container">
      <v-card class="pa-3" elevation="2">
        <v-card-title class="text-h6 text-center mb-2">目標設定</v-card-title>

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
     </v-card>
    </div>
  </v-container>
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
