<template>
	<div class="card">
		<div class="back-text">
			<div class="title">Hip Tips</div>
			<agile ref="carousel" :dots="false" :navButtons="false">
				<div class="slide">1</div>
				<div class="slide">2</div>
			</agile>
			<div style="display: flex; width: 100%; justify-content: space-between">
				<ion-icon
					name="chevron-back-outline"
					style="font-size: 72px; cursor: pointer"
					@click="$refs.carousel.goToPrev()"
				/>
				<ion-icon
					name="chevron-forward-outline"
					style="font-size: 72px; cursor: pointer"
					@click="$refs.carousel.goToNext()"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import { VueAgile } from "vue-agile";

//define components here that can be used elsewhere
export default {
	name: "HipTips",
	components: {
		agile: VueAgile,
	},
};
</script>

<style scoped>
.card {
	margin: 10px;
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	width: 47vw;
	border: 5px solid #f5f5f5;
	border-radius: 25px;
}

.back-text {
	height: 90%;
	width: 90%;
	margin: auto;
	align-items: center;
	font-size: 20px;
	color: #292f36;
	display: flex;
	flex-direction: column;
	padding: 10px;
}

.title {
	font-size: 50px;
	font-weight: bold;
	color: #292f36;
	display: flex;
	justify-content: center;
}

.agile {
	width: 90%;
	border-radius: 10px;
}
</style>