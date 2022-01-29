<template>
	<div class="columns">
		<div class="column1">
			<PercentTimeSponsoredStat :stats="stats" />
			<PercentVideoSponsoredStat :stats="stats" />
			<YouTopChannels />
		</div>
		<div class="column2">
			<CategoryBreakdown />
			<TopInfluencer :stats="stats" />
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
	props: ["stats"],
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
	display: flex;
	flex-direction: column;
	justify-content: start;
}

.column2 {
	flex: 2;
	margin-right: 10px;
	display: flex;
	flex-direction: column;
	justify-content: start;
}
</style>
