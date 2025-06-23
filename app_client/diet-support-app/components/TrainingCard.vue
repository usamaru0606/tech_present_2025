<template>
  <v-card class="px-4 pt-2 fill-height custom-card" elevation="4" rounded="lg">
    <v-card-title class="text-h6 font-weight-bold pb-0">
      今日のトレーニング
    </v-card-title>

    <v-divider class="my-2" />

    <v-row dense class="ml-1 min-height-row" align="center">
      <template v-if="viewmodel.trainingMenu.value.exercises.length > 0">
        <v-col
          cols="12"
          v-for="(item, index) in viewmodel.trainingMenu.value.exercises"
          :key="index"
          class="my-2"
        >
          <v-row no-gutters>
            <v-col cols="3" class="text-left">
              <strong>{{ item.trainingMenu }}</strong>
            </v-col>
            <v-col cols="3" class="text-center">
              回数: {{ item.trainingTime }} 回
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

    <v-row class="pb-4">
      <v-col cols="8">
        <CIconBtn
          class="ml-3 py-0 px-4 custom-btn"
          label="トレーニングを記録"
          icon="mdi-pencil"
          :onClick="viewmodel.OpenRecordTrainingDialog"
        />
        <!-- <RecordTrainingDialog
          session="今日"
          v-model="viewmodel.isOpenRecordTrainingDialog.value"
          :modelTraining="viewmodel.trainingMenu.value"
        /> -->
      </v-col>
      <v-col cols="4" class="pa-1 text-center">
        <CLabelValue
          icon="mdi-fire"
          icon-color="deep-orange"
          label="合計消費カロリー"
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
