<template>
  <v-container
    fluid
    class="fill-height d-flex flex-column justify-center login-bg"
  >
    <div class="container">
      <v-card class="pa-3 mb-5" elevation="2">
        <v-card-title class="text-h6 text-center mb-2 fontblack">ログイン</v-card-title>
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
            v-model:autoLogin="viewmodel.autoLogin.value"
            :onEnter="viewmodel.Login"
            inputRef="passwordField"
            label="パスワード（半角英数字）"
            :showAutoLoginCheckbox="true"
          />

          <CAlert :message="viewmodel.error.value" />
        </v-card-text>

        <v-card-actions class="justify-end">
          <v-btn class="cardbtn bg-primary" @click="viewmodel.Login">
            ログイン
          </v-btn>
        </v-card-actions>
      </v-card>

      <div class="d-flex flex-column">
        <CTextBtn label="パスワードを忘れた方はこちら" />

        <CTextBtn
          label="新規登録"
          color="primary"
          :onClick="viewmodel.GoToRegisterPage"
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
.login-bg {
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
.fontblack {
  color: black;
}
</style>
