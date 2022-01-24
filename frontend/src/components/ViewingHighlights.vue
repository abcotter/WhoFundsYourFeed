<template>
	<div class="columns">
		<div class="column1">
			<PercentTimeSponsoredStat />
			<PercentVideoSponsoredStat />
			<YouTopChannels />
		</div>
		<div class="column2">
			<CategoryBreakdown />
			<TopInfluencer />
		</div>
	</div>
</template>

<script>
import PercentTimeSponsoredStat from "./ViewStatsCards/PercentTimeSponsored.vue";
import PercentVideoSponsoredStat from "./ViewStatsCards/PercentVideoSponsored.vue";
import TopInfluencer from "./ViewStatsCards/TopInfluencer.vue";
import CategoryBreakdown from "./ViewStatsCards/CategoryBreakdown.vue";
import YouTopChannels from "./ViewStatsCards/YourTopChannels.vue";

export default {
	name: "ViewingStats",
	components: {
		CategoryBreakdown,
		PercentTimeSponsoredStat,
		PercentVideoSponsoredStat,
		TopInfluencer,
		YouTopChannels,
	},
};
</script>

<style scoped>
.columns {
	display: flex;
}

.column1 {
	flex: 2;
	margin-right: 10px;
	margin-left: 10px;
}

.column2 {
	flex: 2;
	margin-right: 10px;
}

.statCard1 {
	display: flex;
}

.statCard1Front {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
.statCard1Back {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.statCard2 {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.companyCard1 {
	flex: 1;
	background-color: rgb(255, 230, 109);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.companyCard2 {
	flex: 1;
	background-color: rgb(255, 230, 109);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.influencerCard1 {
	display: flex;
}

.influencerCard1Front {
	flex: 1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.influencerCard2 {
	flex: 1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
</style>
