<template>
  <v-app>
    <v-app-bar app color="primary" dark class="px-3">
      <v-app-bar-title>大サポくん</v-app-bar-title>
      <v-spacer />
      <v-btn icon>
        <v-icon @click="GoLoginPage">mdi-account</v-icon>
      </v-btn>
      <v-btn icon @click="drawer = !drawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>

    <ClientOnly>
      <v-navigation-drawer v-model="drawer" app temporary location="end">
        <v-list>
          <v-list-item title="Home" />
          <v-list-item title="Settings" />
        </v-list>
      </v-navigation-drawer>
    </ClientOnly>

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
const drawer = ref(false);
const router = useRouter();

function GoLoginPage() {
  router.push("/login");
}
</script>