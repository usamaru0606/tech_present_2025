<template>
  <v-container class="fill-height d-flex align-center justify-center">
    <v-card class="pa-6" width="400">
      <v-card-title class="text-h6 text-center">新規登録</v-card-title>

      <v-card-text>
        <v-label class="label">名前</v-label>
        <v-text-field
          v-model="form.name"
          ref="emailField"
          type="email"
          density="compact"
          variant="outlined"
        />
        <v-label class="label">メールアドレス</v-label>
        <v-text-field
          v-model="form.email"
          ref="emailField"
          type="email"
          density="compact"
          variant="outlined"
        />
        <v-label class="label">パスワード(半角英数字)</v-label>
        <v-text-field
          v-model="form.password"
          ref="passwordField"
          :type="showPassword ? 'text' : 'password'"
          density="compact"
          variant="outlined"
          :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append-inner="SwitchPasswordVisibility"
        />
        <v-label class="label">パスワード確認</v-label>
        <v-text-field
          v-model="form.passwordConfirm"
          ref="passwordField"
          :type="showPassword ? 'text' : 'password'"
          density="compact"
          variant="outlined"
          hide-details
          :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append-inner="SwitchPasswordVisibility"
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
        <v-btn color="primary" @click="Register">登録</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { RegisterViewModel } from '~/viewmodel/register_vm'

definePageMeta({
  layout: 'blank',
})

const { form, error, Register } = RegisterViewModel()
const showPassword = ref(false);

function SwitchPasswordVisibility() {
  showPassword.value = !showPassword.value
}
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}

.fixed-height {
  min-height: 23px;
  font-size: 12px;
  font-weight: bold;
}

.invisible {
  visibility: hidden;
}

.textbtn{
    width: fit-content;
}
</style>
