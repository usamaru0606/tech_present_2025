<template>
  <v-card class="px-6 py-4 fill-height" elevation="4" rounded="xl">
    <v-row dense>
      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-weight"
          icon-color="primary"
          label="登録時体重"
          :value="`${viewmodel.cardItem.weight??'--'} kg`"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-scale-bathroom"
          icon-color="blue-darken-2"
          label="現在の体重"
          :value="`${viewmodel.currentWeight.value??'--'} kg`"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-scale-bathroom"
          icon-color="blue-darken-2"
          label="先月の体重"
          :value="`${viewmodel.cardItem.lastMonthWeight??'--'} kg`"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-target"
          icon-color="green-darken-1"
          label="目標体重"
          :value="`${viewmodel.cardItem.goalWeight??'--'} kg`"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          :icon="`mdi-trending-${weightDiffAll < 0 ? 'down' : weightDiffAll > 0 ? 'up' : 'neutral'}`"
          :icon-color="weightDiffAll < 0 ? 'success' : weightDiffAll > 0 ? 'error' : 'grey'"
          label="登録時との差"
          :value="`${weightDiffAll >= 0 ? '+' : ''}${weightDiffAll??'--'} kg`"
          :value-class="weightDiffAll < 0 ? 'text-success' : weightDiffAll > 0 ? 'text-error' : 'text-grey-darken-1'"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          :icon="`mdi-trending-${weightDiff < 0 ? 'down' : weightDiff > 0 ? 'up' : 'neutral'}`"
          :icon-color="weightDiff < 0 ? 'success' : weightDiff > 0 ? 'error' : 'grey'"
          label="先月との差"
          :value="`${weightDiff >= 0 ? '+' : ''}${weightDiff??'--'} kg`"
          :value-class="weightDiff < 0 ? 'text-success' : weightDiff > 0 ? 'text-error' : 'text-grey-darken-1'"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-calendar-end"
          icon-color="deep-purple-accent-2"
          label="目標期限"
          :value="viewmodel.cardItem.goalDate?? '目標未設定'"
        />
      </v-col>

      <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-calendar-today"
          icon-color="indigo"
          label="開始日"
          :value="viewmodel.cardItem.startDate?? '目標未設定'"
        />
      </v-col>

       <v-col cols="4" class="mb-4">
        <CLabelValue
          icon="mdi-calendar-clock"
          icon-color="teal"
          label="継続日数"
          :value="`${viewmodel.continuationDays.value} 日` "
        />
      </v-col>
    </v-row>
  </v-card>
</template>

<script setup lang="ts">
import { RecordWeightCardViewModel } from '~/viewmodel/component/recordweightcard_vm';


const viewmodel = RecordWeightCardViewModel();
const weightDiffAll = viewmodel.weightDiffAllDate.value ?? 0;
const weightDiff = viewmodel.weightDiff.value ?? 0;
</script>

<style scoped>
.text-success {
  color: #2e7d32;
}

.text-error {
  color: #c62828;
}

.text-grey-darken-1 {
  color: #757575;
}
</style>
