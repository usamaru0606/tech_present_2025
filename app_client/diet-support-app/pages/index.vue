<template>
  <v-container fluid class="py-2 px-2">
    <v-row>
      <v-col cols="12" md="7" class="pa-0 d-flex flex-column">
        <div class="pa-2 left-top-container">
          <CChart
            :chartData="viewmodel.chartData.value"
            :userId="viewmodel.userId.value"
          />
        </div>

        <div class="pa-2 left-bottom-container pt-1">
          <div class="d-flex align-center ga-3 pb-3">
            <CIconBtn
              icon="mdi-refresh"
              :isTextPrimary="true"
              :onClick="viewmodel.loadChartData"
            />

            <CIconBtn
              label="体重を記録"
              icon="mdi-pencil"
              :isTextPrimary="true"
              :onClick="viewmodel.OpenRecordWeightDialog"
            />
            <RecordWeightDialog
              v-model="viewmodel.isDialogOpen.value"
              @update:modelValue="viewmodel.OnRecordWeightDialogClosed"
            />
            <CIconBtn
              label="悩み・目標を設定"
              icon="mdi-open-in-new"
              :iconRight="true"
              :onClick="viewmodel.GoGoalSetting"
            />
          </div>

          <RecordWeightCard />
        </div>
      </v-col>
      <v-col cols="12" md="5" class="d-none d-md-flex flex-column pa-0">
        <div class="pa-2 fill-height right-top-container">
          <TrainingCard />
        </div>

        <div class="pa-2 fill-height right-bottom-container">
          <MealCard />
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { IndexViewModel } from "~/viewmodel/index_vm";

const viewmodel = IndexViewModel();
</script>

<style scoped>
.left-top-container {
  flex: 6.5;
}

.left-bottom-container {
  flex: 3.5;
}

.right-top-container {
  flex: 4.5;
}

.right-bottom-container {
  flex: 5.5;
}

.button-row {
  gap: 10px;
  margin: 0px;
  padding: 0px;
}
</style>
