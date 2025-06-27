<template>
  <v-card class="pt-2 fill-height custom-card" elevation="4" rounded="lg">
    <v-card-title class="text-h6 font-weight-bold pb-0">
      今日のトレーニング
    </v-card-title>

    <v-divider class="my-2" />

    <v-row dense class="px-4 ml-2 min-height-row" align="center">
      <template v-if="viewmodel.trainingMenu.value.trainings.length > 0">
        <v-col
          cols="12"
          v-for="(item, index) in viewmodel.trainingMenu.value.trainings"
          :key="index"
          class="my-2"
        >
          <v-row no-gutters>
            <v-col cols="3" class="text-left">
              <strong>{{ item.trainingMenu }}</strong>
            </v-col>
            <v-col cols="3" class="text-center">
              時間: {{ item.trainingTime }} 分
            </v-col>
            <v-col cols="5" class="text-right">
              消費カロリー: {{ item.calories }} kcal
            </v-col>
          </v-row>
        </v-col>
      </template>
      <template v-else>
        <v-col cols="12" class="text-center text-grey my-4">
          トレーニングメニューが登録されていません
        </v-col>
      </template>
    </v-row>

    <v-divider class="my-3" />

    <v-row class="py-1">
      <v-col cols="6">
        <CIconBtn
          class="ml-3 py-0 px-4 custom-btn"
          label="トレーニングを記録"
          icon="mdi-pencil"
          :onClick="viewmodel.OpenRecordTrainingDialog"
        />
        <RecordTrainingDialog
          v-model="viewmodel.isOpenRecordTrainingDialog.value"
          :modelTraining="viewmodel.trainingMenu.value"
        />
      </v-col>
      <v-col cols="3" class="pa-1 pl-4">
        <CLabelValue
          icon="mdi-timer"
          icon-color="green"
          label="合計"
          :value="`${viewmodel.totalTime.value ?? '--'} 分`"
        />
      </v-col>
      <v-col cols="3" class="pa-1 pl-4">
        <CLabelValue
          icon="mdi-fire"
          icon-color="deep-orange"
          label="合計"
          :value="`${viewmodel.trainingMenu.value.totalCalories ?? '--'} kcal`"
        />
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup lang="ts">
import { TrainingCardViewModel } from "~/viewmodel/component/trainingcard_vm";

const viewmodel = TrainingCardViewModel();
</script>

<style scoped>
.custom-card {
  border: 1px solid #90caf9; /* 淡い青 */
  border-radius: 12px;
}

.custom-btn {
  height: 32px;
  border: 1px solid #90caf9; /* 淡い青 */
}

.min-height-row {
  min-height: 200px;
  max-height: 200px;
  overflow-y: auto;
}
</style>
