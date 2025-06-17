<template>
  <v-app>
    <v-app-bar app color="primary" dark class="px-3">
      <v-app-bar-title>大サポくん</v-app-bar-title>
      <v-spacer />
      <v-btn icon>
        <v-icon @click="GoLoginPage">mdi-account</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid class="maincontainer">
        <slot />
      </v-container>
    </v-main>

    <v-footer app color="primary">
      <v-container class="text-center d-flex justify-center align-center">
        <!-- スマホ：アイコンのみ表示 -->
        <v-icon class="d-md-none d-inline-block mr-1">mdi-information</v-icon>

        <!-- タブレット以上：テキスト表示 -->
        <span class="d-none d-md-inline">© 2025 diet-support-app</span>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script setup lang="ts">
const router = useRouter();

async function GoLoginPage() {
  await router.push("/login");
}
</script>

<style scoped>
.maincontainer{
  min-height: 100%;
}
</style>
