<template>
  <v-container class="fill-height d-flex flex-column justify-center pb-10">
    <!-- 中央に表示されるタイトル -->
    <v-label class="text-h5 mb-4">ログイン</v-label>

    <!-- 中央に表示されるログインカード -->
    <v-card min-width="360">
      <v-card-text>
        <v-label class="label">メールアドレス</v-label>
        <v-text-field
          v-model="loginForm.email"
          ref="emailField"
          type="email"
          density="compact"
          variant="outlined"
          @keydown.enter="focusPassword"
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
        />
        <v-checkbox 
        v-model="showPassword"
        label="パスワードを表示する"
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
  </v-container>
</template>

<script setup lang="ts">
import { LoginViewModel } from "~/viewmodel/login_vm";

definePageMeta({
  layout: "blank",
});

const { loginForm, error, Login } = LoginViewModel();
const showPassword = ref(false);
const emailField = ref()
const passwordField = ref()

function focusPassword() {
  passwordField.value?.focus()
}
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}

.checkbox{
    font-size: 12px;
    margin-bottom: 10px;
}

.checkbox >>> .v-label{
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
</style>
