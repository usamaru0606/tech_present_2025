<template>
  <v-btn
    :density="density"
    :variant="variant"
    :color="color"
    class="text-caption mt-1 textbtn"
    @click="onClick"
  >
    {{ label }}
  </v-btn>
</template>

<script setup>
const props = defineProps({
  label: String,
  color: {
    type: String,
    default: undefined, // Vuetifyのデフォルトカラー
  },
  density: {
    type: String,
    default: "compact",
  },
  variant: {
    type: String,
    default: "text",
  },
  onClick: {
    type: Function,
    default: () => {}, // 未指定でもエラーにならないように
  },
});
</script>

<style scoped>
.textbtn {
  width: fit-content;
}
</style>
