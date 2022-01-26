<template>
  <div>
    <canvas id="pie-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import PieChartData from '../pie-data.js'


export default {
  name: 'PieChart',
  data() {
    return {
      PieChartData: PieChartData
    }
  },
  mounted() {
    const ctx = document.getElementById('pie-chart');
    new Chart(ctx, this.PieChartData);
  }
}
</script>