import pandas as pd
from sponsors_detector.process_text import find_video_sponsors
import spacy
"""
detect sponsors and save to list
for every video, count how many of the sponsors are actually sponsors (precision)
count what percentage of all tthe sponsors were actually found (recall)
erturn and add to total precision
"""
def get_actual_sponsors(video_id, data):
    return data[data['video_id']==video_id]['brand_name'].tolist()

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    data = pd.read_csv('test_data/sponsorship_data.csv')
    video_ids = data['video_id'].unique().tolist()
    precision_metrics = []
    recall_metrics = []
    for i, video_id in enumerate(video_ids):
        if i == 1:
            break
        result = find_video_sponsors(video_id, nlp)
        sponsorships = result.get('sponsorships', [])
        sponsorships = [s['name'] for s in sponsorships]
        actual_sponsorships = get_actual_sponsors(video_id, data)
        total = set(actual_sponsorships).intersection(set(sponsorships))
        precision = len(total)/len(sponsorships)
        recall = len(total)/len(actual_sponsorships)
        print({'video_id': video_id,
               'predictted': sponsorships,
               'actual': actual_sponsorships,
               'precision': precision,
               'recall': recall})


