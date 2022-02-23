<template>
	<div class="column" ref="moreStats">
		<h1>Percent Of Your WatchTime That's Sponsored</h1>
		<PercentTimeSponsoredStat :stats="stats" />
		<h1>Percent Of Videos That Are Sponsored</h1>
		<PercentVideoSponsoredStat :stats="stats" />
		<h1>Your Personal Category Breakdown</h1>
		<CategoryBreakdown :stats="stats" />
		<h1>Your Most Watched Channels</h1>
		<TopInfluencer :stats="stats" />
		<h1>Your Most Seen Brands</h1>
		<YourTopBrands />
	</div>
</template>

<script>
import PercentTimeSponsoredStat from "./ViewStatsCards/PercentTimeSponsored.vue";
import PercentVideoSponsoredStat from "./ViewStatsCards/PercentVideoSponsored.vue";
import TopInfluencer from "./ViewStatsCards/TopInfluencer.vue";
import CategoryBreakdown from "./ViewStatsCards/CategoryBreakdown.vue";
import YourTopBrands from "./ViewStatsCards/YourTopBrands.vue";

export default {
	name: "ViewingStats",
	components: {
		CategoryBreakdown,
		PercentTimeSponsoredStat,
		PercentVideoSponsoredStat,
		TopInfluencer,
		YourTopBrands,
	},
	props: ["stats"],
};
</script>

<style scoped>
.column {
	display: flex;
	flex-direction: column;
	height: auto;
}
</style>
