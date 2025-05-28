<template>
  <v-container class="fill-height d-flex flex-column justify-center pb-10">
    <v-label class="text-h5 mb-4">ログイン</v-label>

    <v-container class="container">
      <v-card min-width="360">
        <v-card-text>
          <v-label class="label">メールアドレス</v-label>
          <v-text-field
            v-model="loginForm.email"
            ref="emailField"
            type="email"
            density="compact"
            variant="outlined"
            @keydown.enter="FocusPassword"
          />

          <v-label class="label">パスワード(半角英数字)</v-label>
          <v-text-field
            v-model="loginForm.password"
            ref="passwordField"
            :type="showPassword ? 'text' : 'password'"
            density="compact"
            variant="outlined"
            hide-details
            @keydown.enter="Login"
            :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append-inner="SwitchPasswordVisibility"
          />
          <v-checkbox
            label="次回から自動でログインする"
            class="checkbox"
            density="compact"
            hide-details
          />

          <v-alert
            :class="{ invisible: !error }"
            aaa
            type="error"
            variant="text"
            class="ma-0 pa-0 fixed-height"
            density="compact"
            :icon="false"
          >
            {{ error }}

            <template #prepend v-if="error">
              <v-icon size="22" color="error">mdi-alert-circle</v-icon>
            </template>
          </v-alert>
        </v-card-text>

        <v-card-actions class="justify-end mb-1">
          <v-btn color="primary" @click="Login">ログイン</v-btn>
        </v-card-actions>
      </v-card>

      <div class="d-flex flex-column align-items-endmt-2">
        <v-btn
          density="compact"
          variant="text"
          class="text-caption mb-1 mt-1 textbtn"
        >
          パスワードを忘れた方はこちら
        </v-btn>
        <v-btn
          density="compact"
          color="primary"
          variant="text"
          class="text-caption textbtn"
          @click="GoRegisterPage"
        >
          新規登録
        </v-btn>
      </div>
    </v-container>
  </v-container>
</template>

<script setup lang="ts">
import { LoginViewModel } from "~/viewmodel/login_vm";

definePageMeta({
  layout: "blank",
});

const { loginForm, error, Login, GoRegisterPage } = LoginViewModel();
const showPassword = ref(false);
const emailField = ref();
const passwordField = ref();

function FocusPassword() {
  passwordField.value?.focus();
}

function SwitchPasswordVisibility() {
  showPassword.value = !showPassword.value;
}
</script>

<style scoped>
.container{
    max-width: 600px;
}
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}

.checkbox {
  font-size: 12px;
  margin-bottom: 10px;
}

.checkbox :deep(.v-label) {
  font-size: 12px;
}

.fixed-height {
  min-height: 23px;
  font-size: 12px;
  font-weight: bold;
}

.invisible {
  visibility: hidden;
}

.textbtn {
  width: fit-content;
}
</style>
