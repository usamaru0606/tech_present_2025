<template>
  <v-container fluid class="d-flex justify-center register-bg pt-0">
    <div class="container">
      <RegisterStepIndicator :currentStep="viewmodel.step.value" />

      <v-card v-if="viewmodel.step.value == 0" class="px-3 py-1" elevation="3">
        <v-card-title class="text-h6 text-center mb-2 fontblack"
          >新規登録
        </v-card-title>

        <v-card-text class="pb-0">
          <v-row>
            <v-col class="pb-0" dense>
              <CTextField
                v-model="viewmodel.userInfo.lastName"
                label="姓"
                type="text"
                inputRef="text"
              />
            </v-col>

            <v-col class="pb-0 pl-0" dense>
              <CTextField
                v-model="viewmodel.userInfo.firstName"
                label="名"
                type="text"
                inputRef="text"
              />
            </v-col>
          </v-row>

          <v-row class="align-center" dense>
            <v-col cols="auto" class="py-0">
              <CSelect
                v-model="viewmodel.userInfo.gender"
                :items="viewmodel.genderItems"
                label="性別"
                class="w-100 pr-1 gender_select"
              />
            </v-col>

            <v-col cols="auto" class="py-0 age_field">
              <CTextField
                v-model="viewmodel.userInfo.age"
                label="年齢"
                type="text"
                inputRef="text"
                textAlign="right"
                readonly
                class="input_age"
              />
            </v-col>

            <v-col class="mt-5">
              <p class="fontblack">歳</p>
            </v-col>
          </v-row>

          <CDateSelector
            label="生年月日"
            v-model:Year="viewmodel.birthdayItems.year"
            v-model:Month="viewmodel.birthdayItems.month"
            v-model:Day="viewmodel.birthdayItems.day"
            @vue:updated="viewmodel.UpdateBirthday"
            :minmode="true"
          />

          <CTextField
            v-model="viewmodel.userInfo.mailAddress"
            label="メールアドレス"
            type="email"
            inputRef="emailField"
          />

          <CPassField
            v-model="viewmodel.userInfo.password"
            inputRef="passwordField"
            label="パスワード（半角英数字）"
            :showAutoLoginCheckbox="false"
          />

          <CPassField
            v-model="viewmodel.passwordConfirm.value"
            inputRef="passwordField"
            label="パスワード確認"
            :showAutoLoginCheckbox="false"
          />

          <CAlert :message="viewmodel.error.value" />
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn class="cardbtn bg-primary" @click="viewmodel.NextStep">
            次へ
          </v-btn>
        </v-card-actions>
      </v-card>

      <v-card v-if="viewmodel.step.value == 1" class="py-1" elevation="3">
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

          <v-expansion-panels
            v-model="viewmodel.expandedIndex.value"
            class="px-2"
          >
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
                    v-model:Year="viewmodel.goalDate.year"
                    v-model:Month="viewmodel.goalDate.month"
                    v-model:Day="viewmodel.goalDate.day"
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
          <v-btn class="cardbtn bg-primary" @click="viewmodel.RegisterUserInfo">
            登録
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { RegisterViewModel } from "~/viewmodel/register_vm";

definePageMeta({
  layout: "blank",
});

const viewmodel = RegisterViewModel();
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

.age_field {
  min-width: 93px;
}

.gender_select {
  min-width: 112px;
}

.input_age ::v-deep(.v-input input) {
  background-color: #e0e0e0;
}

.cardbtn :deep(.v-btn__content) {
  font-size: 14px;
  font-weight: bold;
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
  min-height: 40px !important;
  transition: none;
}

.problem {
  max-width: 300px;
}
</style>
