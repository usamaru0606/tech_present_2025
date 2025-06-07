<template>
  <div>
    <v-label v-if="label" class="label">{{ label }}</v-label>
    <v-select
      :items="items"
      :model-value="modelValue"
      @update:modelValue="emit('update:modelValue', $event)"
      density="compact"
      variant="outlined"
      :hide-details="hideDetails"
      :clearable="clearable"
      :multiple="multiple"
    />
  </div>
</template>

<script setup lang="ts">

const props = defineProps({
  modelValue: [String, Number],
  label: String,
  items: {
    type: Array,
    required: true
  },
  hideDetails: {
    type: Boolean,
    default: false
  },
  clearable: {
    type: Boolean,
    default: false
  },
  multiple: {
    type: Boolean,
    default: false
  },
});

const emit = defineEmits(['update:modelValue']);
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
  display: inline-block;
  margin-bottom: 0px;
}

:deep(.v-field__input){
  padding: 8px 4px 8px 12px;
}
</style>
