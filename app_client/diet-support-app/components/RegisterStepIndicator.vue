<!-- components/StepIndicator.vue -->
<template>
  <div class="step-indicator d-flex justify-center py-4">
    <div
      v-for="(stepLabel, index) in steps"
      :key="index"
      class="step-box"
      :class="{ active: currentStep === index }"
    >
      <v-icon class="mr-2" size="18">{{ icons[index] }}</v-icon>
      {{ stepLabel }}
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  currentStep: number;
}>();

const steps = ["基本情報", "身長・体重"];
const icons = ["mdi-account", "mdi-human-male-height"];
</script>

<style scoped>
.step-indicator {
  gap: 12px;
  flex-wrap: wrap;
}

.step-box {
  background-color: #e0e0e0;
  color: #444;
  padding: 10px 32px 10px 16px;
  font-weight: bold;
  font-size: 14px;
  clip-path: polygon(
    0 0,
    calc(100% - 12px) 0,
    100% 50%,
    calc(100% - 12px) 100%,
    0 100%
  );
  display: flex;
  align-items: center;
  height: 40px;
  box-sizing: border-box;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.step-box.active {
  background-color: #1976d2;
  color: white;
}
</style>
