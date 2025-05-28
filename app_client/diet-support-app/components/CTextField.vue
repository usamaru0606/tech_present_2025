<template>
  <div>
    <v-label class="label">{{ label }}</v-label>
    <v-text-field
      :ref="inputRef"
      :model-value="modelValue"
      :type="type"
      :density="density"
      :variant="variant"
      :hide-details="hideDetails"
      @keydown.enter="handleEnter"
      @update:model-value="$emit('update:modelValue', $event)"
    />
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: String,
  label: String,
  type: {
    type: String,
    default: 'text'
  },
  inputRef: String,
  density: {
    type: String,
    default: 'compact'
  },
  variant: {
    type: String,
    default: 'outlined'
  },
  hideDetails: {
    type: Boolean,
    default: false
  },
  onEnter :{
    type: Function,
    default: () => {}, // 未指定でもエラーにならないように
  },
})

const emit = defineEmits(['update:modelValue'])

const handleEnter = () => {
  if (props.onEnter) props.onEnter()
}
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}
</style>
