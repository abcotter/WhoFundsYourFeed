<template>
	<div class="container">
		<div class="mainHeader">
		<h1><font color="#292f36">Taylor, Who Funds Your Feed?</font></h1>
		</div>

		<div class="mainFunder">
			<div class="funderImage">
				<img src="quavo.jpg"> 
			</div>
			<div class="funderDescription">
				<p>description goes here</p>
				</div>
			</div>
		
		<div class="headers">
		<div class="header1">
			<h2><font color="#292f36">My Viewing Stats</font></h2>
			<div class="statCard1">
				<p> Stat 1 </p>
			</div>

			<div class="statCard2">
				<p> Stat 2 </p>
			</div>
			
		</div>
		<div class="header2">
			<h2><font color="#292f36">Top Brands</font></h2>
			<div class="companyCard1">
				<p> Company 1 </p>
			</div>

			<div class="companyCard2">
				<p> Company 2 </p>
			</div>

			<div class="companyCard3">
				<p> Company 3 </p>
			</div>
		
		</div>
		<div class="header3">
			<h2><font color="#292f36">Top Influencers</font></h2>
			<div class="influencerCard1">
				<p> Influencer 1 </p>
			</div>

			<div class="influencerCard2">
				<p> Influencer 2</p>
			</div>

			<div class="influencerCard3">
				<p> Influencer 3</p>
			</div>
		</div>
	</div>

		<div class="nextSection">
			<h1> next section </h1>

		</div>
		
		<div class="mainFooter">
			<p>Share Your Results</p>
			</div>
		<a
			href="https://github.com/abcotter/WhoFundsYourFeed"
			target="_blank"
			rel="noopener"
			>Repo Link</a
		>
	</div>

	
</template>

<script>
//define components here that can be used elsewhere
export default {
  name: 'Main'
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


.container{
	/*justify-content: ;flex-direction: column;*/
	/*align-items: flex-start;*/
	background-color: rgb(251,220,226);	
}

.mainHeader{
	display: flex;
	justify-content: space-around;
}

.mainFunder{
	display: flex;

}

.funderImage{
	flex: 1;
	
}

.funderDescription{
	flex:1;
	background-color: rgb(247,255,247);
	padding: 50px;
	margin: 10px;
}

.headers{
	display: flex;
	
	
}

.header1{
	flex: 3;
	margin-right: 10px;
	margin-left: 10px;
}

.header2{
	flex: 3;
	margin-right: 10px;
}

.header3{
	flex: 3;
	margin-right: 10px;
}

.statCard1{
	background-color: rgb(247,255,247);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)

}

.statCard2{
	flex:1;
	background-color: rgb(255, 107, 107);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.companyCard1{
	flex:1;
	background-color: rgb(255,230,109);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)

}

.companyCard2{
	flex:1; 
	background-color: rgb(247,255,247);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)

}
.companyCard3{
	flex: 1;
	background-color:rgb(78, 205, 196);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.influencerCard1{
	flex:1;
	background-color:rgb(247,255,247);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)
}

.influencerCard2{
	flex:1;
	background-color:rgb(255, 107, 107);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)
	
}

.influencerCard3{
	flex:1;
	background-color:rgb(247,255,247);
	padding: 5px;
	margin: 5px;
	color: rgb(41, 47, 54)
	
}

.nextSection{
	display: flex;
}

.mainFooter{
	flex:3;

}



</style>
