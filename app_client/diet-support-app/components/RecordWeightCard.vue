<template>
  <v-card class="pa-2 fill-height scroll-y" elevation="2">
    <v-row>
      <v-col cols="6" class="pb-0">
        <strong>登録時体重</strong>
        <div>{{ initialWeight }} kg</div>
      </v-col>

      <v-col cols="6" class="pb-0">
        <strong>現在の体重</strong>
        <div>{{ currentWeight }} kg</div>
      </v-col>

      <v-col cols="6" class="pb-0">
        <strong>目標体重</strong>
        <div>{{ goalWeight }} kg</div>
      </v-col>
      
      <v-col cols="6" class="pb-0">
        <strong>先月との体重差</strong>
        <div
          :class="{
            'text-success': weightDiff < 0,
            'text-error': weightDiff > 0,
          }"
        >
          {{ weightDiff >= 0 ? "+" : "" }}{{ weightDiff }} kg
        </div>
      </v-col>

      <v-col cols="6" class="pb-0">
        <strong>期限</strong>
        <div>{{ goalDate }}</div>
      </v-col>

      <v-col cols="6">
        <strong>今日の日付</strong>
        <div>{{ today }}</div>
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup lang="ts">
const initialWeight = 70;
const currentWeight = 67.5;
const goalWeight = 65;
const goalDate = "2025/07/31";
const today = new Date().toLocaleDateString("ja-JP");

// 例: 先月が68.2kgだったとする
const lastMonthWeight = 68.2;
const weightDiff = +(currentWeight - lastMonthWeight).toFixed(1);
</script>

<style scoped>
.scroll-y{
    overflow-y: auto;
}
</style>