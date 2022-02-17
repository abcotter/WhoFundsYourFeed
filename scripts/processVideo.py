import requests
import pandas as pd
import time
if __name__ == "__main__":
    watches = pd.read_csv('Watches.csv').to_dict('records')
    for i, watch in enumerate(watches):
        print(watch)
        time_watched = watch['time_watched'].split(' ')
        date = time_watched[0].split('/')
        month = date[0] if len(date[0])==2 else "0" + date[0]
        timestamp = f"2021-{month}-{date[1]}"
        payload = {
            "userId": watch["user_id"],
            "youtubeVideoId": watch["video_id"],
            "timestamp": watch["time_watched"]
        }
        response = requests.post('https://6827rdxni0.execute-api.us-east-1.amazonaws.com/v1/processVideoTest', json=payload)
    
        print(response.status_code)
        print(response.json())
        time.sleep(10)

    #figure out how to add a 0 if not included
    
    # payload = {
    # "userId": "1",
    # "youtubeVideoId": "UI6FZVbcd-A",
    # "timestamp": "2022-01-11 00:00:00"
    # }
    # response = requests.post('https://6827rdxni0.execute-api.us-east-1.amazonaws.com/v1/processVideoTest', json=payload)
    # print(response.status_code)
    # print(response.json())
