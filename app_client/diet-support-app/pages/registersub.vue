<template>
  <v-container fluid class="d-flex justify-center register-bg pt-0">
    <div class="container">
      <RegisterStepIndicator :currentStep="1" />

      <v-card class="py-1" elevation="3">
        <v-card-title class="text-h6 text-center mb-2 fontblack"
          >新規登録
        </v-card-title>

        <v-card-text class="pb-0 px-0">
          <v-col class="pb-2 pt-0 px-4">
            <SignInHeightSelector v-model="viewmodel.userInfo.height" />
          </v-col>

          <v-col class="pb-6 px-4">
            <SignInWeightSelector v-model="viewmodel.userInfo.weight" />
          </v-col>

          <v-expansion-panels v-model="viewmodel.expandedIndex.value" class="px-2">
            <v-expansion-panel elevation="0" class="border">
              <v-expansion-panel-title
                color="primary"
                class="py-2 font-weight-bold fixed-title"
              >
                目標/悩みを設定
              </v-expansion-panel-title>
              <v-expansion-panel-text>
                <!-- 目標日付 -->
                <div class="form-group">
                  <CDateSelector
                    label="目標期日"
                    v-model:Year="viewmodel.goaldate.year"
                    v-model:Month="viewmodel.goaldate.month"
                    v-model:Day="viewmodel.goaldate.day"
                    :feature="true"
                  />
                </div>

                <!-- 悩みの選択 -->
                <div class="form-group">
                  <CSelect
                    v-model="viewmodel.userInfo.selectedProblem"
                    :items="viewmodel.problemOptions"
                    label="悩み"
                    class="problem"
                  />
                </div>

                <div class="form-group">
                  <WeightSelector
                    v-model="viewmodel.userInfo.goalWeight"
                    label="目標体重"
                  />
                </div>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>

          <CAlert class="pt-3 px-4" :message="viewmodel.error.value" />
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn class="cardbtn bg-primary" @click="viewmodel.RegisterGoal">
            登録
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { RegisterSubViewModel } from "~/viewmodel/registersub_vm";

definePageMeta({
  layout: "blank",
});

const viewmodel = RegisterSubViewModel();
</script>

<style scoped>
.register-bg {
  height: 100%;
  background-color: #f4f6f8;
}

.container {
  width: 100%;
  max-width: 600px;
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

.form-group {
  margin-bottom: 8px;
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

::v-deep(.v-expansion-panel-text__wrapper) {
  padding: 8px 0px 8px 16px !important;
}

.border {
  border: 2px solid black;
  border-radius: 0px;
}

.fixed-title {
  min-height: 40px !important; /* デフォルトは 56px または 64px */
  transition: none; /* 不要なら高さ変化のアニメーションも無効化 */
}
</style>
