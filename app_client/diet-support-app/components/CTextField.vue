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
      :readonly="readonly"
      :style="inputStyle"
      @keydown.enter="handleEnter"
      @update:model-value="$emit('update:modelValue', $event)"
    />
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: String | Number,
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
  textAlign: {
    type: String,
    default: 'left'
  },
  hideDetails: {
    type: Boolean,
    default: false
  },
  readonly: {
    type:Boolean,
    default:false
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

const inputStyle = computed(() => ({
  '--v-input-input-text-align': props.textAlign,
}));
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 5px;
}

::v-deep(input) {
  text-align: var(--v-input-input-text-align);
}
</style>
