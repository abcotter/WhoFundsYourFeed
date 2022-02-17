import pandas as pd
import json
from sponsors_detector.process_text import find_video_sponsors
import spacy

def get_actual_sponsors(video_id, data):
    brand_names = data[data['video_id']==video_id]['brand_name'].tolist()
    return [brand_name.lower() for brand_name in brand_names]

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    data = pd.read_csv('test_data/sponsorship_data.csv')
    video_ids = data['video_id'].unique().tolist()
    precision_metrics = []
    recall_metrics = []
    overall_results = []
    for i, video_id in enumerate(video_ids):
        try:
            result = find_video_sponsors(video_id, nlp)
        except Exception as e:
            print('Error finding sponsors', e)
            continue
        sponsorships = result.get('sponsorships', [])
        sponsorships = [s['name'].lower() for s in sponsorships]
        if len(sponsorships) == 0:
            precision = 0.0
            recall = 0.0
        else:
            actual_sponsorships = get_actual_sponsors(video_id, data)
            total = set(actual_sponsorships).intersection(set(sponsorships))
            precision = len(total)/len(sponsorships)
            recall = len(total)/len(actual_sponsorships)
        results_info = {'video_id': video_id,
                        'predicted': sponsorships,
                        'actual': actual_sponsorships,
                        'precision': precision,
                        'recall': recall}
        overall_results.append(results_info)
        precision_metrics.append(precision)
        recall_metrics.append(recall)
        print(json.dumps(results_info, indent=4))
    with open('results.json', 'w') as f:
        json.dump(overall_results, f)
    print('average precision:', sum(precision_metrics)/len(precision_metrics))
    print('average recall:', sum(recall_metrics)/len(recall_metrics))


