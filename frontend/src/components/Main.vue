<template>
	<div class="container">
		<Header userName="Taylor" />

		<MainFunder topFunder="HelloFresh" />

		<div class="downScroll">
			<ion-icon name="chevron-down-outline" style="font-size: 72px"></ion-icon>
		</div>

		<div class="secondHeader">
			<h1><font color="#292f36"> More Viewing Highlights</font></h1>
		</div>

		<ViewingHighlights />

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
	name: "Main",
	components: {
		Header,
		MainFunder,
		ViewingHighlights,
	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
	background-color: rgb(251, 220, 226);
}
</style>
