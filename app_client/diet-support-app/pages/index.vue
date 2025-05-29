<template>
  <v-container max-width="600px" class="d-flex flex-column align-items-center">
    <p class="text-h5 mb-4 mx-auto">ユーザー情報</p>
    <v-card min-width="360" elevation="3" class="mb-4">
      <v-card-text>
        <v-list dense>
          <v-list-item>
            <v-list-item-title>名前 : {{ user.name }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>性別 : {{ user.gender }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>年齢 : {{ user.age }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>誕生日 : {{ user.birthday }}</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>メール : {{ user.email }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
    <v-btn min-width="200px" class="mx-auto" color="primary" @click="useFetchData">ユーザー情報を取得</v-btn>
  </v-container>
</template>

<script setup lang="ts">
import type { UserInfo } from "~/model/userinfo";

const error = ref<Error | null>(null);

const credentials = {
  email: "test@example.com",
  password: "test",
};

const user = reactive<UserInfo>({
  guid: "",
  name: "",
  gender: "",
  age: 0,
  birthday: "",
  email: "",
  password: "",
  passwordConfirm: "",
});

async function useFetchData() {
  const res = await useFetch<UserInfo>("http://127.0.0.1:8000/users/", {
    method: "POST",
    body: {
      email: credentials.email,
      password: credentials.password,
    },
  });

  error.value = res.error.value;

  if (error.value) {
    console.error("取得エラー:", error.value);
    alert("ユーザー情報の取得に失敗しました");
    return;
  }

  if (res.data.value) {
    Object.assign(user, res.data.value);
  }
}
</script>
