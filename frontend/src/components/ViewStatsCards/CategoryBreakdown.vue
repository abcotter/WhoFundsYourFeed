<template>
	<div class="card">
		<div class="back">
			<div class="back-text">
				"{{ mostWatchedCategory }}" is your most watched category
				<canvas
					style="max-width: 40vw; max-height: 30vw"
					id="Category"
				></canvas>
			</div>
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
			mostWatchedCategory: null,
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

			this.mostWatchedCategory = this.stats.outputTopCategories[0][0];
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
.card {
	margin: 10px;
	min-height: 26vw;
}

.back {
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	position: absolute;
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