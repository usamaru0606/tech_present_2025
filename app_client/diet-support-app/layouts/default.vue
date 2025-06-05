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
      <v-container fluid class="fill-height pa-4">
        <slot />
      </v-container>
    </v-main>

    <v-footer app color="primary">
      <v-container class="text-center">© 2025 diet-support-app</v-container>
    </v-footer>
  </v-app>
</template>

<script setup lang="ts">
const router = useRouter();

function GoLoginPage() {
  router.push("/login");
}
</script>