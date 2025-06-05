<template>
  <v-container fluid class="pa-0 fill-height">
    <v-row class="fill-height">
      <v-col cols="12" md="7" class="pa-0 d-flex flex-column fill-height">
        <div class="pa-2 left-top-container">
          <CChart
            :chartData="viewmodel.chartData.value"
            :userId="viewmodel.userId.value"
          />
        </div>

        <div class="pa-2 left-bottom-container">
          <v-row class="button-row" no-gutters>
            <v-col cols="auto" class="d-flex align-self-center">
              <CIconBtn
                icon="mdi-refresh"
                :isTextPrimary="true"
                :onClick="viewmodel.Reload"
              />
            </v-col>

            <v-col cols="auto" class="d-flex d-inline-flex align-self-center">
              <CIconBtn
                label="体重を記録"
                icon="mdi-pencil"
                :isTextPrimary="true"
                :onClick="viewmodel.GoRecordWeight"
              />
            </v-col>

            <v-col cols="auto" class="d-flex align-self-center">
              <CIconBtn
                label=" 悩み・目標を設定"
                icon="mdi-open-in-new"
                :iconRight="true"
                :onClick="viewmodel.GoGoalSetting"
              />
            </v-col>
          </v-row>

          <v-card class="pa-0" elevation="2">
            <v-row dense>
              <v-col cols="6">
                <strong>登録時体重</strong>
                <div>{{ initialWeight }} kg</div>
              </v-col>

              <v-col cols="6">
                <strong>現在の体重</strong>
                <div>{{ currentWeight }} kg</div>
              </v-col>

              <v-col cols="6">
                <strong>目標体重</strong>
                <div>{{ goalWeight }} kg</div>
              </v-col>

              <v-col cols="6">
                <strong>期限</strong>
                <div>{{ goalDate }}</div>
              </v-col>

              <v-col cols="6">
                <strong>今日の日付</strong>
                <div>{{ today }}</div>
              </v-col>

              <v-col cols="6">
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
            </v-row>
          </v-card>
        </div>
      </v-col>

      <v-col
        cols="12"
        md="5"
        class="d-none d-md-flex flex-column align-center justify-space-between right-side-container pa-10"
      >
        <v-btn
          class="relaodBtn w-auto"
          @click="viewmodel.Reload"
          text="トレーニングメニュー"
        />
        <v-btn
          class="relaodBtn w-auto"
          @click="viewmodel.Reload"
          text="食事メニュー"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { IndexViewModel } from "~/viewmodel/index_vm";

const viewmodel = IndexViewModel();
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
.left-top-container {
  min-height: 0;
  display: flex;
  flex-direction: column;
  flex: 6.5;
}

.left-bottom-container {
  border: 1px #e8f5f0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  flex: 3.5;
}

.right-side-container {
  background-color: #fff3e0;
  border: 1px solid #ffcc80;
}

.button-row {
  gap: 10px;
  margin: 0px;
  padding: 0px;
}
</style>
