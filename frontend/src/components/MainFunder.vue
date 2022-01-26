<template>

    <div class="mainFunder">
			<!--<div class="funderImage">
				<img src="frontend\src\assets\quavo.jpg"> 
			</div>-->
			<div class="funderDescription">
				<h1><font color="#292f36">Your main funder is Quavo</font></h1>
                <div class="funderCard1">
                    <p>card 1</p>
                </div>
                <div class="funderCard2">
                    <p>card 2</p>
                    <PieChart />
                </div>
            </div>
    </div>
</template>

<script>
//define components here that can be used elsewhere
import PieChart from "./PieChart.vue";
export default {
  name: 'Main',
  components: {
    PieChart,
  }
};


</script>

<style scoped>

.mainFunder{
	display: flex;
    height: 75vh;
}

/*.funderImage{
	flex: 1;
	width: 100%;
	padding: 325px;
}*/

.funderDescription{
	flex:1;
	background-color: rgb(78, 205, 196);
	border-radius: 30px;
	padding: 200px;
	margin: 10px;
}

.funderCard1{
    background-color: rgb(247,255,247);
    border-radius: 25px;
    padding: 10px;
    margin: 10px;
}

.funderCard2{
    background-color: rgb(247,255,247);
    border-radius: 25px;
    padding: 10px;
    margin: 10px;

}

</style>