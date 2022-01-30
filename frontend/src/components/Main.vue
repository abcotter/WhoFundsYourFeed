<template>
	<div class="container">
		<img class="blue-circle" src="../assets/blue_circ.png" alt="blue circle" />
		<img class="yellow-bar" src="../assets/yell_bar.png" alt="yellow bar" />
		<img class="peace-sign" src="../assets/peace.png" alt="peace sign" />

		<Header userName="Taylor" />

		<MainFunder :stats="Stats" />

		<div class="downScroll">
			<ion-icon name="chevron-down-outline" style="font-size: 72px"></ion-icon>
		</div>

		<div class="secondHeader">
			<h1><font color="#292f36"> More Viewing Highlights</font></h1>
		</div>

		<ViewingHighlights :stats="Stats" />

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

export default {
	mounted() {
		// todo call Fatimahs API and get real data
		this.Stats = {
			outputTimeSponsored: 75,
			outputVideoSponsored: 53,
			outputFrequentCompanies: ["HelloFresh", "Native", "Audible"],
			outputChannelSponsors: [
				"channelSponsorOne",
				"channelSponsorTwo",
				"channelSponsorThree",
				"channelSponsorFour",
				"channelSponsorFive",
			],
			outputTopCategories: ["How to & Style"],
		};
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
	background-color: #ffcbc6;
}

.blue-circle {
	position: absolute;
	max-width: 20vw;
	max-height: 20vh;
	top: 16vh;
	left: 7vw;
}

.yellow-bar {
	position: absolute;
	top: 16vh;
	right: 5vw;
	max-width: 8vw;
	max-height: 85vh;
}

.peace-sign {
	position: absolute;
	top: 8vh;
	right: 13vw;
	max-width: 10vw;
	max-height: 20vh;
}
</style>
