<template>
  <v-container fluid class="pa-2 weekly-container">
    <h2 class="text-h5 font-weight-bold mb-2">1週間の献立</h2>

    <v-tabs v-model="viewmodel.currentTab.value" class="border">
      <v-tab
  v-for="(day, index) in viewmodel.weeklyMeals.value"
  :key="index"
  :class="getTabClass(day.label)"
>
  {{ day.date }}<br />{{ day.label }}
</v-tab>

    </v-tabs>

    <v-window v-model="viewmodel.currentTab.value" class="scroll-y pt-6 px-4">
      <v-window-item
        v-for="(day, index) in viewmodel.weeklyMeals.value"
        :key="index"
      >
        <v-row>
          <v-col
            v-for="tab in viewmodel.mealTabs"
            :key="tab.key"
            cols="12"
            md="4"
            class="pa-0"
          >
            <v-card elevation="2" class="mb-4">
              <v-card-title class="text-subtitle-1 font-weight-bold">
                {{ tab.label }}
              </v-card-title>
              <v-card-text>
                <div
                  v-for="item in viewmodel.mealCategories"
                  :key="item.key"
                  class="my-2"
                >
                  <CLabelValue
                    :icon="item.icon"
                    icon-color="orange"
                    :label="item.label"
                    :value="day.meals[tab.key][item.key] || '--'"
                  />
                </div>

                <div class="mt-4">
                  <CLabelValue
                    icon="mdi-fire"
                    icon-color="deep-orange"
                    label="合計カロリー"
                    :value="`${day.meals[tab.key].totalCalories || '--'} kcal`"
                  />
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <!-- 🔽 1日の合計カロリー -->
        <v-container elevation="1" class="my-2 pa-2 w-50 total-day-calories">
          <CLabelValue
            icon="mdi-counter"
            icon-color="red"
            label="1日の合計カロリー"
            :value="`${viewmodel.GetTotalCalories(day)} kcal`"
          />
        </v-container>
      </v-window-item>
    </v-window>
  </v-container>
</template>

<script setup lang="ts">
import { WeeklyMealViewModel } from "~/viewmodel/weeklymeal_vm";

const viewmodel = WeeklyMealViewModel();
const getTabClass = (label: string): string => {
  if (label === "土") return "saturday-tab";
  if (label === "日") return "sunday-tab";
  return "";
};

</script>

<style scoped>
.v-tabs {
  min-height: fit-content;
  display: flex;
  justify-content: space-between;
}

.v-tab {
  flex-grow: 1;
  text-align: center;
  border-right: 1px solid rgba(0, 0, 0, 0.12);
}

.v-tab:last-child {
  border-right: none;
}

.weekly-container {
  height: 80vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.scroll-y {
  min-height: 60vh;
  overflow-y: auto;
}

.total-day-calories {
  text-align: center;
  border: 1px solid #f0c0c0;
}

.saturday-tab {
  color: #1976d2; /* 青系 */
  font-weight: bold;
}

.sunday-tab {
  color: #d32f2f; /* 赤系 */
  font-weight: bold;
}

</style>
