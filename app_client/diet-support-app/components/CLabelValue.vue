<template>
  <div class="c-label-value">
    <div class="label-row">
      <v-icon :color="iconColor" :size="iconSize??18">{{ icon }}</v-icon>
      <span class="label">{{ label }}</span>
    </div>
    <div class="value" :class="valueClass">{{ value }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  icon: string,
  iconColor?: string,
  iconSize?: string | number,
  label: string,
  value: string | number,
  valueClass?: string,
}>()
</script>

<style scoped>
.label-row {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-bottom: 5px;
}
.label {
  font-size: 0.85rem;
  font-weight: 500;
  color: #555;
}
.value {
  font-size: 0.9rem;
  font-weight: bold;
}
</style>
