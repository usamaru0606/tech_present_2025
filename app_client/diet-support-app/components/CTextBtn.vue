<template>
  <v-btn
    :density="density"
    :variant="variant"
    :color="color"
    class="text-caption mt-1 textbtn"
    :text="label"
    @click="onClick"
  />
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
.textbtn{
  width: fit-content;
}
.textbtn :deep(.v-btn__content){
  font-size: 14px;
}
</style>
