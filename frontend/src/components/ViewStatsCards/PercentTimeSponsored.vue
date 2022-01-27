<template>
	<div class="card">
		<div class="back">
			<div class="back-text">
				<canvas
					style="max-width: 30vw; max-height: 30vw"
					id="TimeSponsored"
				></canvas>
				{{ stats.outputTimeSponsored }}% of your time on youtube is being
				sponsored!
			</div>
		</div>
	</div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
	name: "PercentTimeSponsoredStat",
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
					labels: ["Sponsored Time", "Unsponsored Time"],
					datasets: [
						{
							label: "Watching Stats",
							data: [
								this.stats.outputTimeSponsored,
								100 - this.stats.outputTimeSponsored,
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
			const ctx = document.getElementById("TimeSponsored");
			new Chart(ctx, this.chartData);
		},
	},
	methods: {},
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
	background-color: rgb(247, 255, 247);
	position: absolute;
	width: 47vw;
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