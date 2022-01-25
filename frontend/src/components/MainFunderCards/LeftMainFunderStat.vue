<template>
	<div class="funderCard">
		<div class="content-flipper" @click="flip">
			<div class="front" :class="{ reveal: flipped }">
				<div>Left Stat</div>
			</div>
			<div class="back" :class="{ reveal: flipped }">
				<div>
					maybe I contain a % statistic that says what amount of the videos you
					watch does this funder sponser
				</div>
			</div>
		</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
export default {
	name: "LeftMainFunderStat",
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

<style>
.funderCard {
	margin: 10px;
	width: 40%;
}

.content-flipper {
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	width: 100%;
	height: 100%;
	transition: ease-in 300ms;
	transform-style: preserve-3d;
}

.flip {
	transform: rotateY(180deg);
}

.front {
	position: absolute;
	width: 100%;
	height: 100%;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
}

.front.reveal {
	transform: rotateY(180deg);
}

.back {
	position: absolute;
	width: 100%;
	height: 100%;
	-webkit-backface-visibility: hidden;
	backface-visibility: hidden;
	transform: rotateY(180deg);
}

.back.reveal {
	transform: rotateY(0deg);
}
</style>