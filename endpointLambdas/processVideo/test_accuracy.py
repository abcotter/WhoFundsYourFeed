from sponsors_detector.process_text import (find_sponsors_in_disclaimer,
                                            match_title_to_domain,
                                            get_video_description,
                                            find_sponsor_names_in_disclaimer)
import json
import spacy
import requests
import os

YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics"
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

def test_detect_possible_sponsors():
    model = spacy.load('en_core_web_sm')
    with open('test_data/disclaimers.json') as f:
        data = json.load(f)
    recall_metric = []
    precision_metric = []
    results = []
    for d in data:
        disclaimer = d['disclaimer']
        sponsors = [s.lower() for s in d['sponsors']]
        try:
            predicted = find_sponsor_names_in_disclaimer(disclaimer, model)
        except Exception as e:
            print('disclaimer not working', disclaimer)
            print(e)
            continue
        predicted = [s["name"] for s in predicted]
        correct_sponsors = set(sponsors).intersection(predicted)
        precision = 0.0 if len(predicted) == 0 else len(correct_sponsors)/len(predicted)
        precision_metric.append(precision)
        recall = len(correct_sponsors)/len(sponsors)
        recall_metric.append(recall)
        result = {"video_id": d["video_id"],
                  "disclaimer": disclaimer,
                  "actual sponsors": sponsors,
                  "predicted": list(predicted),
                  "precision": precision,
                  "recall": recall}
        results.append(result)
        print(json.dumps(result, indent=4))
    average_p = sum(precision_metric)/len(precision_metric)
    average_r = sum(recall_metric)/len(recall_metric)
    print('Average precision', average_p)
    print('Average recall', average_r)

def test_match_title_to_domain():
    """
    when testing functionality:
    cant reach, no code, bit link

    """
    model = spacy.load('en_core_web_sm')
    with open('test_data/links.json') as f:
        data = json.load(f)
    accuracies = 0.0

    for d in data:
        url = d["url"]
        sponsor = d["sponsor"]
        predicted = match_title_to_domain(url, model)
        if not predicted:
            print('No sponsor detecte when sponsor is: ', sponsor)
            continue
        if sponsor == predicted["name"]:
            accuracies += 1
        else:
            print('Actual missed: ', sponsor)
            print('Predicted: ', predicted)
        print({
            "actual": sponsor,
            "predicted": predicted["name"]
        })
    print('Accuracy: ', accuracies/len(data))

def test_find_sponsorship_disclaimer():
    with open('test_data/disclaimers.json') as f:
        data = json.load(f)

    accuracy = 0.0 

    for d in data:
        video_id = d["video_id"]
        print(video_id)

        youtube_api_url = f"{YOUTUBE_API_BASE_URL}&id={video_id}&key={YOUTUBE_API_KEY}"
        youtube_response = requests.get(youtube_api_url)
        description = get_video_description(youtube_response)
        disclaimers = find_sponsorship_disclaimers(description)
        disclaimers = disclaimers.lower()
        if d['disclaimer'].lower() == disclaimers or d['disclaimer'].lower() in disclaimers or disclaimers in d['disclaimer'].lower():
            accuracy+=1
        print('actual', d['disclaimer'].lower())
        print('predicted', disclaimers)
        print(' ')

    print('Accuracy: ', accuracy/len(data))

if __name__ == "__main__":
    test_detect_possible_sponsors()
    # test_match_title_to_domain()
    # test_find_sponsorship_disclaimer()
