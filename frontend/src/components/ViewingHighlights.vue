<template>

    <div class="columns">
		<div class="column1">
			<!--<h2><font color="#292f36">My Viewing Stats</font></h2>-->
			
			<div class="statCard1">
			<div class="statCard1Front">
				<p> Stat 1 Front</p>
			</div>
			<div class="statCard1Back">
				<p> Stat 1 Back </p>
				</div>
			</div>
			

			<div class="influencerCard1">
			<div class="influencerCard1Front">
				<p> Influencer 1 Front</p>
			</div>
			<div class="influencerCard1Back">
				<p> Influencer 1 Back</p>
				</div>
			</div>

			<div class="companyCard2">
				<p> Company 2 </p>
			</div>

			<div class="companyCard2Flipped">
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
	height: 75vh;
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
	display: flex;
}

.statCard1Front{
	flex:1;
	background-color: rgb(247,255,247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
.statCard1Back{
	flex:1;
	background-color: rgb(247,255,247);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
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
	display: flex;
}

.influencerCard1Front{
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
