<template>
  <v-card class="px-4 pt-2 fill-height custom-card" elevation="4" rounded="lg">
    <v-card-title class="text-h6 font-weight-bold pb-0">
      今日のごはん
    </v-card-title>

    <client-only>
      <v-tabs v-model="viewmodel.selectedMeal.value" grow class="mt-1">
        <v-tab
          v-for="tab in viewmodel.mealTabs"
          :key="tab.key"
          :value="tab.key"
        >
          {{ tab.label }}
        </v-tab>
      </v-tabs>
    </client-only>

    <v-divider class="mb-4" />

    <v-row dense class="ml-1">
      <v-col
        cols="4"
        v-for="item in viewmodel.mealCategories"
        :key="item.key"
        class="my-3"
      >
        <CLabelValue
          :icon="item.icon"
          icon-color="orange"
          :label="item.label"
          :value="
            viewmodel.menuItem[viewmodel.selectedMeal.value].value[item.key] ||
            '--'
          "
        />
      </v-col>

      <v-col cols="4" class="my-2">
        <CLabelValue
          icon="mdi-fire"
          icon-color="deep-orange"
          label="合計カロリー"
          :value="`${
            viewmodel.menuItem[viewmodel.selectedMeal.value].value
              .totalCalories || '--'
          } kcal`"
        />
      </v-col>
    </v-row>

    <v-divider class="my-3" />

    <v-row>
      <v-col cols="7">
        <CIconBtn
          class="ml-3 py-0 px-4 custom-btn"
          label="食事を記録"
          icon="mdi-pencil"
          :onClick="viewmodel.OpenRecordMealDialog"
        />
        <RecordMealDialog
          :timing="
            viewmodel.mealTabs.find(
              (tab) => tab.key === viewmodel.selectedMeal.value
            )?.label ?? ''
          "
          v-model="viewmodel.isOpenRecordMealDialog.value"
          :modelMeal="viewmodel.menuItem[viewmodel.selectedMeal.value].value"
          @confirm="viewmodel.RecordMeal"
        />
      </v-col>
      <v-col cols="5">
        <CTextBtn
          class="text-btn"
          label="1週間の献立はこちら"
          @click="viewmodel.GoWeeklyMealPage"
        />
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup lang="ts">
import { MealCardViewModel } from "~/viewmodel/component/mealcard_vm";

const viewmodel = MealCardViewModel();
</script>

<style scoped>
.custom-card {
  border: 1px solid #ffcc80; /* 淡いオレンジ */
  border-radius: 12px;
}

.custom-btn {
  height: 32px;
  border: 1px solid #ffcc80; /* 淡いオレンジ */
}

.text-btn {
  cursor: pointer;
  font-weight: 500;
}
.text-btn:hover {
  text-decoration: underline;
}
</style>
