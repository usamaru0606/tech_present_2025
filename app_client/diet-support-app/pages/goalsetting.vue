<template>
  <v-container fluid class="py-12 goal-container">
    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-card class="goal-card">
          <v-card-title class="goal-title"> 目標設定 </v-card-title>

          <!-- 今日の日付 -->
          <div class="form-group">
            <p class="form-label">今日の日付</p>
            <p class="form-value">{{ goalsettingviewmodel.today }}</p>
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
              v-model="goalsettingviewmodel.settingItem.selectedProblem"
              :items="goalsettingviewmodel.problemOptions"
              label="悩み"
              :error="goalsettingviewmodel.problemError.value"
              :errorMessages="goalsettingviewmodel.problemError.value ? '選択してください' : ''"
              class="problem"
            />
          </div>

          <!-- 現在の体重 -->
          <div class="form-group">
            <p class="form-label">現在の体重</p>
            <p class="form-value">
              {{ goalsettingviewmodel.currentWeight.value }} kg
            </p>
          </div>

          <!-- 目標体重 -->
          <div class="form-group">
            <WeightSelector
              v-model="goalsettingviewmodel.settingItem.goalWeight"
              :currentWeight="goalsettingviewmodel.currentWeight.value"
              label="目標体重"
            />
          </div>

          <v-card-actions class="action-wrap">
            <v-btn
              color="white"
              size="large"
              rounded
              elevation="2"
              class="register-btn bg-primary"
              @click="goalsettingviewmodel.OnConfirm"
            >
              登録
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { GoalSettingViewModel } from "~/viewmodel/goalsetting_vm";

definePageMeta({ layout: "blank" });

const goalsettingviewmodel = GoalSettingViewModel();
</script>

<style scoped>
.goal-container {
  background-color: #f4f6f8;
  min-height: 100%;
}

.goal-card {
  padding: 24px 32px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.goal-title {
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 32px;
  color: #222;
}

.form-group {
  margin-bottom: 26px;
}

.form-label {
  font-weight: 600;
  font-size: 15px;
  color: #555;
  margin-bottom: 4px;
}

.form-value {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a1a;
  margin-top: 2px;
}

.action-wrap {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}

.register-btn {
  padding: 0 40px;
  font-size: 16px;
  font-weight: 700;
  text-transform: none;
  min-width: 200px;
}
.problem {
  max-width: 300px;
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
