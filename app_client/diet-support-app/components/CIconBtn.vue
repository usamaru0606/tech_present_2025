<template>
  <v-btn
    density="compact"
    :class="['left_bottom_Btn', { 'text-primary': isTextPrimary }]"
    @click="onClick"
  >
    <!-- アイコンだけの中央表示 -->
    <template v-if="icon && !label">
      <v-icon :size="18">{{ icon }}</v-icon>
    </template>

    <!-- 左アイコン + テキスト -->
    <template v-if="icon && label && !iconRight">
      <v-icon :size="18" class="mr-1">{{ icon }}</v-icon>
    </template>

    <span v-if="label">{{ label }}</span>

    <template v-if="icon && label && iconRight">
      <v-icon :size="18" class="ml-1">{{ icon }}</v-icon>
    </template>
  </v-btn>
</template>

<script setup lang="ts">
const props = defineProps<{
  label?: string;
  icon?: string;
  iconRight?: boolean;
  isTextPrimary?: boolean;
  onClick: () => void;
}>();
</script>

<style scoped>
.left_bottom_Btn {
  width: fit-content;
  padding: 6px;
  height: 30px;
}
</style>
