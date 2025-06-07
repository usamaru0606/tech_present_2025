<template>
  <v-dialog
    v-model="internalValue"
    max-width="500"
    height="400"
    persistent
  >
    <v-card>
      <v-card-title class="text-h6 bg-primary">{{ title }}</v-card-title>
      <v-card-text class="pa-4">
        <slot />
      </v-card-text>
      <v-card-actions style="border-top: 1px solid lightgray;">
        <v-spacer />
        <v-btn text @click="emitCancel">キャンセル</v-btn>
        <v-btn text color="primary" @click="emitConfirm">{{ emitBtnLabel }}</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  modelValue: boolean;
  title: string;
  emitBtnLabel:string;
}>();
const emit = defineEmits(['update:modelValue', 'confirm']);

const internalValue = computed({
  get: () => props.modelValue,
  set: (val: boolean) => emit('update:modelValue', val),
});

function emitCancel() {
  emit('update:modelValue', false);
}

function emitConfirm() {
  emit('confirm');
  emit('update:modelValue', false);
}
</script>
