<template>
	<div class="card">
		<div class="back-text">
			<div class="title">Your Most Watched Channels</div>
			<div class="channel-list">
				<div
					v-for="channel in stats.outputTopChannels"
					:key="channel['channelId']"
				>
					{{ channel["chanelName"] }}
				</div>
			</div>
		</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
export default {
	name: "TopInfluencers",
	props: ["stats"],
};
</script>

<style scoped>
.card {
	margin: 10px;
	height: 40vw;
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
	color: #292f36;
	display: flex;
	justify-content: center;
}

.channel-list {
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
}

a {
	font-size: 30px;
	color: #292f36;
}
</style>