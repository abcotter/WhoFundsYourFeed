<template>
	<div class="container">
		<Header />

		<MainFunder :stats="Stats" />

		<div class="secondHeader" @click="scrollDown">
			<h1>More Viewing Highlights</h1>
			<div class="downScroll">
				<ion-icon
					name="chevron-down-outline"
					style="font-size: 42px"
				></ion-icon>
			</div>
		</div>

		<ViewingHighlights :stats="Stats" ref="highlights" />

		<h2>Share Your Results</h2>
		<ion-icon name="logo-instagram" style="font-size: 35px"></ion-icon>
		<ion-icon name="logo-facebook" style="font-size: 35px"></ion-icon>
		<ion-icon name="download-outline" style="font-size: 35px"></ion-icon>
	</div>
</template>

<script>
import Header from "./Header.vue";
import MainFunder from "./MainFunder.vue";
import ViewingHighlights from "./ViewingHighlights.vue";
import sampleResponse from "../../../endpointLambdas/reportAnalytics/SampleOutput.json";

export default {
	mounted() {
		// todo call Fatimahs API and get real data
		this.Stats = sampleResponse;
	},
	name: "Main",
	components: {
		Header,
		MainFunder,
		ViewingHighlights,
	},
	data: function () {
		return {
			Stats: {},
		};
	},
	methods: {
		scrollDown() {
			console.log("scroll");
			console.log(this.$refs.highlights.$refs.moreStats.offsetTop);
			window.scrollTo({
				top: this.$refs.highlights.$refs.moreStats.offsetTop,
				behavior: "smooth",
			});
		},
	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
	background-color: #ffcbc6;
}

.yellow-bar {
	position: absolute;
	top: 13vh;
	left: 3vw;
	max-width: 12vw;
	max-height: 75vh;
	transform: scaleX(-1);
}

.secondHeader {
	margin: auto;
	font-size: 12px;
	color: #292f36;
	margin-top: 15px;
	cursor: pointer;
	width: 400px;
}

h1 {
	margin: 0;
}
</style>
