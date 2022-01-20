<template>
	<div class="top-stats-container">
		<div class="main-header">Your Top Brands and Influencers</div>
		<div class="headers">
			<div class="header2">
				<h2><font color="#292f36">Top Brands</font></h2>
				<div class="companyCard1">
					<p>Company 1</p>
				</div>

				<div class="companyCard2">
					<p>Company 2</p>
				</div>

				<div class="companyCard3">
					<p>Company 3</p>
				</div>
			</div>
			<div class="header3">
				<h2><font color="#292f36">Top Influencers</font></h2>
				<div class="influencerCard1">
					<p>Influencer 1</p>
				</div>

				<div class="influencerCard2">
					<p>Influencer 2</p>
				</div>

				<div class="influencerCard3">
					<p>Influencer 3</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "ViewingStats",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.top-stats-container {
	margin: auto;
	margin-bottom: 10px;
	width: 97%;
	height: 80vh;
	background-color: #ffcbc6;
	border-radius: 30px;
}
.main-header {
	padding-left: 30px;
	padding-top: 10px;
	height: 80px;
	display: flex;
	justify-content: left;
	color: #292f36;
	font-size: 50px;
	font-weight: bold;
}

.headers {
	display: flex;
}

.header1 {
	flex: 3;
	margin-right: 10px;
	margin-left: 10px;
}

.header2 {
	flex: 3;
	margin-right: 10px;
}

.header3 {
	flex: 3;
	margin-right: 10px;
}

.statCard1 {
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.statCard2 {
	flex: 1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.companyCard1 {
	flex: 1;
	background-color: rgb(255, 230, 109);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.companyCard2 {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
.companyCard3 {
	flex: 1;
	background-color: rgb(78, 205, 196);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.influencerCard1 {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.influencerCard2 {
	flex: 1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}

.influencerCard3 {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
</style>