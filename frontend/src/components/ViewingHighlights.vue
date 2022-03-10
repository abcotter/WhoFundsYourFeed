<template>
	<div class="column" ref="moreStats">
		<div style="position: relative">
			<h1 class="section-header">Percent Of Your WatchTime That's Sponsored</h1>
			<PercentTimeSponsoredStat :stats="stats" />
			<div class="arrow-1">
				<img
					style="height: 200px; width: 200px"
					src="../assets/loopArrow.png"
				/>
				<h1 style="width: 185px; padding-top: 100px; margin: 0px">
					<h1 style="margin: 0px; font-weight: bolder">
						{{ stats.outputTimeSponsored }}%
					</h1>
					of your time on youtube is being sponsored!
				</h1>
			</div>
		</div>
		<div style="position: relative">
			<h1 class="section-header">
				Percent Of Videos You Watched That Are Sponsored
			</h1>
			<PercentVideoSponsoredStat :stats="stats" />
			<div class="arrow-2">
				<h1 style="width: 200px; margin: 0px">
					<h1 style="margin: 0px; font-weight: bolder">
						{{ stats.outputVideoSponsored }}%
					</h1>
					of your videos are sponsored!
				</h1>
				<img
					style="height: 200px; width: 200px; padding-left: 115px"
					src="../assets/swirly-arrow.png"
				/>
			</div>
		</div>
		<div style="position: relative">
			<h1 class="section-header">Your Personal Category Breakdown</h1>
			<CategoryBreakdown :stats="stats" />
			<div class="arrow-1" style="left: 70vw">
				<img
					style="height: 200px; width: 200px; transform: scaleX(-1)"
					src="../assets/scribble.png"
				/>
				<h1 style="width: 220px; margin: 0px">
					WOW! <br />
					you watch a lot of <br />
					<h1 style="margin: 0px; font-weight: bolder">
						{{ topCategory }}
					</h1>
				</h1>
			</div>
		</div>
		<h1 class="section-header">Your Most Watched Channels</h1>
		<TopInfluencer :stats="stats" />
		<h1 class="section-header">Your Most Seen Brands</h1>
		<YourTopBrands :stats="stats" />
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
	data() {
		return {
			topCategory: this.stats.outputTopCategories[0]["video_category"],
		};
	},
	watch: {
		stats() {
			this.topCategory = this.stats.outputTopCategories[0]["video_category"];
		},
	},
};
</script>

<style scoped>
.column {
	display: flex;
	flex-direction: column;
	height: auto;
}

.section-header {
	font-size: 45px;
}

.arrow-1 {
	display: flex;
	position: absolute;
	top: 20vh;
	left: 68vw;
}

.arrow-2 {
	display: flex;
	flex-direction: column;
	position: absolute;
	top: 20vh;
	left: 12vw;
}
</style>
