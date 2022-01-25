import json
import spacy
from sponsors_detector.process_text import find_video_sponsors
from util.util import (get_model_path, is_video_processed,
                       process_sponsors, add_new_watch_event)

HEADERS = {'Access-Control-Allow-Origin': '*',
           'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
	       'Access-Control-Allow-Credentials': 'true',
	       'Content-Type': 'application/json'
           }

model = get_model_path("en_core_web_sm-3.0.0")
nlp = spacy.load(model)

def lambda_handler(event, context):
    userId = event.get('userId')
    videoId = event.get('youtubeVideoId')
    timestamp = event.get('timestamp')
    if not userId or not videoId or not timestamp:
        return {
            'statusCode': 400,
            'headers': HEADERS
        }

    if is_video_processed(videoId) == "True":
        return {
            'statusCode': 200,
            'headers': HEADERS
        }
    result = find_video_sponsors(videoId, nlp)
    if result:
        process_sponsors(result, videoId)
    add_new_watch_event(userId, videoId, timestamp)
    return {
        "statusCode": 200,
        "body": json.dumps(f"Sponsorships: {result.get('sponsorships', [])}")

    }
