from bs4 import BeautifulSoup
import os
import re
import requests

YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet"
SOCIAL_MEDIA_DOMAINS = set(['instagram', 'facebook', 'linkedin', 'youtube', 'snapchat', 'twitter', 'paypal', 'patreon', 'tiktok',
                            'podcasts.apple', 'flickr', 'soundcloud', 'spotify',
                            'twitch', 'twitter', 'reddit', 'thematic', 'amazon', 'discord', 'epidemic sound'])

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']


def find_video_sponsors(video_id: str, model) -> list:
    """Find sponsor in Youtube videos"""
    result = {}
    sponsorships = []
    youtube_api_url = f"{YOUTUBE_API_BASE_URL}&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(youtube_api_url)
    if response.status_code != 200 or not response:
        return result
    result["youtubeApiResponse"] = response.json()
    description = get_video_description(response)
    if not description:
        result["sponsorships"] = sponsorships
        return result
    urls, sponsored_lines = find_urls(description)
    if not urls:
        result["sponsorships"] = sponsorships
        return result
    scraped_sponsors = scrape_sponsor_websites(urls, model)
    found_sponsor_names = find_sponsors_from_disclaimer(sponsored_lines, model, scraped_sponsors)
    if found_sponsor_names:
        sponsorships = found_sponsor_names
    else:
        sponsorships = [{"name": name.lower(), "url": url} for name, url in scraped_sponsors.items() if name not in SOCIAL_MEDIA_DOMAINS]
    result["sponsorships"] = sponsorships
    result['sponsor_lines'] = sponsored_lines
    return result

def find_sponsors_from_disclaimer(lines, model, scraped_sponsors):
    """
    if there are brand names then they should be cross referenced against
    scraping to match against urls
    ["brand name"] {"name": "brand_name", "url":"url}

    if iob is B start  then once its O stop a dding 


    go through each entity and add tokens if every token is proper noun and entity is org
    go through each noun chunk and add token if every token is proper noun
    iterate through matched sponsors


    """
    print('scraped sponsors', scraped_sponsors)
    entities = set()
    sponsors = []
    for line in lines:
        print("Processing line: ",line)
        doc = model(line)
        for ent in doc.ents:
            print(ent, ent.label_, [t.pos_ == "PROPN" for t in ent])
            if ent.label_ == "ORG" and all([t.pos_ == "PROPN" for t in ent]):
                entities.add(ent.text.lower())

        for noun_chunk in doc.noun_chunks:
            print(noun_chunk, [t.pos_ == "PROPN" for t in noun_chunk])
            if all([t.pos_ == "PROPN" for t in noun_chunk]):
                entities.add(noun_chunk.text.lower())
    print("entities", entities)
    for entity in entities:
        url = scraped_sponsors.get(entity)
        sponsors.append({"name": entity, "url": url})

    return sponsors

def get_video_description(youtube_api_response):
    """Send request to Youtube API to get video description"""

    items = youtube_api_response.json().get('items', [])
    description = ''
    if items:
        description = items[0]['snippet']['description']
    return description

def find_urls(description: str) -> set:
    """Find urls specifide in video description"""
    urls = set()
    description = description.split('\n')
    sponsored_lines = []
    for line in description:
        matches = re.findall(r'(https?://.*?([a-zA-Z]*).([a-zA-Z]+)[^ ]*)', line)
        for match in matches:
            if match[1] not in SOCIAL_MEDIA_DOMAINS:
                urls.add(match[0])
        if "sponsor" in line.lower() or "sponsored" in line.lower() or "sponsors" in line.lower():
            sponsored_lines.append(line)
    return urls, sponsored_lines

def get_html_content(url):
    # matches = re.search('(https?://.*?([a-zA-Z]*).([a-zA-Z]{2}))', url)
    matches = re.search('(?:https?:\/\/)?(?:[^\/\n]+)?(?:www\.)?([^:\/?\n]+)', url)
    print(url, matches.group(0))
    page_url = matches.group(0) if matches else url
    print(f'original url {url} page url: {page_url}')
    page = requests.get(page_url, timeout=30)
    if not page or not page.content or page.status_code == 404:
        print(f'Falling back to original url {url} ')
        print({"page": page,
               "page status_code": page.status_code})
        page = requests.get(url, timeout=30)
    return page
def remove_duplicate_tokens(tokens: list):
    seen = set()
    deduplicated = []
    for token in tokens:
        if token not in seen:
            deduplicated.append(token)
            seen.add(token)
    return deduplicated



def cross_reference_brand_names(detected_sponsors, entities):
    """
    entities: ["hellofresh & some", "neiwei, "man scaped]
    detected_sponsors: ["neiwei", "createive", "man scaped", hellofresh]

    """
    if not entities:
        return detected_sponsors
    cross_ref_sponsors = []
    for sponsor in detected_sponsors:
        tokens = [s.lower() for s in sponsor["name"].split(" ")]
        print("tokens", tokens)
        print("entities", entities)
        intersection = [token for token in tokens if token in entities]
        name = ' '.join(intersection)
        if intersection:
            cross_ref_sponsors.append({"name": name, "url": sponsor["url"]})

    print("Cross referenced sponsors", cross_ref_sponsors)
    return cross_ref_sponsors if cross_ref_sponsors else detected_sponsors

def scrape_sponsor_websites(urls: list, model):
    """Scrape urls and extract business name from website title"""
    """
    we probably want to check links that don't include the code first and then
    if they don't return anything or return an error then we can check the full url

    """
    sponsors = set()
    for i, url in enumerate(urls):
        print(f"processssing {i} of {len(urls)}")
        try:
            page = get_html_content(url)
        except Exception as e:
            print(f'Exception at url {url}')
            continue
        parser = BeautifulSoup(page.content, 'html.parser')
        title = parser.title
        matches = re.search('(https?://.*?([a-zA-Z]*).(com|ca))', page.url)
        page_url = matches.group(0) if matches else page.url
        domain = matches.group(2) if matches else page.url
        if not title:
            continue
        document = model(title.get_text())
        entities = []
        for token in document:
            if token.text.lower() in domain and token.pos_ not in set(['PUNCT', 'ADP', 'DET']):
                entities.append(token.text.lower())
        entities = remove_duplicate_tokens(entities)
        if entities:
            sponsors.add((' '.join(entities), page_url))
    return {name: url for name, url in sponsors}
