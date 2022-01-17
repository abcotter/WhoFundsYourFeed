from bs4 import BeautifulSoup
import os
import re
import requests
import spacy

YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet"
SOCIAL_MEDIA_DOMAINS = set(['instagram', 'facebook', 'linkedin', 'youtube',
                              'snapchat', 'twitter', 'paypal', 'patreon', 'tiktok',
                              'podcasts.apple', 'flickr'])

HEADERS = {'Access-Control-Allow-Origin': '*',
           'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
	       'Access-Control-Allow-Credentials': 'true',
	       'Content-Type': 'application/json'
           }

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

nlp = spacy.load("en_core_web_sm")

def lambda_handler(event, context):
    userId = event.get('userId')
    videoId = event.get('youtubeVideoId')
    timestamp = event.get('timestamp')
    if not userId or not videoId or not timestamp:
        return {
            'statusCode': 400,
            'headers': HEADERS
        }

    #if video processed return 200

    YOUTUBE_API_URL = f"{YOUTUBE_API_BASE_URL}&id={videoId}&key={YOUTUBE_API_KEY}"
    response = requests.get(YOUTUBE_API_URL)
    if response.status_code != 200 or not response:
        return {
            'statusCode': 500,
            'headers': HEADERS
        }
    items = response.json().get('items', [])
    if items:
        description = items[0]['snippet']['description']
    urls = set()
    matches = re.findall(r'(https?://.*?([a-zA-Z]*).(com|ca|ly))', description)
    for match in matches:
        if match[1] not in SOCIAL_MEDIA_DOMAINS:
            urls.add(match[0])
    sponsor_names = set([])
    for url in urls:
        try:
            page = requests.get(url)
        except Exception as e:
            continue
        if not page.content:
            continue
        parser = BeautifulSoup(page.content, 'html.parser')
        title = parser.title
        print('title', title)
        print('url', url)
        if not title:
            continue
        document = nlp(title.get_text())
        entities = []
        for token in document:
            if token.text.lower() in page.url and token.pos_ not in set(['PUNCT', 'ADP', 'DET']):
                entities.append(token.text)
        sponsor_names.add(' '.join(entities))

    print('Sponsor names', sponsor_names)
    # Call Abi's lambda to pass in sponsor name
    return

if __name__ == "__main__":
    videoIds = ["KDdfv56T16s", "UI6FZVbcd-A"]
    for videoId in videoIds:
        event = {'userId': 1, 'youtubeVideoId': videoId, "timestamp": "blah"}
        context = {}
        print('videId: ', videoId)
        lambda_handler(event, context)

        #if its a shortened link then crawl the whole link
