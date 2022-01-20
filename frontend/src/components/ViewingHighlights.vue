<template>

    <div class="columns">
		<div class="column1">
			<!--<h2><font color="#292f36">My Viewing Stats</font></h2>-->
			<div class="statCard1">
				<p> Stat 1 </p>
			</div>

			<div class="influencerCard1">
				<p> Influencer 1 </p>
			</div>

			<div class="companyCard2">
				<p> Company 2 </p>
			</div>
		</div>

		<div class="column2">
			<!--<h2><font color="#292f36">Top Brands</font></h2>-->
			<div class="companyCard1">
				<p> Company 1 </p>
			</div>

			<div class="statCard2">
				<p> Stat 2 </p>
			</div>

			<div class="influencerCard2">
				<p> Influencer 2</p>
			</div>
		</div>
	</div>

</template>

<script>
export default {
  name: 'Main',
};
</script>

<style scoped>

.columns{
	display: flex;
}

.column1{
	flex: 2;
	margin-right: 10px;
	margin-left: 10px;
}

.column2{
	flex: 2;
	margin-right: 10px;
}

.statCard1{
	background-color: rgb(247,255,247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.statCard2{
	flex:1;
	background-color: rgb(247,255,247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.companyCard1{
	flex:1;
	background-color: rgb(255,230,109);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.companyCard2{
	flex:1; 
	background-color: rgb(255,230,109);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.influencerCard1{
	flex:1;
	background-color:rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.influencerCard2{
	flex:1;
	background-color:rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

</style>
