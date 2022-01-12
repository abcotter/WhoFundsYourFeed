<template>
	<div class="container">
		<div class="mainHeader">
		<h1>Taylor, Who Funds Your Feed?</h1>
		</div>

		<div class="header1">
			<h2>My Viewing Stats</h2>
			</div>

		<div class="header2">
			<h2>Top Brands</h2>
			</div>
		
		<div class="header3">
			<h2>Top Influencers</h2>
			</div>

		<div class="statCard1">
		</div>

		<div class="statCard2">
		</div>

		<div class="companyCard1">
		</div>

		<div class="companyCard2">
		</div>

		<div class="companyCard3">
		</div>

		<div class="influencerCard1">
		</div>

		<div class="influencerCard2">
		</div>

		<div class="influencerCard3">
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
	display: flex;
	padding: 10px;
	justify-content: space-between;
	/*flex-direction: column;*/
	/*align-items: flex-start;*/
}

.mainHeader{
	flex:3; 
}

.header1{
	flex:2;

}

.header2{
	flex:2;

}

.header3{
	flex:2;
}

.statCard1{
	flex:1;
	background-color: blue;
}

.statCard2{
	flex:1;
	background-color: pink;
}

.companyCard1{
	flex:1;
	background-color: red;
}

.companyCard2{
	flex:1; 
	background-color: orange;
	
}
.companyCard3{
	flex: 1;
	background-color:brown;
}

.influencerCard1{
	flex:1;
	background-color:green;
}

.influencerCard2{
	flex:1;
	background-color:blueviolet
	
}

.influencerCard3{
	flex:1;
	background-color:greenyellow;
	
}

.mainFooter{
	flex:3;

}



</style>
