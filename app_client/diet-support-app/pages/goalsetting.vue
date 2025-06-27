<template>
  <v-container
    fluid
    class="fill-height d-flex flex-column justify-center goal-bg"
  >
    <div class="container">
      <v-card elevation="2" class="pa-3 mb-10">
        <v-card-title class="text-h6 text-center mb-2 fontblack">
          目標設定
        </v-card-title>

        <v-card-text>
          <!-- 今日の日付 -->
          <div class="form-group">
            <p class="form-label">今日の日付</p>
            <p class="form-value">{{ goalsettingviewmodel.settingItem.startDate }}</p>
          </div>

          <!-- 目標日付 -->
          <div class="form-group">
            <CDateSelector
              label="目標期日"
              v-model:Year="goalsettingviewmodel.goaldate.year"
              v-model:Month="goalsettingviewmodel.goaldate.month"
              v-model:Day="goalsettingviewmodel.goaldate.day"
              :feature="true"
            />
          </div>

          <!-- 悩みの選択 -->
          <div class="form-group">
            <CSelect
              v-model="goalsettingviewmodel.settingItem.problem"
              :items="goalsettingviewmodel.problemOptions"
              label="悩み"
              :error="goalsettingviewmodel.problemError.value"
              :errorMessages="
                goalsettingviewmodel.problemError.value
                  ? '選択してください'
                  : ''
              "
              class="problem"
            />
          </div>

          <!-- 現在の体重 -->
          <div class="form-group">
            <p class="form-label">現在の体重</p>
            <p class="form-value">
              {{ goalsettingviewmodel.settingItem.weight }} kg
            </p>
          </div>

          <!-- 目標体重 -->
          <div class="form-group">
            <WeightSelector
              v-model="goalsettingviewmodel.settingItem.goalWeight"
              :currentWeight="goalsettingviewmodel.settingItem.weight"
              label="目標体重"
            />
          </div>
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn
          width="100"
            class="cardbtn bg-primary"
            @click="goalsettingviewmodel.OnConfirm"
          >
            登録
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { GoalSettingViewModel } from "~/viewmodel/goalsetting_vm";

definePageMeta({ layout: "blank" });

const goalsettingviewmodel = GoalSettingViewModel();
</script>

<style scoped>
.container {
  width: 100%;
  max-width: 600px;
}
.goal-bg {
  background-color: #f4f6f8;
}

.form-group {
  margin-bottom: 18px;
}

.form-label {
  font-weight: 600;
  font-size: 15px;
  color: #555;
  margin-bottom: 4px;
}

.form-value {
  font-weight: 700;
  color: #1a1a1a;
  margin-top: 2px;
}

.cardbtn :deep(.v-btn__content) {
  font-size: 14px;
  font-weight: bold;
}

.problem {
  max-width: 300px;
}

.fontblack {
  color: black;
}

@media (max-width: 600px) {
  .goal-card {
    padding: 32px 16px;
  }
  .goal-title {
    font-size: 20px;
  }
  .form-value {
    font-size: 18px;
  }
  .register-btn {
    min-width: 160px;
    font-size: 15px;
  }
}
</style>
