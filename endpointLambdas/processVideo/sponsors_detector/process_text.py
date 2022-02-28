from bs4 import BeautifulSoup
import os
import re
import requests
from difflib import SequenceMatcher

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
        print('No description found')
        result["sponsorships"] = sponsorships
        return result
    disclaimers = find_sponsorship_disclaimers(description)
    sponsorships = find_sponsors_in_disclaimer(disclaimers, model)
    sponsorships = [s for s in sponsorships if s["name"] not in FILTER_ORGANIZATIONS]
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
            disclaimers.add(line)
        if "sponsor" in l or "sponsored" in l or "thank you to" in l or "partnership" in l or "partner" in l:
            disclaimers.add(line)
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
    sponsor_names = find_sponsor_names_in_disclaimer(sentence, model)
    return links if links else sponsor_names
 

def find_link_in_disclaimer(sentence, model):
    matches = match_links(sentence)
    sponsors = []
    for link in matches:
        sponsor = match_title_to_domain(link, model)
        if sponsor:
            sponsors.append(sponsor)
    return sponsors

def match_links(sentence):
    print('sentence', sentence)
    if re.search(r'((?:https?://)?www\.[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence):
        return re.findall(r'((?:https?://)?www\.[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence)
    elif re.search(r'((?:https?://)[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence):
        return re.findall(r'((?:https?://)[a-zA-Z]+\.[a-zA-z]+(?:/[a-zA-Z0-9]+)?)', sentence)
    elif re.search(r'([a-zA-Z0-9]+\.[a-zA-z]+)', sentence):
        return re.findall(r'([a-zA-Z0-9]+\.[a-zA-z]+)', sentence)
    else:
        return []



def find_sponsor_names_in_disclaimer(disclaimer: str, model):
    doc = model(disclaimer)
    sponsors = []
    for ent in doc.ents:
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
        return {"name": sponsor, "url": page.url}

def scrape_url(url):
    if "http" not in url:
        url = "http://" + url
    #try and match url with no code since links with codes often do not expire.
    # an exception is tiny urls since these require a code to work
    url_no_code_match = re.search('(?:https?:\/\/)?(?:[^\/\n]+)?(?:www\.)?([^:\/?\n]+)', url)
    if "bit" not in url and url_no_code_match:
        url = url_no_code_match.group(0)
    try:
        page = requests.get(url, timeout=10)
    except requests.Timeout as err:
        return None
    if not page or not page.content or page.status_code == 404:
        return None

    return page

def get_url_domain(url):
    matches = re.search(r'(?:https?://)?([A-Za-z.]+)', url)
    if matches:
        return matches.group(1)

