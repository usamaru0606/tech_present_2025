<template>
  <v-container class="fill-height d-flex align-center justify-center">
    <v-container max-width="600px">
      <v-card class="pa-6" min-width="360">
        <v-card-title class="text-h6 text-center">新規登録</v-card-title>

        <v-card-text>
          <CTextField
            v-model="viewmodel.userInfo.name"
            label="名前"
            type="text"
            inputRef="emailField"
          />

          <CTextField
            v-model="viewmodel.userInfo.email"
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
            v-model="viewmodel.userInfo.passwordConfirm"
            inputRef="passwordField"
            label="パスワード確認"
            :showAutoLoginCheckbox="false"
          />

          <CAlert :message="viewmodel.error.value" />
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn color="primary" @click="viewmodel.Register">登録</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-container>
</template>

<script setup lang="ts">
import { RegisterViewModel } from "~/viewmodel/register_vm";

definePageMeta({
  layout: "blank",
});

const viewmodel = RegisterViewModel();
</script>
