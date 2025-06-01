<template>
  <div>
    <v-label class="label">{{ label }}</v-label>
    <v-text-field
      :ref="inputRef"
      :model-value="modelValue"
      :type="showPassword ? 'text' : 'password'"
      density='compact'
      variant='outlined'
      :hide-details="hideDetails"
      :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
      @click:append-inner="togglePasswordVisibility"
      @keydown.enter="handleEnter"
      @update:model-value="$emit('update:modelValue', $event)"
    />

    <v-checkbox
      v-if="showAutoLoginCheckbox"
      v-model="autoLogin"
      :label="checkboxLabel"
      class="checkbox"
      density='compact'
      :hide-details="hideDetails"
    />
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  modelValue: String,
  autoLogin:Boolean,
  label: String,
  inputRef: String,
  hideDetails: {
    type: Boolean,
    default: false
  },
  showAutoLoginCheckbox: {
    type: Boolean,
    default: false
  },
  checkboxLabel: {
    type: String,
    default: '次回から自動でログインする'
  },
  onEnter :{
    type: Function,
    default: () => {}, // 未指定でもエラーにならないように
  },
})

const emit = defineEmits(['update:modelValue', 'update:autoLogin'])

const showPassword = ref(false)
const autoLogin = computed({
  get: () => props.autoLogin,
  set: (val: Boolean) => emit('update:autoLogin', val)
});

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

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

.checkbox {
  font-size: 12px;
  margin: 0px;
}

.checkbox :deep(.v-label) {
  font-size: 12px;
}
</style>

