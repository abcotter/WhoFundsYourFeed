<template>
	<div class="main-funder">
		<div style="display: flex; justify-content: center">
			<h1>Your main funder is:&nbsp;</h1>
			<h2>{{ topFunder }}</h2>
		</div>
		<div class="stats-container">
			<leftStatCard :topFunder="topFunder" />
			<rightStatCard :topFunder="topFunder" />
		</div>
	</div>
</template>

<script>
import leftStatCard from "./MainFunderCards/LeftMainFunderStat.vue";
import rightStatCard from "./MainFunderCards/RightMainFunderStat.vue";

//define components here that can be used elsewhere
export default {
	name: "Funder",
	components: {
		leftStatCard,
		rightStatCard,
	},
	props: ["topFunder"],
};
</script>

<style scoped>
.main-funder {
	display: flex;
	flex-direction: column;
	justify-content: flex-start;
	height: 75vh;
	width: 75%;
	margin: auto;
	background-color: #f5f5f5;
	border-radius: 30px;
	padding: 10px;
}

h1 {
	font-size: 50px;
	color: #292f36;
	display: flex;
	justify-content: center;
}

h2 {
	font-family: Impact, fantasy;
	font-size: 100px;
	color: #292f36;
	font-style: italic;
	margin: 0;
}

.stats-container {
	display: flex;
	height: 58vh;
	justify-content: space-evenly;
}
</style>