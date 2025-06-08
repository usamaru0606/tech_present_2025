<template>
  <v-label class="label">{{ label }}</v-label>

  <v-row dense no-gutters>
    <v-col cols="auto">
      <CSelect
        :model-value="Year"
        :items="computedYears"
        @update:model-value="$emit('update:Year', $event)"
        label="年"
        class="select-item-year"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        :model-value="Month"
        :items="months"
        @update:model-value="$emit('update:Month', $event)"
        label="月"
        class="select-item mx-3"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        :model-value="Day"
        :items="days"
        @update:model-value="$emit('update:Day', $event)"
        label="日"
        class="select-item"
      />
    </v-col>
    <v-col cols="auto" class="d-flex align-center pl-2">
      <v-btn
        icon="mdi-calendar"
        variant="text"
        density="compact"
        @click="showCalendar = true"
      />
    </v-col>
  </v-row>

  <v-dialog v-if="!minmode" v-model="showCalendar" max-width="320">
    <v-card>
      <v-locale-provider locale="ja">
        <v-date-picker
          title="日付選択"
          v-model="selectedDate"
          :min="today"
          color="primary"
          @update:model-value="onDateSelected"
        />
      </v-locale-provider>
      <v-card-actions  class="border">
        <v-spacer />
        <v-btn text @click="showCalendar = false">閉じる</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-if="minmode" v-model="showCalendar" max-width="320">
    <v-card>
      <v-locale-provider locale="ja">
        <v-date-picker
          title="日付選択"
          v-model="selectedDate"
          :max="today"
          color="primary"
          @update:model-value="onDateSelected"
        />
      </v-locale-provider>
      <v-card-actions class="border">
        <v-spacer />
        <v-btn text @click="showCalendar = false">閉じる</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

// props
const props = defineProps({
  Year: [String, Number],
  Month: [String, Number],
  Day: [String, Number],
  feature: {
    type: Boolean,
    default: false,
  },
  label: String,
  minmode:{
    type: Boolean,
    default: false,
  }
});

// emit
const emit = defineEmits(["update:Year", "update:Month", "update:Day"]);

// 日付関連
const currentYear = new Date().getFullYear();
const years = Array.from({ length: 100 }, (_, i) => currentYear - i);
const featureYears = Array.from({ length: 100 }, (_, i) => currentYear + i);
const months = Array.from({ length: 12 }, (_, i) => i + 1);
const days = Array.from({ length: 31 }, (_, i) => i + 1);

const computedYears = computed(() => (props.feature ? featureYears : years));

// カレンダー表示管理
const showCalendar = ref(false);
const today = new Date().toISOString().split("T")[0]; // yyyy-mm-dd
const selectedDate = ref(today);

// カレンダー日付選択時の処理
const onDateSelected = (val: string) => {
  const date = new Date(val);
  emit("update:Year", date.getFullYear());
  emit("update:Month", date.getMonth() + 1);
  emit("update:Day", date.getDate());
  showCalendar.value = false;
};
</script>

<style scoped>
.label {
  color: black;
  font-size: 12px;
  font-weight: bold;
}
.select-item {
  width: 85px;
}
.select-item-year {
  width: 108px;
}

.border{
  border-top: 1 solid lightgray;
}

::v-deep(.v-date-picker-month__days) {
  text-align: center;
}

::v-deep(.v-date-picker-month__day--week-start) {
  color: red;
}

::v-deep(.v-date-picker-month__day--week-end) {
  color: blue;
}
</style>
