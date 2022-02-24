from bs4 import BeautifulSoup
import os
import re
import requests

YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet"
FILTER_ORGANIZATIONS = set(["ftc"])

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']


def find_video_sponsors(video_id: str, model) -> list:
    """Find sponsor in Youtube videos"""
    result = {}
    sponsorships = []
    description = get_video_description(video_id)
    # If no description found, result includes empty list of sponsors
    if not description:
        result["sponsorships"] = sponsorships
        return result
    disclaimers = find_sponsorship_disclaimers(description)
    sponsorships = find_sponsors_in_disclaimer(disclaimers, model)

    result["sponsorships"] = sponsorships
    result['sponsor_lines'] = disclaimers
    return result

def get_video_description(video_id):
    """Send request to Youtube API and get video description"""

    youtube_api_url = f"{YOUTUBE_API_BASE_URL}&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(youtube_api_url)
    if response.status_code != 200 or not response:
        return ""
    items = response.json().get('items', [])
    description = ''
    if items:
        description = items[0]['snippet']['description']
    return description

def find_sponsorship_disclaimers(description):
    lines = description.split("\n")
    disclaimers = set([])
    for line in lines:
        l = line.lower()
        if "promo code" in l or "code" in l:
            disclaimers.add(l)
        if "sponsor" in l or "sponsored" in l or "thank you to" in l:
            disclaimers.add(l)
    return '. '.join(list(disclaimers))

def remove_duplicate_tokens(tokens: list):
    seen = set()
    deduplicated = []
    for token in tokens:
        if token not in seen:
            deduplicated.append(token)
            seen.add(token)
    return deduplicated

def find_sponsors_in_disclaimer(sentence: str, model):
    links = find_link_in_disclaimer(sentence, model)
    if links:
        return links
    else:
        return find_sponsor_names_in_disclaimer(sentence, model)
    
def find_link_in_disclaimer(sentence, model):
    matches = match_links(sentence)
    sponsors = []
    for link in matches:
        sponsor = match_title_to_domain(link, model)
        if sponsor:
            sponsors.append(sponsor)
    return sponsors

def match_links(sentence):
    matches = re.findall(r'((?:https?://)?www\.[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence)
    if matches:
        return matches
    else:
        return re.findall(r'((?:https?://)[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence)

def find_sponsor_names_in_disclaimer(disclaimer: str, model):
    doc = model(disclaimer)
    sponsors = []
    for ent in doc.ents:
        print('ent label', ent, ent.label_,[t.pos for t in ent])
        if ent.label_ == "ORG" and all([t.pos_ == "PROPN" for t in ent]):
            sponsors.append(ent.text)

    for noun_chunk in doc.noun_chunks:
        if all([t.pos_ == "PROPN" for t in noun_chunk]):
            sponsors.append(noun_chunk.text)
    return [{"name": sponsor.lower(), "url": ""} for sponsor in set(sponsors)]

def match_title_to_domain(url: str, model):
    page = scrape_url(url)
    if not page:
        return {}

    #parse page html
    parser = BeautifulSoup(page.content, 'html.parser')
    title = parser.title
    domain = get_url_domain(page.url)

    #march html title to url domain
    document = model(title.get_text())
    entities = []
    for token in document:
        if token.text.lower() in domain and token.pos_ not in set(['PUNCT', 'ADP', 'DET']):
            entities.append(token.text.lower())
    if entities:
        entities = remove_duplicate_tokens(entities)
        sponsor = ' '.join(entities)
    return {"name": sponsor, "url": url}

def scrape_url(url):
    valid_url = validate_url(url)
    if not valid_url:
        return None
    page = requests.get(valid_url, timeout=50)
    if not page or not page.content or page.status_code == 404:
        print('url not found', valid_url)
        return {"name": " ", "url": " "}
    return page

def validate_url(url):
    return

def get_url_domain(url):
    matches = re.search(r'(?:https?://)?([A-Za-z.]+)', url)
    if matches:
        return matches.group(1)

