newUserUrl = "https://ihj75vr267.execute-api.us-east-1.amazonaws.com/default/newUserHandler";
async function getNewUserId(userEmail) {
    body = {'userEmail': userEmail};
    const response = await fetch(newUserUrl, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    console.log('Done processing request');
    return response.json();
};

function _submitHandler() {
    userEmail = document.getElementById("userEmail").value;
    console.log(userEmail);
    getNewUserId(userEmail).then(data => {
        var userIdVal = data['userId'];
        chrome.storage.local.set({userId: userIdVal}, function() {
            console.log('userId is set to ' + userIdVal);
        });
        chrome.storage.local.get(['userId'], function(result) {
            console.log('userId currently is ' + result.userId);
        });
        emailRequest.style.display = "none";
    });
}

function requestEmail() {
    emailRequest = document.getElementById("email");
    chrome.storage.local.get(['userId'], function(result) {
        if ("userId" in result) {
            console.log('user id found');
            emailRequest.style.display = "none";
        }
        else {
            console.log('user id not found');
            emailRequest.style.display = "block";
        }
    });
}
requestEmail();
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submit").onclick = _submitHandler;
});

