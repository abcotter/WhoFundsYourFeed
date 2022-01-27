<template>
	<div class="card">
		<div class="back">
			<div class="back-text">
				<canvas
					style="max-width: 30vw; max-height: 30vw"
					id="VideoSponsored"
				></canvas>
				{{ stats.outputVideoSponsored }} of videos you watch are sponsored!
			</div>
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
							backgroundColor: ["rgb(255, 99, 132)", "rgb(54, 162, 235)"],
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
.card {
	margin: 10px;
	height: 35vw;
}

.back {
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(255, 230, 109);
	position: absolute;
	width: 47vw;
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