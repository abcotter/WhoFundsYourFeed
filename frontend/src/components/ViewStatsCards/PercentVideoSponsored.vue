<template>
	<div class="back">
		<div class="back-text">
			<canvas
				style="max-width: 35vw; max-height: 35vw"
				id="VideoSponsored"
			></canvas>
		</div>
	</div>
</template>

<script>
import Chart from "chart.js/auto";

//define components here that can be used elsewhere
export default {
	name: "PercentVideoSponsoredStat",
	props: ["stats"],
	data() {
		return {
			flipped: false,
		};
	},
	computed: {
		chartData() {
			return {
				type: "doughnut",
				data: {
					labels: ["Sponsored Videos", "Unsponsored Video"],
					datasets: [
						{
							label: "Watching Stats",
							data: [
								this.stats.outputVideoSponsored,
								100 - this.stats.outputVideoSponsored,
							],
							backgroundColor: ["rgb(255, 230, 109)", "rgb(79,204,196)"],
							borderColor: "#36495d",
							borderWidth: 1,
						},
					],
				},
				options: {
					responsive: true,
				},
			};
		},
	},
	watch: {
		chartData() {
			const ctx = document.getElementById("VideoSponsored");
			new Chart(ctx, this.chartData);
		},
	},
};
</script>

<style scoped>
.back {
	width: 40vw;
	height: 40vw;
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	width: 47vw;
	border: 5px solid #f5f5f5;
	border-radius: 25px;
	margin: auto;
}

.back-text {
	height: 90%;
	width: 90%;
	margin: auto;
	justify-content: center;
	align-items: center;
	font-size: 20px;
	color: #292f36;
	display: flex;
	flex-direction: column;
	padding: 10px;
}
</style>