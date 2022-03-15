<template>
	<div id="wholePage" class="container">
		<Header id="Header"/>

		<div v-if="userId == 'demo'" class="demo-disclaimer">
			Note: you are viewing demo data!
		</div>

		<div v-if="noData" class="no-data">
			hhhm....Looks like we haven't collected viewing data for you yet <br />
			Go watch some
			<a href="http://www.youtube.com" target="_blank" style="color: black"
				>YouTube
			</a>
			and we'll start gathering insights!
		</div>

		<DoubleBounce
			style="margin-top: 30vh"
			v-if="loading && !noData"
		></DoubleBounce>

		<MainFunder :stats="Stats" v-if="!loading" />

		<div class="secondHeader" @click="scrollDown" v-if="!loading">
			<h1>More Viewing Highlights</h1>
			<div class="downScroll">
				<ion-icon
					name="chevron-down-outline"
					style="font-size: 42px"
				></ion-icon>
			</div>
		</div>

		<ViewingHighlights :stats="Stats" ref="highlights" v-show="!loading" />
		<h1 class="section-header" v-show="!loading">Hip Tips: greenwashing 101</h1>
		<HipTips v-if="!loading" />

		<div v-if="!loading">
			<h2>Share Your Results</h2>
			<ion-icon name="logo-instagram" style="font-size: 35px"></ion-icon>
			<ion-icon name="logo-facebook" style="font-size: 35px"></ion-icon>
			<ion-icon name="download-outline" style="font-size: 35px" v-on:click = "downloadVisualReport ()" ></ion-icon>
		</div>
	</div>
</template>

<script>
import Header from "./Header.vue";
import MainFunder from "./MainFunder.vue";
import ViewingHighlights from "./ViewingHighlights.vue";
import HipTips from "./TipsCarousel/HipTips.vue";
import axios from "axios";
import DoubleBounce from "./loader.vue";
import SampleData from "../../../endpointLambdas/reportAnalytics/SampleOutput.json";
import html2canvas from 'html2canvas'

export default {
	async mounted() {
		if (this.$route.params.userid) {
			try {
				this.userId = this.$route.params.userid;
				let url =
					"https://3vor3iykgi.execute-api.us-east-1.amazonaws.com/default/reportAnalytics";
				let body = {
					userId: this.userId,
				};
				const response = await axios({
					url: url,
					method: "POST",
					data: JSON.stringify(body),
				});
				this.Stats = response.data;
				this.loading = false;
			} catch (e) {
				this.noData = true;
			}
		} else {
			// load demo data
			this.Stats = SampleData;
			this.loading = false;
		}
		// for loading nice data - to cut when we have good data in the DB
		this.Stats = SampleData;
	},
	name: "Main",
	components: {
		Header,
		MainFunder,
		ViewingHighlights,
		HipTips,
		DoubleBounce,
	},
	data: function () {
		return {
			Stats: {},
			loading: true,
			userId: "demo",
			noData: false,
		};
	},
	methods: {
		scrollDown() {
			window.scrollTo({
				top: this.$refs.highlights.$refs.moreStats.offsetTop,
				behavior: "smooth",
			});
		},

		/* html2canvas(container,{allowTaint:true})
				.then(function(canvas){
					var link = document.createElement("a");
					document.body.appendChild(link);
					link.download = "html_image.png";
					link.href = canvas.toDataURL("image/png");
					link.target = '_blank';
					link.click();
		}) */
	
		async downloadVisualReport () {
  			let vc = document.getElementById("wholePage")
 		 	let filename = 'something.png'; 
			html2canvas(vc).then(canvas => {  
				vc.saveAs(canvas.toDataURL(), filename);      
			}).catch((error) => {
				alert("Error")
			});
			},

	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
	background-color: #ffcbc6;
}

.demo-disclaimer {
	width: 20%;
	margin: auto;
	position: absolute;
	left: 40%;
	top: 11%;
	margin-bottom: 10px;
	background-color: rgb(79, 203, 195);
	border-radius: 10%;
}

.no-data {
	font-size: 30px;
	width: 50vw;
	padding-top: 25vh;
	margin: auto;
}

.secondHeader {
	margin: auto;
	font-size: 12px;
	color: #292f36;
	margin-top: 15px;
	cursor: pointer;
	width: 400px;
}

h1 {
	margin: 0;
}

.section-header {
	font-size: 45px;
}
</style>
