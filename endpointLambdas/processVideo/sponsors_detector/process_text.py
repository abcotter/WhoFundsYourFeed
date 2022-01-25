from bs4 import BeautifulSoup
import os
import re
import requests

YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet"
SOCIAL_MEDIA_DOMAINS = set(['instagram', 'facebook', 'linkedin', 'youtube',
                              'snapchat', 'twitter', 'paypal', 'patreon', 'tiktok',
                              'podcasts.apple', 'flickr', 'soundcloud', 'spotify'])

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']


def find_video_sponsors(video_id: str, model) -> list:
    """Find sponsor in Youtube videos"""
    result = {}
    sponsorships = []
    youtube_api_url = f"{YOUTUBE_API_BASE_URL}&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(youtube_api_url)
    if response.status_code != 200 or not response:
        return result
    description = get_video_description(response)
    urls = find_urls(description)
    if urls:
        sponsorships = scrape_sponsor_websites(urls, model)
    result["sponsorships"] = sponsorships
    result["youtubeApiResponse"] = response.json()
    return result

def get_video_description(youtube_api_response):
    """Send request to Youtube API to get video description"""

    items = youtube_api_response.json().get('items', [])
    if items:
        description = items[0]['snippet']['description']
    return description

def find_urls(description: str) -> set:
    """Find urls specifide in video description"""
    urls = set()
    matches = re.findall('(https?://.*\.ly[^ ]*)', description)
    for match in matches:
        urls.add(match)

    matches = re.findall(r'(https?://.*?([a-zA-Z]*).(com|ca)[^ ]*)', description)
    for match in matches:
        if match[1] not in SOCIAL_MEDIA_DOMAINS:
            urls.add(match[0])
    return urls

def scrape_sponsor_websites(urls: list, model):
    """Scrape urls and extract business name from website title"""
    sponsors = set()
    for url in urls:
        try:
            page = requests.get(url)
        except Exception as e:
            continue
        if not page.content:
            continue
        parser = BeautifulSoup(page.content, 'html.parser')
        title = parser.title
        matches = re.search('(https?://.*?([a-zA-Z]*).(com|ca))', page.url)
        page_url = matches.group(0) if matches else page.url
        domain = matches.group(2) if matches else page.url
        if not title:
            continue
        document = model(title.get_text())
        entities = set()
        for token in document:
            if token.text.lower() in domain and token.pos_ not in set(['PUNCT', 'ADP', 'DET']):
                entities.add(token.text)
        if entities:
            sponsors.add((' '.join(entities), url))
    return [{"name": name, "url": page_url} for name, url in sponsors]


