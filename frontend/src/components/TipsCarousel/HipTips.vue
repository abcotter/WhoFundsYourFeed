<template>
	<div class="card">
		<div class="back-text">
			<agile ref="carousel" :dots="false" :navButtons="false">
				<img style="object-fit: cover" src="./GreenwashingSlide1.png" />
				<img style="object-fit: cover" src="./GreenwashingSlide2.png" />
				<img style="object-fit: cover" src="./GreenwashingSlide3.png" />
				<img style="object-fit: cover" src="./GreenwashingSlide4.png" />
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
			<div>
				see more tips at
				<a
					href="https://ecogreenlove.com/2021/03/18/avoid-greenwashing/"
					target="_blank"
					>ecogreenlove
				</a>
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
	margin: auto;
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
	height: 430px;
}
</style>