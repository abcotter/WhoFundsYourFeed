<template>
	<div class="card">
		<div class="back-text">
			<div class="title">Your Most Watched Channels</div>
			<div class="channel-list">
				<div
					class="channel"
					v-for="(channel, index) in stats.outputTopChannels"
					:key="channel['channelId']"
				>
					<h1>{{ index + 1 }}</h1>
					<img
						style="
							max-width: 120px;
							max-height: 120px;
							border-radius: 60px;
							margin-left: 60px;
						"
						:src="channel['channelImage']"
					/>
					<div
						style="
							display: flex;
							flex-direction: column;
							justify-content: start;
							margin-left: 30px;
						"
					>
						<h1 style="margin: 0">
							{{ channel["chanelName"] }}
						</h1>
						<p style="margin: 0">
							Subscriber count : {{ channel["subCount"] }}
						</p>
					</div>
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
	padding-top: 20px;
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
}

.channel {
	margin-bottom: 20px;
	width: 100%;
	display: flex;
	justify-content: start;
}

a {
	font-size: 30px;
	color: #292f36;
}
</style>