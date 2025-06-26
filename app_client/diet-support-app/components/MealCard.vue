<template>
  <v-card class="meal-card d-flex flex-column" elevation="4" rounded="lg">
    <!-- タイトル -->
    <v-card-title class="text-h6 font-weight-bold pb-0">
      今日のごはん
    </v-card-title>

    <!-- タブ -->
    <client-only>
      <v-tabs
        v-model="viewmodel.selectedMeal.value"
      >
        <v-tab
          v-for="tab in viewmodel.mealTabs"
          width="33.33%"
          :key="tab.key"
          :value="tab.key"
        >
          {{ tab.label }}
        </v-tab>
      </v-tabs>
    </client-only>

    <!-- メイン内容エリア -->
    <v-divider class="ma-0" />

    <div class="flex-grow-1 overflow-auto px-4 py-2 ml-2">
      <v-row dense>
        <v-col
          cols="4"
          v-for="item in viewmodel.mealCategories"
          :key="item.key"
          class="my-4"
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

        <v-col cols="4" class="my-3">
          <CLabelValue
            icon="mdi-fire"
            icon-color="deep-orange"
            label="合計カロリー"
            :value="`${
              viewmodel.menuItem[viewmodel.selectedMeal.value].value.totalCalories || '--'
            } kcal`"
          />
        </v-col>
      </v-row>
    </div>

    <v-divider class="ma-0" />

    <!-- フッター -->
    <div class="footer px-4 pt-2 pb-3">
      <v-row dense>
        <v-col cols="7">
          <CIconBtn
            class="custom-btn"
            label="食事を記録"
            icon="mdi-pencil"
            :onClick="viewmodel.OpenRecordMealDialog"
          />
          <RecordMealDialog
            :timing="viewmodel.mealTabs.find(tab => tab.key === viewmodel.selectedMeal.value)?.label ?? ''"
            v-model="viewmodel.isOpenRecordMealDialog.value"
            :modelMeal="viewmodel.menuItem[viewmodel.selectedMeal.value].value"
            @update:modelValue="onDialogClosed"
          />
        </v-col>
        <v-col cols="5" class="text-right">
          <CTextBtn
            class="text-btn"
            label="1週間の献立はこちら"
            @click="viewmodel.GoWeeklyMealPage"
          />
        </v-col>
      </v-row>
    </div>
  </v-card>
</template>



<script setup lang="ts">
import { MealCardViewModel } from "~/viewmodel/component/mealcard_vm";
import { nextTick } from "vue";

const viewmodel = MealCardViewModel();

// RecordMealDialogの保存完了時にGetMenuを再取得
const onDialogClosed = async (val: boolean) => {
  if (!val) {
    await nextTick(); // ダイアログ閉じた直後に
    if (viewmodel.GetMenu) await viewmodel.GetMenu();
  }
};
</script>

<style scoped>
.meal-card {
  height: 100%;
  border: 1px solid #ffcc80;
  border-radius: 12px;
}

.custom-btn {
  height: 32px;
  border: 1px solid #ffcc80;
}

.text-btn {
  cursor: pointer;
  font-weight: 500;
}
.text-btn:hover {
  text-decoration: underline;
}

.footer {
  background-color: white;
}
</style>
