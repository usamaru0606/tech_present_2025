<template>
  <div>
    <label v-if="label" class="label" :for="id">{{ label }}</label>
    <v-select
      :id="id"
      :items="items"
      :model-value="modelValue"
      @update:model-value="emit('update:modelValue', $event)"
      density="compact"
      variant="outlined"
      :hide-details="hideDetails"
      :clearable="clearable"
      :multiple="multiple"
      :error="error"
      :error-messages="errorMessages"
    />
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  modelValue: [String, Number],
  label: String,
  items: {
    type: Array,
    required: true,
  },
  hideDetails: {
    type: Boolean,
    default: false,
  },
  clearable: {
    type: Boolean,
    default: false,
  },
  multiple: {
    type: Boolean,
    default: false,
  },
  id: {
    type: String,
    default: "select",
  },
  error: {
    type: Boolean,
    default: false,
  },
  errorMessages: {
    type: [String, Array],
    default: "",
  },
});

const emit = defineEmits(["update:modelValue"]);
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
  display: inline-block;
  margin-bottom: 0px;
}

:deep(.v-field__input) {
  padding: 8px 4px 8px 12px;
}
</style>
