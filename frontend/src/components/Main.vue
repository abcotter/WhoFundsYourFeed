<template>
	<div class="container">
		<Header />

		<div class="demo-toggle">
			<toggle-switch
				:options="myOptions"
				v-model="isLiveData"
				@change="toggleDemoState($event.value)"
			></toggle-switch>
			<div v-if="isLiveData == 'Demo'" class="demo-disclaimer">
				Note: you are viewing demo data!
			</div>
			<div v-if="isLiveData == 'Live' && noData" class="demo-disclaimer">
				PSSSTTT! check out a demo here!
			</div>
		</div>

		<div v-if="noData" class="no-data">
			hhhm....Looks like we haven't collected viewing data for you yet <br />
			Go watch some
			<a href="http://www.youtube.com" target="_blank" style="color: black"
				>YouTube
			</a>
			and we'll start gathering insights!
		</div>

		<DoubleBounce
			style="margin-top: 30vh"
			v-if="loading && !noData"
		></DoubleBounce>

		<MainFunder :stats="Stats" v-if="!loading && !noData" />

		<div class="secondHeader" @click="scrollDown" v-if="!loading && !noData">
			<h1>More Viewing Highlights</h1>
			<div class="downScroll">
				<ion-icon
					name="chevron-down-outline"
					style="font-size: 42px"
				></ion-icon>
			</div>
		</div>

		<ViewingHighlights
			:stats="Stats"
			ref="highlights"
			v-show="!loading && !noData"
		/>
		<h1 class="section-header" v-show="!loading && !noData">
			Hip Tips: greenwashing 101
		</h1>
		<HipTips v-if="!loading && !noData" />

		<div v-if="!loading && !noData">
			<h2>Share Your Results</h2>
			<ion-icon
				name="logo-instagram"
				style="font-size: 35px; fill: grey"
			></ion-icon>
			<ion-icon
				name="logo-facebook"
				style="font-size: 35px; fill: grey"
			></ion-icon>
			<ion-icon
				name="download-outline"
				style="font-size: 35px"
				@click="download()"
			></ion-icon>
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
import img from "../assets/DemoToDownload.png";
import ToggleSwitch from "vuejs-toggle-switch";

export default {
	async mounted() {
		if (this.$route.params.userid) {
			try {
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
				this.loading = false;
				this.isLiveData = "Live";
			} catch (e) {
				this.noData = true;
				this.loading = false;
				this.isLiveData = "Live";
			}
		} else {
			// load demo data
			this.Stats = SampleData;
			this.loading = false;
			this.isLiveData = "Demo";
		}
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
			noData: false,
			isLiveData: "Demo",
			myOptions: {
				layout: {
					color: "black",
					backgroundColor: "#faeae4",
					selectedColor: "white",
					selectedBackgroundColor: "green",
					borderColor: "black",
					fontFamily: "Arial",
					fontWeight: "normal",
					fontWeightSelected: "bold",
					squareCorners: false,
					noBorder: false,
				},
				size: {
					fontSize: 1,
					height: 2,
					padding: 0.3,
					width: 7,
				},
				items: {
					delay: 0.4,
					preSelected: "unknown",
					disabled: false,
					labels: [
						{ name: "Demo", color: "white", backgroundColor: "#4fcbc3" },
						{ name: "Live", color: "white", backgroundColor: "#4fcbc3" },
					],
				},
			},
		};
	},
	methods: {
		scrollDown() {
			window.scrollTo({
				top: this.$refs.highlights.$refs.moreStats.offsetTop,
				behavior: "smooth",
			});
		},
		download() {
			console.log(img);
			var a = document.createElement("a");
			a.href = img;
			a.download = "MainFunder.png";
			a.click();
		},
		async toggleDemoState(newState) {
			this.noData = false;
			console.log(newState);
			if (newState == "Demo") {
				this.loading = false;
				this.Stats = SampleData;
			} else {
				this.loading = true;
				try {
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
					this.loading = false;
				} catch (e) {
					this.noData = true;
				}
			}
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
	width: 250px;
	margin: auto;
	margin-bottom: 10px;
}

.no-data {
	font-size: 30px;
	width: 50vw;
	padding-top: 25vh;
	margin: auto;
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

.demo-toggle {
	width: 130px;
	height: 50px;
	background-color: #ffcbc6;
	position: absolute;
	top: 50px;
	left: 30px;
}
</style>
