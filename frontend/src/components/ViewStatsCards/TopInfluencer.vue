<template>
	<div class="card">
		<div class="back-text">
			<div class="channel-list">
				<div
					class="channel"
					v-for="(channel, index) in stats.outputTopChannels"
					:key="channel['channelId']"
				>
					<h1 class="number">{{ index + 1 }}</h1>
					<img class="channel-pic" :src="channel['channelImage']" />
					<div class="channel-deets">
						<a
							style="margin: 0; text-align: left"
							:href="`http://www.youtube.com/channel/${channel['channelId']}`"
							target="_blank"
						>
							{{ channel["chanelName"] }}
						</a>
						<p style="margin: 0; text-align: left">
							Subscribers: {{ channel["subCount"] }}
						</p>
						<p style="margin: 0; text-align: left">
							Top Brand Partner:
							{{ channel["top_brand"] }}
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
	border-radius: 25px;
	padding: 10px;
	background-color: rgb(247, 255, 247);
	width: 47vw;
	border: 5px solid #f5f5f5;
	border-radius: 25px;
	margin: auto;
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
.number {
	display: flex;
	justify-content: start;
	margin: 0;
}
.channel-pic {
	max-width: 130px;
	max-height: 130px;
	border-radius: 65px;
	margin-left: 60px;
	margin-top: 10px;
}
.channel-deets {
	display: flex;
	flex-direction: column;
	justify-content: start;
	margin-left: 30px;
	padding-top: 10px;
}
a {
	font-size: 30px;
	color: #292f36;
}
</style>