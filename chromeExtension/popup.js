document.addEventListener('DOMContentLoaded', () => {
	var y = document.getElementById("index_link");
	y.addEventListener("click", openIndex);
});

function openIndex() {
	userId = localStorage.getItem("userId");
	baseUrl = "http://wfyf-app.s3-website-us-east-1.amazonaws.com/";
	url = userId ? baseUrl + userId : baseUrl;
	chrome.tabs.create({ active: true, url: url });



}
