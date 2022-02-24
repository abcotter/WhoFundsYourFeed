<template>
	<div class="back">
		<div class="back-text">
			<canvas style="max-width: 40vw; max-height: 45vw" id="Category"></canvas>
		</div>
	</div>
</template>

<script>
import Chart from "chart.js/auto";
//define components here that can be used elsewhere
export default {
	name: "CategoryBreakdown",
	props: ["stats"],
	data() {
		return {
			chartData: null,
		};
	},
	watch: {
		stats() {
			this.chartData = {
				type: "bar",
				data: {
					labels: this.stats.outputTopCategories.map(
						(x) => x["video_category"]
					),
					datasets: [
						{
							label: ["frequency"],
							data: this.stats.outputTopCategories.map(
								(x) => x["count(video_category)"]
							),
							backgroundColor: ["rgb(255,107,107)"],
						},
					],
				},
				options: {
					responsive: true,
				},
			};
		},
		chartData() {
			const ctx = document.getElementById("Category");
			new Chart(ctx, this.chartData);
		},
	},
	methods: {},
};
</script>

<style scoped>
.back {
	min-height: 25vw;
	margin: auto;
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	width: 47vw;
	border: 5px solid #f5f5f5;
	border-radius: 25px;
}

.back-text {
	height: 90%;
	width: 90%;
	margin: auto;
	justify-content: space-evenly;
	align-items: center;
	font-size: 20px;
	color: #292f36;
	display: flex;
	flex-direction: column;
	padding: 10px;
}
</style>