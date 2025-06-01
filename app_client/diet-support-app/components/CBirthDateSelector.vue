<template>
  <v-label class="label">生年月日</v-label>
  <v-row dense no-gutters>
    <v-col cols="auto">
      <CSelect
        :model-value="birthYear"
        :items="years"
        @update:model-value="$emit('update:birthYear', $event)"
        label="年"
        class="select-item-year"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        :model-value="birthMonth"
        :items="months"
        @update:model-value="$emit('update:birthMonth', $event)"
        label="月"
        class="select-item mx-3"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        :model-value="birthDay"
        :items="days"
        @update:model-value="$emit('update:birthDay', $event)"
        label="日"
        class="select-item"
      />
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
const props = defineProps({
  birthYear: [String, Number],
  birthMonth: [String, Number],
  birthDay: [String, Number],
  label: String,
});

const currentYear = new Date().getFullYear();
const years = Array.from({ length: 100 }, (_, i) => currentYear - i);
const months = Array.from({ length: 12 }, (_, i) => i + 1);
const days = Array.from({ length: 31 }, (_, i) => i + 1);

const emit = defineEmits([
  "update:birthYear",
  "update:birthMonth",
  "update:birthDay",
]);
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}
.select-item {
  width: 85px;
}
.select-item-year{
  width: 108px;
}
.container{
  width: 100%;
  max-width: 600px;
}
</style>
