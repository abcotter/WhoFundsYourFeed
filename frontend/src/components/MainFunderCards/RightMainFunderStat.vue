<template>
	<div class="funder-card">
		<div class="channel-list">
			<div
				class="channel"
				v-for="(channel, index) in stats.outputFunderChannels"
				:key="channel['channelId']"
			>
				<h1 class="number">{{ index + 1 }}</h1>
				<img class="channel-pic" :src="channel['channelImage']" />
				<div class="channel-deets">
					<a
						style="margin: 0; text-align: left"
						:href="`http://www.youtube.com/channel/${channel['channelId']}`"
					>
						{{ channel["channelName"] }}
					</a>
					<p style="margin: 0; text-align: left; font-size: 25px">
						Subscribers: {{ channel["subCount"] }}
					</p>
				</div>
			</div>
		</div>
		<div class="arrow-right">
			<img
				style="height: 300px; width: 300px; transform: ScaleX(-1)"
				src="../../assets/ARROW_RIGHT.png"
			/>
			<div style="position: relative">
				<h1
					style="
						width: 200px;
						font-size: 25px;
						margin: 0px;
						position: absolute;
						left: 9vw;
						top: -9vh;
					"
				>
					These are the channels who work with {{ topFunder }} the most!
				</h1>
			</div>
		</div>
	</div>
</template>

<script>
//define components here that can be used elsewhere
export default {
	name: "RightMainFunderStat",
	props: ["topFunder", "stats"],
	methods: {},
};
</script>

<style scoped>
.funder-card {
	margin: 10px;
	width: 40%;
	height: 90%;
	background-color: #4fccc4;
	border: 5px solid #83d3cd;
	border-radius: 25px;
	padding: 20px;
}

.content-flipper {
	width: 100%;
	height: 100%;
	transition: ease-in 300ms;
	transform-style: preserve-3d;
	cursor: pointer;
}

.back {
	border-radius: 25px;
	padding: 10px;
	background-color: #4fccc4;
	border: 5px solid #83d3cd;
	position: absolute;
	width: 100%;
	height: 100%;
	margin: auto;
	justify-content: center;
	align-items: center;
	font-size: 20px;
	color: #292f36;
	display: flex;
	padding: 20px;
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
	height: 20%;
	margin-bottom: 20px;
	width: 100%;
	display: flex;
	justify-content: start;
}

.number {
	display: flex;
	justify-content: start;
	margin: 0;
	font-size: 30px;
}

.channel-pic {
	width: 130px;
	height: 130px;
	border-radius: 65px;
	margin-left: 10px;
	margin-top: 10px;
}

.channel-deets {
	display: flex;
	flex-direction: column;
	justify-content: start;
	margin-left: 20px;
	padding-top: 10px;
}

a {
	font-size: 35px;
	color: #292f36;
}

.arrow-right {
	position: absolute;
	top: 30vh;
	right: 5vw;
}
</style>