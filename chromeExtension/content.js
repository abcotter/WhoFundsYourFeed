var past_url = '';
var processVideoUrl = 'https://6827rdxni0.execute-api.us-east-1.amazonaws.com/v1/processVideoTest';
// mutation observer will invoke the clalback function
// when the specified dom elements update

function getVideoId(url) {
    const youtubeRegex = /https:\/\/www\.youtube.com\/watch\?v=([-a-zA-Z0-9_]+)/;
    const videoIdMatch = url.match(youtubeRegex)[1];
    return videoIdMatch;
}


function getCurrentTimeStamp() {
    const currentDate = new Date();
    const hours = currentDate.getHours();
    const minutes = currentDate.getMinutes();
    const seconds = currentDate.getSeconds();
    const timeStamp = hours + ":" + minutes + ":" + seconds;

    const currentDayOfMonth = currentDate.getDate();
    const currentMonth = currentDate.getMonth(); 
    const currentYear = currentDate.getFullYear();

    const dateTime = currentYear + "-" + (currentMonth + 1) + "-" + currentDayOfMonth + " " + timeStamp;
    return dateTime;
}

async function processWatchedVideo(body) {
    const response = await fetch(processVideoUrl, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    console.log('Done processing video');
    console.log(body);
    return response.json();
};

function sendWatchEvent() {
    chrome.storage.local.get(['userId'], function(result) {
        var videoId = getVideoId(location.href);
        var userId = result.userId;
        var timeStamp = getCurrentTimeStamp();
        body = {'userId': userId, 'youtubeVideoId': videoId, 'timestamp': timeStamp};
        processWatchedVideo(body).then(data => {
            console.log(data);
        });
    });

}
var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
        if (location.href != past_url) {
            past_url = location.href;
            if (location.href.startsWith("https://www.youtube.com/watch?v=")) {
                sendWatchEvent();
            }
        }
    });
});
observer.observe(document.documentElement, {childList: true, subtree: true});
