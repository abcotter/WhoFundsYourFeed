<template>
	<div class="funder-card">
		<div class="content-flipper" @click="flip">
			<div class="front" :class="{ reveal: flipped }">
				<div class="front-text">
					What percent of my videos have been funded by {{ topFunder }}?
				</div>
			</div>
			<div class="back" :class="{ reveal: flipped }">
				<div class="back-text">
					{{ stats.outputTimeSponsoredbyFunder }}% of your time on youtube is being
				sponsored by {{topFunder}}!
				<canvas
					style="max-width: 30vw; max-height: 30vw"
					id="VideoSponsoredbyFunder"
				></canvas>
				
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Chart from "chart.js/auto";

export default {
	name: "PercentTimeSponsoredStat",
	props: ["topFunder", "stats"],
	mounted(){
		this.chartData ={
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
							backgroundColor: ["rgb(255, 230, 109)", "rgb(247, 255, 247)"],
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
			flipped: false,
			chartData: null,
		};
	},
	computed: {
		
	},
	watch: {
		chartData() {
			const ctx = document.getElementById("VideoSponsoredbyFunder");
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
.funder-card {
	margin: 10px;
	width: 40%;
}

.content-flipper {
	width: 100%;
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
	background-color: #4fccc4;
	position: absolute;
	width: 100%;
	height: 100%;
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
	background-color: #4fccc4;
	position: absolute;
	width: 100%;
	height: 100%;
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
</style>