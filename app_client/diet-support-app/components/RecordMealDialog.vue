<template>
  <CDialog
    v-model="internalValue"
    title="食事を記録"
    emitBtnLabel="保存"
    :width="800"
    :height="500"
    @confirm="emitConfirm"
  >
    <v-container fluid class="pa-0 d-flex flex-column container">
      <v-row class="px-4 pt-2" align="center">
        <v-icon color="primary" size="32">mdi-silverware-fork-knife</v-icon>
        <p class="title ml-3 mb-0">{{ timing }}</p>
      </v-row>

      <v-row dense class="px-4 pt-4 flex-grow-1 scroll-y">
        <v-col
          cols="12"
          sm="6"
          v-for="item in mealCategories"
          :key="item.key"
          class="pb-4"
        >
          <CTextField
            class="px-2"
            :icon="item.icon"
            icon-color="orange"
            v-model="tempMeal[item.key]"
            :label="item.label"
            inputRef="mealField"
          />
        </v-col>

        <v-col cols="12" sm="6" class="pb-4">
          <div class="d-flex justify-end align-end">
            <CTextField
              class="w-50 pl-2"
              :icon="'mdi-fire'"
              icon-color="deep-orange"
              v-model.number="tempMeal.totalCalories"
              label="合計カロリー"
              type="number"
              inputRef="calorieField"
              :hideDetails="true"
            />
            <p class="mb-0 px-2 align-self-end">kcal</p>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </CDialog>
</template>

<script setup lang="ts">
import type { Meal, MealCategoryKey } from "~/model/meal";

const props = defineProps<{
  modelValue: boolean;
  modelMeal: Meal;
  timing: string;
}>();

const emit = defineEmits<{
  (e: "update:modelValue", val: boolean): void;
}>();

const internalValue = computed({
  get: () => props.modelValue,
  set: (val: boolean) => emit("update:modelValue", val),
});

const tempMeal = reactive<Meal>({
  stapleFood: null,
  mainDish: null,
  sideDish: null,
  soup: null,
  other: null,
  totalCalories: null,
});

const mealCategories: {
  key: MealCategoryKey;
  label: string;
  icon: string;
}[] = [
  { key: "stapleFood", label: "主食", icon: "mdi-rice" },
  { key: "mainDish", label: "主菜", icon: "mdi-silverware-fork-knife" },
  { key: "sideDish", label: "副菜", icon: "mdi-leaf" },
  { key: "soup", label: "汁物", icon: "mdi-bowl" },
  { key: "other", label: "その他", icon: "mdi-dots-horizontal" },
];

watch(
  () => props.modelValue,
  (opened) => {
    if (opened) {
      Object.assign(tempMeal, props.modelMeal);
    }
  },
  { immediate: true }
);

const emitConfirm = async () => {
  try {
    const userId = useUserIdStore().getUserId()!;
    const res = await useRecordMeal().Execute(userId,tempMeal,props.timing);
    if(!res) alert('記録できませんでした');
  } catch {
    alert('記録できませんでした');
  } finally {
    emit("update:modelValue", false);
  }
};
</script>

<style scoped>
.container {
  height: 100%;
}

.scroll-y {
  overflow-y: auto;
}
.title {
  font-weight: 600;
  font-size: 1.5rem;
}

.v-row[style*="overflow-y: auto"]::-webkit-scrollbar {
  width: 8px;
}
.v-row[style*="overflow-y: auto"]::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}
</style>
