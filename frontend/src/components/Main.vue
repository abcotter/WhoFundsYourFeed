<template>
	<div class="main-container">
		<div class="main-header">
			<Header userName="Taylor" />
		</div>
		<div class="main-body">
			<ViewingStats />

			<div class="down-scroll">
				<ion-icon
					name="chevron-down-outline"
					style="font-size: 72px"
				></ion-icon>
			</div>

			<TopStats />

			<div class="mainFooter">
				<ion-icon name="logo-instagram" style="font-size: 35px"></ion-icon>
				<ion-icon name="logo-facebook" style="font-size: 35px"></ion-icon>
				<ion-icon name="download-outline" style="font-size: 35px"></ion-icon>
			</div>
		</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
import Header from "./Header.vue";
import ViewingStats from "./ViewingStats.vue";
import TopStats from "./TopStats.vue";

export default {
	name: "Main",
	components: {
		Header,
		ViewingStats,
		TopStats,
	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main-container {
	margin: 0px;
}

.main-header {
	position: fixed;
	width: 100%;
	backdrop-filter: blur(4px);
}

.main-body {
	padding-top: 140px;
}

.down-scroll {
	padding-bottom: 200px;
}

.mainFooter {
	flex: 3;
	display: flex;
	justify-content: center;
}
</style>
