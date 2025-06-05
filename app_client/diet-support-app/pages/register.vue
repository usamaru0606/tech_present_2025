<template>
  <v-container class="fill-height d-flex align-center justify-center">
    <div class="container">
      <v-card class="pa-3" elevation="2">
        <v-card-title class="text-h6 text-center mb-2">新規登録</v-card-title>

        <v-card-text>
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
            <v-col class="mt-5"><label>歳</label></v-col>
          </v-row>

          <CBirthDateSelector
            v-model:birthYear="viewmodel.birthdayItems.year"
            v-model:birthMonth="viewmodel.birthdayItems.month"
            v-model:birthDay="viewmodel.birthdayItems.day"
            @vue:updated="viewmodel.UpdateBirthday"
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
          <v-btn class="cardbtn bg-primary" @click="viewmodel.Register">登録</v-btn>
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
.container{
  width: 100%;
  max-width: 600px;
}
.age_field
{
  min-width:93px
}
.gender_select
{
  min-width:112px
}
.input_age ::v-deep(.v-input input) {
  background-color: #eeeeee;
}
.cardbtn :deep(.v-btn__content){
  font-size: 14px;
  font-weight: bold;
}
</style>