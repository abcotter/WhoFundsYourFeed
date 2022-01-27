<template>
	<div>
		<canvas id="pie-chart"></canvas>
	</div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
	name: "PieChart",
	props: ["data"],
	data() {
		return {
			PieChartData: this.data,
		};
	},
	mounted() {
		const ctx = document.getElementById("pie-chart");
		new Chart(ctx, this.PieChartData);
	},
};
</script>