<template>
  <v-app>
    <v-app-bar app color="primary" dark class="px-3">
      <v-app-bar-title>大サポくん</v-app-bar-title>
      <v-btn icon>
        <v-icon @click="GoHomePage">mdi-home</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <slot />
    </v-main>
  </v-app>

  <CDialog
    v-model="dialog"
    title="確認"
    :width="400"
    :height="250"
    emitBtnLabel="OK"
    @confirm="OnConfirm"
  >
      <p class="fontsize mb-2">
        ホーム画面に移動します。
      </p>
      <p class="fontsize">入力内容が破棄されますがよろしいですか？</p>
  </CDialog>

  <v-footer app color="primary">
    <v-container class="text-center d-flex justify-center align-center">
      <!-- スマホ：アイコンのみ表示 -->
      <v-icon class="d-md-none d-inline-block mr-1">mdi-information</v-icon>

      <!-- タブレット以上：テキスト表示 -->
      <span class="d-none d-md-inline">© 2025 diet-support-app</span>
    </v-container>
  </v-footer>
</template>

<script setup lang="ts">
const router = useRouter();
const dialog = ref(false);

async function GoHomePage() {
  dialog.value = true;
}

const OnConfirm = async() => {
  dialog.value = false;
  await router.push("/");
};
</script>

<style scoped>
.fontsize{
  font-size: 16px;
}
</style>
