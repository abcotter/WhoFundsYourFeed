<template>

    <div class="columns">
		<div class="column1">
			<!--<h2><font color="#292f36">My Viewing Stats</font></h2>-->
			
			<div class="statCard1">
			<div class="statCard1Content statCard1Front">
				<p> Stat 1 Front</p>
			</div>
			<div class="card-body">
				<p> t </p>
				</div>
			<div class="statCard1Content statCard1Back">
				<p> Stat 1 Back</p>
				</div>
				<div class="card-body">
					<p> t </p>
				</div>
			</div>

			<div class="influencerCard1">
			<div class="influencerCard1Content influencerCard1Front">
				<p> Influencer 1 Front</p>
			</div>
			<div class="card-body">
				<p> h </p>
			</div>
			<div class="influencerCard1Content influencerCard1Back">
				<p> Influencer 1 Back</p>
				</div>
				<div class="card-body">
					<p>t</p>
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
	justify-content: space-evenly;
	height: 75vh;
	width: 100%;
}

.column1{
	width: 45%
}

.column2{
	width: 45%;
}
.statCard1{
	display: flex;
	perspective: 1000px;
	position: relative;
}
.statCard1Content{ 
	box-shadow: 0 1rem 1Srem rgba(0,0,0,.5);
	transition: all 1s;
	position: absolute;
	top:0;
	left:0;
	width: 100%;
	backface-visibility: hidden;
	-webkit-backface-visibility: hidden;
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
	transform:rotateY(180deg);
}
.statCard1:hover .statCard1Front{ 
	transform: rotateY(-180deg);
}
.statCard1:hover .statCard1Back{
	transform: rotateY(0);
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
	perspective: 1000px;
	position: relative;
}
.influencerCard1Content{ 
	box-shadow: 0 1rem 1Srem rgba(0,0,0,.5);
	transition: all 1s;
	position: absolute;
	top:0;
	left:0;
	width: 100%;
	backface-visibility: hidden;
	-webkit-backface-visibility: hidden;
}
.influencerCard1Front{
	flex:1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
}
.influencerCard1Back{
	flex:1;
	background-color: rgb(255, 107, 107);
	border-radius: 25px;
	padding: 10px;
	margin: 5px;
	color: rgb(41, 47, 54);
	transform:rotateY(180deg);
	
}
.influencerCard1:hover .influencerCard1Front{ 
	transform: rotateY(-180deg);
}
.influencerCard1:hover .influencerCard1Back{
	transform: rotateY(0);
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
