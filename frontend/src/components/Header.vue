<template>
	<div class="mainHeader">{{ userName }}, Who Funds Your Feed?</div>
</template>

<script>
export default {
	name: "Header",
	props: ["userName"],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mainHeader {
	padding: 30px;
	height: 80px;
	display: flex;
	justify-content: center;
	color: #292f36;
	font-size: 70px;
	font-weight: bold;
}
</style>
