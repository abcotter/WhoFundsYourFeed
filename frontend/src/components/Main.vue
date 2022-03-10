<template>
	<div class="container">
		<Header />

		<div v-if="userId == 'demo'" class="demo-disclaimer">
			Note: you are viewing demo data!
		</div>

		<DoubleBounce style="margin-top: 30vh" v-if="loading"></DoubleBounce>

		<MainFunder :stats="Stats" v-if="!loading" />

		<div class="secondHeader" @click="scrollDown" v-if="!loading">
			<h1>More Viewing Highlights</h1>
			<div class="downScroll">
				<ion-icon
					name="chevron-down-outline"
					style="font-size: 42px"
				></ion-icon>
			</div>
		</div>

		<ViewingHighlights :stats="Stats" ref="highlights" v-show="!loading" />
		<h1 class="section-header" v-show="!loading">Hip Tips: greenwashing 101</h1>
		<HipTips v-if="!loading" />

		<div v-if="!loading">
			<h2>Share Your Results</h2>
			<ion-icon name="logo-instagram" style="font-size: 35px"></ion-icon>
			<ion-icon name="logo-facebook" style="font-size: 35px"></ion-icon>
			<ion-icon name="download-outline" style="font-size: 35px"></ion-icon>
		</div>
	</div>
</template>

<script>
import Header from "./Header.vue";
import MainFunder from "./MainFunder.vue";
import ViewingHighlights from "./ViewingHighlights.vue";
import HipTips from "./TipsCarousel/HipTips.vue";
import axios from "axios";
import DoubleBounce from "./loader.vue";
import SampleData from "../../../endpointLambdas/reportAnalytics/SampleOutput.json";

export default {
	async mounted() {
		if (this.$route.params.userid) {
			this.userId = this.$route.params.userid;
			let url =
				"https://3vor3iykgi.execute-api.us-east-1.amazonaws.com/default/reportAnalytics";
			let body = {
				userId: this.userId,
			};
			const response = await axios({
				url: url,
				method: "POST",
				data: JSON.stringify(body),
			});
			this.Stats = response.data;
		} else {
			// load demo data
			this.Stats = SampleData;
		}
		// for loading nice data - to cut when we have good data in the DB
		this.Stats = SampleData;
		this.loading = false;
	},
	name: "Main",
	components: {
		Header,
		MainFunder,
		ViewingHighlights,
		HipTips,
		DoubleBounce,
	},
	data: function () {
		return {
			Stats: {},
			loading: true,
			userId: "demo",
		};
	},
	methods: {
		scrollDown() {
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

.demo-disclaimer {
	width: 300px;
	margin: auto;
	margin-bottom: 10px;
	background-color: #ffe66e;
	border-radius: 10%;
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

.section-header {
	font-size: 45px;
}
</style>
