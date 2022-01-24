<template>
	<div class="main-funder">
		<div style="display: flex; justify-content: center">
			<h1>Your most funder is:&nbsp;</h1>
			<h2>{{ topFunder }}</h2>
		</div>
		<div class="stats-container">
			<leftStatCard />
			<rightStatCard />
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
	background-color: rgb(78, 205, 196);
	border-radius: 30px;
	padding: 10px;
	margin-left: 10px;
	margin-right: 10px;
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
	height: 80%;
	justify-content: space-evenly;
}

.funderCard2 {
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 10px;
}
</style>