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
      <v-container fluid class="maincontainer flex-grow-1">
        <slot />
      </v-container>
    </v-main>

    <v-footer app color="primary">
      <v-container class="text-center justify-center align-center">
        <v-container class="d-md-none d-flex pa-0">
          <!-- スマホ：アイコンのみ表示 -->
          <v-spacer />
          <v-icon @click="OnHomeIconClick" style="cursor: pointer">
            mdi-home
          </v-icon>
          <v-spacer />
          <v-icon @click="OnFoodIconClick" style="cursor: pointer">
            mdi-food
          </v-icon>
          <v-spacer />
           <v-icon @click="OnDumbbellIconClick" style="cursor: pointer">
            mdi-dumbbell
          </v-icon>
          <v-spacer />
        </v-container>
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

const OnFoodIconClick = async () => {
  await router.push("/meal");
};

const OnHomeIconClick = async () => {
  await router.push("/");
};

const OnDumbbellIconClick =async() =>{
   await router.push("/training");
}
</script>

<style scoped>
.maincontainer {
  min-height: 100%;
}
</style>
