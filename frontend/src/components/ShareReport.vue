<template>
<!-- <Header id="Header" /> -->
<div>
<Header id="mainFunder" />
<!--MainFunder /-->
</div>
</template>
<script>
import Header from "./Header.vue";
//import MainFunder from "./MainFunder.vue";
//import ViewingHighlights from "./ViewingHighlights.vue";

export default {
    props:["stats"],
	name: "shareReport",
	components: {
		Header,
		//MainFunder,
		//ViewingHighlights,
	}
}
</script>

