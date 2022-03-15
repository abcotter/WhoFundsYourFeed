<template>
	<div class="funder-card">
		<div class="back-text">
			<canvas
				style="max-width: 30vw; max-height: 30vw"
				id="VideoSponsoredbyFunder"
			></canvas>
		</div>
		<div class="arrow-left">
			<img
				style="height: 300px; width: 300px; transform: rotate(-20deg)"
				src="../../assets/ARROW_RIGHT.png"
			/>
			<div style="position: relative">
				<h1
					style="
						width: 200px;
						font-size: 25px;
						margin: 0px;
						position: absolute;
						left: -4vw;
						top: -6vh;
					"
				>
					{{ stats.outputTimeSponsoredbyFunder }}% of your time on youtube is
					being sponsored by {{ topFunder }}!
				</h1>
			</div>
		</div>
	</div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
	name: "PercentTimeSponsoredStat",
	props: ["topFunder", "stats"],
	mounted() {
		this.chartData = {
			type: "doughnut",
			data: {
				labels: ["Sponsored by Top Funder", "Sponsored by Others"],
				datasets: [
					{
						label: "Watching Stats",
						data: [
							this.stats.outputTimeSponsoredbyFunder,
							100 - this.stats.outputTimeSponsoredbyFunder,
						],
						backgroundColor: ["rgb(255,107,107)", "rgb(247, 255, 247)"],
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

	data() {
		return {
			chartData: null,
		};
	},
	computed: {},
	watch: {
		chartData() {
			new Chart(
				document.getElementById("VideoSponsoredbyFunder").getContext("2d"),
				this.chartData
);
		},
	},
};
</script>

<style scoped>
.funder-card {
	margin: 10px;
	width: 40%;
	height: 90%;
	background-color: rgb(79, 204, 196, 0.6);
	border: 5px solid rgb(131, 211, 205);
	border-radius: 25px;
	padding: 20px;
}
.back-text {
	height: 90%;
	width: 90%;
	margin: auto;
	justify-content: space-evenly;
	align-items: center;
	font-size: 25px;
	font-weight: bold;
	color: #292f36;
	display: flex;
	flex-direction: column;
	padding-top: 25px;
}

.title {
	font-size: 50px;
	color: #292f36;
	display: flex;
	justify-content: center;
}
.channel-list {
	padding-top: 20px;
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
}
.channel {
	margin-bottom: 20px;
	width: 100%;
	display: flex;
	justify-content: start;
}
.number {
	display: flex;
	justify-content: start;
	margin: 0;
	font-size: 30px;
}
.channel-pic {
	max-width: 50px;
	max-height: 50px;
	border-radius: 65px;
	margin-left: 10px;
	margin-top: 10px;
}
.channel-deets {
	display: flex;
	flex-direction: column;
	justify-content: start;
	margin-left: 20px;
	padding-top: 10px;
}
a {
	font-size: 20px;
	color: #292f36;
}

.arrow-left {
	position: absolute;
	top: 45vh;
	left: 5vw;
}
</style>