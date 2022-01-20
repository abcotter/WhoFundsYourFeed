<template>
	<div class="viewing-stats-container">
		<div class="mainFunder">
			<div class="funderImage">
				<img src="quavo.jpg" />
			</div>
			<div class="funderDescription">
				<h1>Your main funder is Quavo</h1>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "MainFunder",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.viewing-stats-container {
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

.mainFunder {
	display: flex;
	height: 80vh;
}

.down-scroll {
	padding-bottom: 200px;
}

.funderImage {
	flex: 1;
	width: 100%;
	padding: 325px;
}

.funderDescription {
	flex: 1;
	background-color: rgb(247, 255, 247);
	border-radius: 30px;
	padding: 150px;
	margin: 10px;
}
</style>
