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
import axios from "axios";

export default {
	async mounted() {
		// todo call Fatimahs API and get real data
		let userId = "10001";
		let url =
			"https://3vor3iykgi.execute-api.us-east-1.amazonaws.com/default/reportAnalytics";
		let body = {
			userId: userId,
		};
		const response = await axios({
			url: url,
			method: "POST",
			data: JSON.stringify(body),
		});
		const test = await response.data;
		this.Stats = test;
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
