<template>
	<div class="Card">
		<div>What percent of you content sponsored?</div>
		<div>I'm where % of videos you watch that's sponsored goes</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
export default {
	name: "PercentVideoSponsoredStat",
};
</script>

<style scoped>
.Card {
	background-color: rgb(255, 230, 109);
	border-radius: 25px;
	padding: 10px;
	margin: 10px;
	height: 350px;
	transition: transform 1s;
	transform-style: preserve-3d;
	cursor: pointer;
}
</style>