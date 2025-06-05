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

  <v-dialog v-model="dialog" max-width="400" min-width="360">
    <v-card>
      <v-card-title class="bg-primary text-h6 font-weight-medium mb-4 py-1">確認</v-card-title>
      <v-card-text class="py-1" style="font-size: 14px;">ホーム画面に移動します。</v-card-text>
      <v-card-text class="py-1" style="font-size: 14px;">入力内容が破棄されますがよろしいですか？</v-card-text>
      <v-card-actions class="mt-4">
        <v-spacer />
        <v-btn color="grey-dark" text @click="OnCancel">キャンセル</v-btn>
        <v-btn color="primary" text @click="OnConfirm">OK</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

</template>

<script setup lang="ts">
const router = useRouter();
const dialog = ref(false);

function GoHomePage() {
  dialog.value = true;
};

const OnConfirm = () => {
  dialog.value = false;
  router.push("/");
};

const OnCancel = () => {
  dialog.value = false;
};
</script>