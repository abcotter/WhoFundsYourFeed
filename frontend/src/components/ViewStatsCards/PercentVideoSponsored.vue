<template>
	<div class="card">
		<div class="content-flipper" @click="flip">
			<div class="front" :class="{ reveal: flipped }">
				<div class="front-text">What percent of your videos sponsored?</div>
			</div>
			<div class="back" :class="{ reveal: flipped }">
				<div class="back-text">
					INSERT DATA VISUAL FOR STAT <br />
					I'm where % of videos you watch that's sponsored goes
				</div>
			</div>
		</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
export default {
	name: "PercentVideoSponsoredStat",
	data() {
		return {
			flipped: false,
		};
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
	height: 600px;
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
	background-color: rgb(255, 230, 109);
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
	background-color: rgb(255, 230, 109);
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
	justify-content: center;
	align-items: center;
	font-size: 20px;
	color: #292f36;
	display: flex;
	padding: 10px;
}

.back.reveal {
	transform: rotateY(0deg);
}
</style>