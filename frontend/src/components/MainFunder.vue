<template>
	<div class="main-funder">
		<div style="display: flex; justify-content: center">
			<h1>Your main funder is:&nbsp;</h1>
			<div
				style="display: flex; flex-direction: column; justify-content: flex-end"
			>
				<a
					class="brand-name"
					:href="stats.outputFrequentCompanies[0]['brand_url']"
					target="_blank"
				>
					{{ stats.outputFrequentCompanies[0]["brand_name"] }}
				</a>
				<div>
					<a
						style="float: right; color: black"
						:href="
							'https://www.youtube.com/results?search_query=' +
							stats.outputFrequentCompanies[0]['brand_name'] +
							' review'
						"
						target="_blank"
					>
						See reviews for
						{{ stats.outputFrequentCompanies[0]["brand_name"] }}</a
					>
				</div>
			</div>
		</div>
		<div class="stats-container">
			<leftStatCard
				:topFunder="stats.outputFrequentCompanies[0]['brand_name']"
				:stats="stats"
			/>
			<rightStatCard
				:topFunder="stats.outputFrequentCompanies[0]['brand_name']"
				:stats="stats"
			/>
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
	props: ["stats"],
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
	background-color: rgb(247, 255, 247, 0.6);
	border: 5px solid rgba(243, 243, 243, 0.65);
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

.brand-name {
	font-family: Impact, fantasy;
	font-size: 100px;
	color: #292f36;
	font-style: italic;
	margin: 0;
	float: right;
}

.stats-container {
	display: flex;
	height: 58vh;
	justify-content: space-evenly;
}
</style>