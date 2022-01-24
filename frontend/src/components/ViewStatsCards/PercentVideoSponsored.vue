<template>
	<vue-flip active-click="" transition="2s" class="Card">
		<template v-slot:front class="front"> front </template>
		<template v-slot:back class="back">
			I'm where % of videos you watch that's sponsored goes
		</template>
	</vue-flip>
</template>

<script>
import VueFlip from "vue-flip";
//define components here that can be used elsewhere
export default {
	name: "PercentVideoSponsoredStat",
	components: {
		VueFlip,
	},
};
</script>

<style scoped>
.Card {
	background-color: rgb(255, 230, 109);
	border-radius: 25px;
	padding: 10px;
	margin: 10px;
	height: 350px;
}
</style>