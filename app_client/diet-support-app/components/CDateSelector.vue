<template>
  <p class="label">{{ label }}</p>
  <v-row dense no-gutters :for="label">
    <v-col cols="auto">
      <CSelect
        id="year"
        :model-value="Year"
        :items="computedYears"
        @update:model-value="onYearChange"
        label="年"
        class="select-item-year"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        id="month"
        :model-value="Month"
        :items="months"
        @update:model-value="onMonthChange"
        label="月"
        class="select-item mx-3"
      />
    </v-col>
    <v-col cols="auto">
      <CSelect
        id="day"
        :model-value="Day"
        :items="days"
        @update:model-value="onDayChange"
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

  <v-dialog v-model="showCalendar" max-width="320">
    <v-card>
      <v-locale-provider locale="ja">
        <v-date-picker
          title="日付選択"
          v-model="selectedDate"
          :min="minDate"
          :max="maxDate"
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
const props = defineProps({
  Year: { type: Number, required: true },
  Month: { type: Number, required: true },
  Day: { type: Number, required: true },
  feature: { type: Boolean, default: false },
  label: String,
  minmode: { type: Boolean, default: false },
});

const emit = defineEmits(["update:Year", "update:Month", "update:Day"]);

const currentYear = new Date().getFullYear();
const today = new Date();

const minDate = computed(() => (props.minmode ? undefined : today));
const maxDate = computed(() => (props.minmode ? today : undefined));

// 年の選択肢を min/max で絞る
const computedYears = computed(() => {
  let start = currentYear - 99;
  let end = currentYear;
  if (props.feature) {
    start = currentYear;
    end = currentYear + 99;
  }
  if (minDate.value) start = Math.max(start, minDate.value.getFullYear());
  if (maxDate.value) end = Math.min(end, maxDate.value.getFullYear());

  const years = [];
  for (let y = end; y >= start; y--) {
    years.push(y);
  }
  return years;
});

// 月の選択肢を年に応じて絞る
const months = computed(() => {
  let start = 1;
  let end = 12;

  if (minDate.value && props.Year === minDate.value.getFullYear()) {
    start = minDate.value.getMonth() + 1;
  }
  if (maxDate.value && props.Year === maxDate.value.getFullYear()) {
    end = maxDate.value.getMonth() + 1;
  }

  const mths = [];
  for (let m = start; m <= end; m++) {
    mths.push(m);
  }
  return mths;
});

// 日の選択肢を年・月に応じて絞る
const days = computed(() => {
  const year = props.Year;
  const month = props.Month;
  const lastDay = new Date(year, month, 0).getDate();

  let start = 1;
  let end = lastDay;

  if (
    minDate.value &&
    year === minDate.value.getFullYear() &&
    month === minDate.value.getMonth() + 1
  ) {
    start = minDate.value.getDate();
  }
  if (
    maxDate.value &&
    year === maxDate.value.getFullYear() &&
    month === maxDate.value.getMonth() + 1
  ) {
    end = Math.min(end, maxDate.value.getDate());
  }

  const ds = [];
  for (let d = start; d <= end; d++) {
    ds.push(d);
  }
  return ds;
});

const showCalendar = ref(false);
const selectedDate = ref(new Date(props.Year, props.Month - 1, props.Day));

watch(
  () => [props.Year, props.Month, props.Day],
  ([year, month, day]) => {
    selectedDate.value = new Date(year, month - 1, day);
  }
);

function onYearChange(val: number) {
  let newMonth = props.Month;
  let newDay = props.Day;

  if (!props.minmode) {
    // minmodeがtrueなら「minDateがある＝過去日付の下限制御」
    // → 年がminDate年の場合は月日をminDate以降に調整
    if (val === minDate.value?.getFullYear()) {
      if (!months.value.includes(newMonth)) {
        newMonth = months.value[0];
      }
      if (newMonth < minDate.value.getMonth() + 1) {
        newMonth = minDate.value.getMonth() + 1;
        newDay = minDate.value.getDate();
      } else if (
        newMonth === minDate.value.getMonth() + 1 &&
        newDay < minDate.value.getDate()
      ) {
        newDay = minDate.value.getDate();
      }
      if (!days.value.includes(newDay)) {
        newDay = days.value[0];
      }
    } else {
      // minDate年以外なら普通に範囲内に調整
      if (!months.value.includes(newMonth)) {
        newMonth = months.value[0];
      }
      if (!days.value.includes(newDay)) {
        newDay = days.value[0];
      }
    }
  } else {
    // minmodeがfalseなら「maxDateがある＝未来日付の上限制御」
    // → 年がcurrentYearなら今日の日付を上限に調整
    if (val === currentYear) {
      const todayMonth = today.getMonth() + 1;
      const todayDay = today.getDate();

      if (!months.value.includes(newMonth)) {
        newMonth = months.value[0];
      }
      if (newMonth > todayMonth) {
        newMonth = todayMonth;
        newDay = todayDay;
      } else if (newMonth === todayMonth && newDay > todayDay) {
        newDay = todayDay;
      }
      if (!days.value.includes(newDay)) {
        newDay = days.value[0];
      }
    } else {
      // currentYear以外ならmaxDate制限内に調整
      if (!months.value.includes(newMonth)) {
        newMonth = months.value[0];
      }
      if (!days.value.includes(newDay)) {
        newDay = days.value[0];
      }

      if (maxDate.value && val === maxDate.value.getFullYear()) {
        if (newMonth > maxDate.value.getMonth() + 1) {
          newMonth = maxDate.value.getMonth() + 1;
          newDay = maxDate.value.getDate();
        } else if (
          newMonth === maxDate.value.getMonth() + 1 &&
          newDay > maxDate.value.getDate()
        ) {
          newDay = maxDate.value.getDate();
        }
      }
    }
  }

  emit("update:Year", val);
  if (newMonth !== props.Month) emit("update:Month", newMonth);
  if (newDay !== props.Day) emit("update:Day", newDay);
}

// 月変更時の処理
function onMonthChange(val: number) {
  let newDay = props.Day;
  if (!days.value.includes(newDay)) {
    newDay = days.value[0];
  }
  emit("update:Month", val);
  if (newDay !== props.Day) emit("update:Day", newDay);
}

// 日変更時はそのままemit
function onDayChange(val: number) {
  emit("update:Day", val);
}

// カレンダーで日付選択されたとき
function onDateSelected(val: Date) {
  emit("update:Year", val.getFullYear());
  emit("update:Month", val.getMonth() + 1);
  emit("update:Day", val.getDate());
  showCalendar.value = false;
}
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

.border {
  border-top: 1px solid lightgray;
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
