<template>
	<div class="card">
		<div class="content-flipper" @click="flip">
			<div class="front" :class="{ reveal: flipped }">
				<div class="front-text">
					What percent of your watch time is sponsored?
				</div>
			</div>
			<div class="back" :class="{ reveal: flipped }">
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
	methods: {
		flip() {
			this.flipped = !this.flipped;
		},
	},
};
</script>

<style scoped>
.card {
	margin: 10px;
	height: 35vw;
	margin-bottom: 30px;
}

.content-flipper {
	height: 100%;
	transition: ease-in 300ms;
	transform-style: preserve-3d;
	cursor: pointer;
}

.flip {
	transform: rotateY(180deg);
}

.front {
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	position: absolute;
	height: 100%;
	width: 47vw;
	margin-right: 10px;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
	transition: ease-in 300ms;
	display: flex;
	justify-content: space-around;
}

.front-text {
	height: 90%;
	width: 90%;
	margin: auto;
	justify-content: center;
	align-items: center;
	font-size: 30px;
	color: #292f36;
	display: flex;
	font-weight: bold;
	border: 5px solid #f5f5f5;
	border-radius: 25px;
	padding: 10px;
}

.front.reveal {
	transform: rotateY(180deg);
}

.back {
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	position: absolute;
	height: 100%;
	width: 47vw;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
	transform: rotateY(180deg);
	transition: ease-in 300ms;
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

.back.reveal {
	transform: rotateY(0deg);
}
</style>