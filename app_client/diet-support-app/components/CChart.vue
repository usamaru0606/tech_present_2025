<template>
  <v-row class="button-row" dense no-Gutters>
    <v-col cols="auto" v-for="period in periods" :key="period">
      <v-btn
        class="chart_Btn"
        :class="{ selected: selectedPeriod === period }"
        @click="changePeriod(period)"
      >
        {{ period }}
      </v-btn>
    </v-col>
  </v-row>

  <v-card class="chart-card" elevation="2">
    <v-card-text class="pa-0 chart-card-text position-relative">
      <Line :data="computedChartData" :options="chartOptions" />
      <div v-if="!userId" class="overlay d-flex align-center justify-center">
        <v-card flat color="transparent" class="text-center">
          <CTextBtn
            label="ログインして下さい"
            color="primary"
            @click="GoLoginPage"
          />
        </v-card>
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
} from "chart.js";
import { Line } from "vue-chartjs";
import type { ChartData, ChartOptions } from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler
);
const router = useRouter();

const datasetStyle = {
  borderColor: "#42A5F5",
  backgroundColor: "rgba(66, 165, 245, 0.2)",
  tension: 0.2,
  fill: true,
};

const props = defineProps<{
  chartData: ChartData<"line">;
  userId: number | null;
}>();

const periods = ["1週間", "1か月間", "半年間", "1年間"] as const;
type Period = (typeof periods)[number];
const selectedPeriod = ref<Period>(periods[0]);

const periodLengthMap = {
  "1週間": 7,
  "1か月間": 30,
  "半年間": 180,
  "1年間": 365,
} as const;

const intervalMap = {
  "1週間": 1,
  "1か月間": 1,
  "半年間": 7,
  "1年間": 15,
} as const;

function changePeriod(period: (typeof periods)[number]) {
  selectedPeriod.value = period;
}

// 加工済み chartData を返す
const computedChartData = computed(() => {
  const datasets = props.chartData.datasets || [];
  const originalLabels = props.chartData.labels as (string | number)[] || [];

  if (originalLabels.length === 0) {
    return props.chartData;
  }

  const limit = periodLengthMap[selectedPeriod.value];
  const interval = intervalMap[selectedPeriod.value];
  const latestLabel = originalLabels[originalLabels.length - 1].toString();
  const expectedLabels = createDateLabels(latestLabel, limit, interval);
  const labelIndexMap = createLabelIndexMap(originalLabels);
  const paddedDatasets = padDatasetsWithLabels(datasets, expectedLabels, labelIndexMap);

  return {
    ...props.chartData,
    labels: expectedLabels,
    datasets: paddedDatasets,
  };
});

function createDateLabels(
  latestLabel: string,
  days: number,
  step: number
): string[] {
  const currentYear = new Date().getFullYear();
  const [monthStr, dayStr] = latestLabel.split("/");
  const month = parseInt(monthStr, 10) - 1;
  const day = parseInt(dayStr, 10);

  const labels: string[] = [];
  for (let i = days - 1; i >= 0; i -= step) {
    const d = new Date(currentYear, month, day - i);
    labels.push(`${d.getMonth() + 1}/${d.getDate()}`);
  }
  return labels;
}

function createLabelIndexMap(labels: (string | number)[]): Map<string, number> {
  const map = new Map<string, number>();
  labels.forEach((label, i) => {
    map.set(label.toString(), i);
  });
  return map;
}

function padDatasetsWithLabels(
  datasets: typeof props.chartData.datasets,
  expectedLabels: string[],
  labelIndexMap: Map<string, number>
) {
  return datasets.map((ds) => {
    const originalData = ds.data as (number | null)[];
    const paddedData = expectedLabels.map((label) => {
      const idx = labelIndexMap.get(label);
      return idx !== undefined ? originalData[idx] : null;
    });
    return {
      ...datasetStyle,
      ...ds,
      data: paddedData,
    };
  });
}



const chartOptions = computed<ChartOptions<"line">>(() => ({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: true,
      position: "center",
    },
    title: {
      display: true,
      text: `体重記録(${selectedPeriod.value})`,
    },
  },
  scales: {
    x: {
      title: {
        display: true,
        text: "日付",
      },
    },
    y: {
      title: {
        display: true,
        text: "体重 (kg)",
      },
      suggestedMin: 60,
      suggestedMax: 80,
    },
  },
}));

function GoLoginPage() {
  router.push("/login");
}
</script>

<style scoped>
.chart-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 0;
}

.chart-card-text {
  flex: 1;
  display: flex;
  min-height: 0;
}

.chart-card-text canvas {
  width: 100% !important;
  height: 100% !important;
  max-width: 100%;
  max-height: 100%;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(240, 240, 240, 0.75);
  z-index: 10;
}

.chart_Btn {
  padding: 6px;
  height: 30px;
  color: #1976d2;
  background-color: transparent;
}

.chart_Btn.selected {
  background-color: #1976d2;
  color: white;
}
</style>
