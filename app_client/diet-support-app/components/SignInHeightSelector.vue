<template>
  <div>
    <p class="label">{{ label }}</p>
    <div class="d-flex align-center  gap-2">
      <CSelect
        id="heighttinteger"
        :width="100"
        :items="integerOptions"
        v-model="selectedInteger"
        :hide-details="true"
      />
      <span>.</span>
      <CSelect
        id="heightdecimal"
        :width="80"
        :items="decimalOptions"
        v-model="selectedDecimal"
        :hide-details="true"
      />
      <span>cm</span>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  modelValue: {
    type: Number,
    default: 160,
  },
  label: {
    type: String,
    default: "身長",
  },
});

const emit = defineEmits(["update:modelValue"]);

// 整数部：currentHeight
const integerOptions = computed(() => {
  return Array.from({ length:  100}, (_, i) => 100 + i);
});

// 小数部：0〜9（0.0〜0.9）
const decimalOptions = Array.from({ length: 10 }, (_, i) => i);

// 選択中の整数・小数部
const selectedInteger = ref(Math.floor(props.modelValue));
const selectedDecimal = ref(Math.round((props.modelValue % 1) * 10));

// props.modelValueが変わったら反映
watch(
  () => props.modelValue,
  (val) => {
    selectedInteger.value = Math.floor(val);
    selectedDecimal.value = Math.round((val % 1) * 10);
  },
  { immediate: true }
);

// 値が変わったらemit
watch([selectedInteger, selectedDecimal], ([intPart, decPart]) => {
  const value = Math.round((intPart + decPart / 10) * 10) / 10;
  emit("update:modelValue", value);
});
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 5px;
}
.gap-2 {
  gap: 8px;
}
</style>
