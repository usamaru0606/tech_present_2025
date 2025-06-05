<template>
  <v-container fluid class="pa-0 fill-height">
    <v-row class="fill-height">
      <v-col cols="12" md="7" class="pa-0 d-flex flex-column fill-height">
        <div class="pa-2 left-top-container">
          <CChart
            :chartData="viewmodel.chartData.value"
            :userId="viewmodel.userId.value"
          />
        </div>

        <div class="pa-2 left-bottom-container">
          <v-row class="button-row" dense no-Gutters>
            <v-col cols="auto">
              <CIconBtn
                icon="mdi-refresh"
                :isTextPrimary="true"
                :onClick="viewmodel.Reload"
              />
            </v-col>

            <v-col cols="auto">
              <CIconBtn
                label="体重を記録"
                icon="mdi-pencil"
                :isTextPrimary="true"
                :onClick="viewmodel.GoRecordWeight"
              />
            </v-col>

            <v-col cols="auto">
               <CIconBtn
                label=" 悩み・目標を設定"
                icon="mdi-open-in-new"
                :iconRight="true"
                :onClick="viewmodel.GoGoalSetting"
              />
            </v-col>
          </v-row>
        </div>
      </v-col>

      <v-col
        cols="12"
        md="5"
        class="d-none d-md-flex flex-column align-center justify-space-between right-side-container pa-10"
      >
        <v-btn
          class="relaodBtn w-auto"
          @click="viewmodel.Reload"
          text="トレーニングメニュー"
        />
        <v-btn
          class="relaodBtn w-auto"
          @click="viewmodel.Reload"
          text="食事メニュー"
        />
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
  min-height: 0;
  display: flex;
  flex-direction: column;
  flex: 6.5;
}

.left-bottom-container {
  border: 1px #e8f5f0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  flex: 3.5;
}

.right-side-container {
  background-color: #fff3e0;
  border: 1px solid #ffcc80;
}

.button-row {
  gap: 10px;
}
</style>
