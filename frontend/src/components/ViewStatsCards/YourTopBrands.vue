<template>
	<div class="card">
		<div class="back">
			<div class="back-text">
				<div class="brand-list">
					<div
						class="brand"
						v-for="(brand, index) in stats.outputFrequentCompanies"
						:key="brand['brand_name']"
					>
						<h1 class="number">{{ index + 1 }}</h1>

						<div class="brand-deets">
							<a
								style="margin: 0; text-align: left"
								:href="brand['brand_url']"
								target="_blank"
							>
								{{ brand["brand_name"] }}
							</a>
							<a
								style="color: black; font-size: 20px"
								:href="
									'https://www.youtube.com/results?search_query=' +
									stats.outputFrequentCompanies[index]['brand_name'] +
									' review'
								"
								target="_blank"
							>
								See reviews for
								{{ stats.outputFrequentCompanies[index]["brand_name"] }}</a
							>
							<p style="margin: 0; text-align: left">
								Videos Sponsored: {{ brand["video_count"] }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "TopBrandsStat",
	props: ["stats"],
};
</script>

<style scoped>
.card {
	margin: auto;
	margin-bottom: 30px;
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

.back {
	width: 50vw;
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
}

.brand-list {
	padding-top: 20px;
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
}
.brand {
	margin-bottom: 20px;
	width: 100%;
	display: flex;
	justify-content: start;
}
.number {
	display: flex;
	justify-content: start;
	margin: 0;
}

.brand-deets {
	display: flex;
	flex-direction: column;
	justify-content: start;
	margin-left: 30px;
	padding-top: 10px;
}
.brand-pic {
	max-width: 130px;
	max-height: 130px;
	border-radius: 65px;
	margin-left: 60px;
	margin-top: 10px;
}
a {
	font-size: 30px;
	color: #292f36;
}
</style>