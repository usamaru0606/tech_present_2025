<template>
  <v-container class="fill-height d-flex flex-column justify-center pb-10">
    <div class="container">
      <v-card elevation="2" class="mb-4">
        <v-card-title class="text-h6 text-center">ログイン</v-card-title>
        <v-card-text>
          <CTextField
            v-model="viewmodel.loginInfo.mailaddress"
            label="メールアドレス"
            type="email"
            inputRef="emailField"
            :onEnter="viewmodel.Login"
          />

          <CPassField
            v-model="viewmodel.loginInfo.password"
            :onEnter="viewmodel.Login"
            inputRef="passwordField"
            label="パスワード（半角英数字）"
            :showAutoLoginCheckbox="true"
          />

          <CAlert :message="viewmodel.error.value" />
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn color="primary" @click="viewmodel.Login">ログイン</v-btn>
        </v-card-actions>
      </v-card>

      <div class="d-flex flex-column align-items-endmt-2">
        <CTextBtn label="パスワードを忘れた方はこちら" />

        <CTextBtn
          label="新規登録"
          color="primary"
          :onClick="viewmodel.GoRegisterPage"
        />
      </div>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { LoginViewModel } from "~/viewmodel/login_vm";

definePageMeta({
  layout: "blank",
});

const viewmodel = LoginViewModel();
</script>

<style scoped>
.container{
  width: 100%;
  max-width: 600px;
}
</style>