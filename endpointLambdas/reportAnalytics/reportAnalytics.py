import json
import os
import requests
import pymysql
import RDSconfigs

rdsHost = RDSconfigs.db_endpoint
name = RDSconfigs.db_username
password = RDSconfigs.db_password
dbName = RDSconfigs.db_name
port = 3306

conn = pymysql.connect(host=rdsHost, user=name,
                       passwd=password, db=dbName,
                       connect_timeout=5,
                       cursorclass=pymysql.cursors.DictCursor)

# input
# {
# 	userId: int,
# }

def topChannels(userId):
    
    """ SELECT topChannels.channel_id as channelid, brand_name
            From who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN
                    (SELECT video_id, channel_id
                            FROM who_funds_your_feed.Videos
                            NATURAL JOIN (SELECT *
                                                    FROM who_funds_your_feed.Watches
                                                    WHERE user_id = 10001
                                                    ORDER BY time_watched DESC
                                                    LIMIT 50) as userWatched
                            WHERE is_sponsored = TRUE
                            GROUP BY channel_id
                            ORDER BY COUNT(channel_id) DESC
                            LIMIT 5) AS topChannels
            WHERE Sponsorships.video_id = topChannels.video_id
            GROUP BY channel_id
            ORDER BY count(brand_name) OVER (partition by channel_id)
            LIMIT 5"""

    with conn.cursor() as cur:
        qry = f"SELECT topChannels.channel_id as channelid, brand_name From who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN (SELECT video_id, channel_id FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id = " + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched WHERE is_sponsored = TRUE GROUP BY channel_id ORDER BY COUNT(channel_id) DESC LIMIT 5) AS topChannels WHERE Sponsorships.video_id = topChannels.video_id GROUP BY channel_id ORDER BY count(brand_name) OVER (partition by channel_id) LIMIT 5"

        try:
            cur.execute(qry)

        except pymysql.Error as e:
            print(e)
            return {
                'statusCode': 500
            }

        records = cur.fetchall()
        result = []
        
        for record in records:
            channel_id = record['channelid']
            brand = record['brand_name']

            apiKey = os.environ['YOUTUBE_API_KEY']
            channelId = channel_id
            youtubeUrl = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channelId}&key={apiKey}'
            response = requests.get(youtubeUrl)
            channelDetails = response.json()
            channelName = channelDetails['items'][0]['snippet']['title']
            location = channelDetails['items'][0]['snippet']['country'] if "country" in channelDetails['items'][0]['snippet'] else "NA"
            thumbnail = channelDetails['items'][0]['snippet']['thumbnails']['medium']['url']
            vidCount = channelDetails['items'][0]['statistics']['videoCount']
            subCount = channelDetails['items'][0]['statistics']['subscriberCount']
            result.append({
                "channelId": channelId,
                "chanelName": channelName,
                "channelLocation": location,
                "channelImage": thumbnail,
                "videoCount": vidCount,
                "subCount": subCount,
                "topBrand": brand})
        return result


def lambda_handler(event, context):
    if 'body' in event:
        body = json.loads(event["body"])
        userId = body["userId"]
    else:
        userId = event["userId"]
    userId = str(userId)
    reportOutputJSON = {}
    
    reportOutputJSON["outputTopChannels"] = topChannels(userId)

    # % of time watched that is sponsored vs not
    """SELECT SUM(CASE WHEN is_sponsored = TRUE THEN video_duration_secs ELSE 0 END) *100 /SUM(video_duration_secs) as sponsoredTime
        FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT *
                FROM who_funds_your_feed.Watches
                WHERE user_id = 10001
                ORDER BY time_watched DESC LIMIT 50) as watchHistory;"""

    with conn.cursor() as cur:
        qryTimeSponsored = f"SELECT SUM(CASE WHEN is_sponsored = TRUE THEN video_duration_secs ELSE 0 END) *100 /SUM(video_duration_secs) as sponsoredTime FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as watchHistory;"

        try:
            cur.execute(qryTimeSponsored)
            value = cur.fetchall()
            outputTimeSponsored = int(value[0]["sponsoredTime"])
            

        except pymysql.Error as e:
            outputTimeSponsored = "System Error"
            print(e)
            return {
                'statusCode': 500,    
            }
    
        reportOutputJSON['outputTimeSponsored'] = outputTimeSponsored        

        # % of videos watched that are sponsored
        """ SELECT SUM(CASE WHEN is_sponsored THEN 1 ELSE 0 END)*100 / COUNT(*) as sponsoredVideos
        FROM who_funds_your_feed.Videos
        NATURAL JOIN (SELECT *
                                FROM who_funds_your_feed.Watches
                                WHERE user_id = 10001
                                ORDER BY time_watched DESC
                                LIMIT 50) as userWatched """

    with conn.cursor() as cur:
        qryVideoSponsored = f" SELECT SUM(CASE WHEN is_sponsored THEN 1 ELSE 0 END)*100 / COUNT(*) as sponsoredVideos FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id = " + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched"

        try:
            cur.execute(qryVideoSponsored)
            value = cur.fetchall()
            outputVideoSponsored = int(value[0]["sponsoredVideos"])

        except pymysql.Error as e:
            outputVideoSponsored = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }

        reportOutputJSON['outputVideoSponsored'] = outputVideoSponsored

        # Most frequently occuring companies
        """ SELECT brand_name, brand_url, COUNT(brand_name) AS video_count
        FROM who_funds_your_feed.Brands
        NATURAL JOIN who_funds_your_feed.Videos
        NATURAL JOIN (SELECT *
                                FROM who_funds_your_feed.Watches
                                WHERE user_id = 10001
                                ORDER BY time_watched DESC
                                LIMIT 50) as userWatched
        NATURAL JOIN who_funds_your_feed.Sponsorships
        GROUP BY brand_name
        ORDER BY COUNT(brand_name) DESC
        LIMIT 5  """

    with conn.cursor() as cur:
        qryFrequentCompanies = f" SELECT brand_name, brand_url, COUNT(brand_name) AS video_count FROM who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched NATURAL JOIN who_funds_your_feed.Sponsorships GROUP BY brand_name ORDER BY COUNT(brand_name) DESC LIMIT 5 "

        try:
            cur.execute(qryFrequentCompanies)
            outputFrequentCompanies = cur.fetchall()

        except pymysql.Error as e:
            outputFrequentCompanies = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }
 
        reportOutputJSON['outputFrequentCompanies'] = outputFrequentCompanies

        # What makes you unique (your top categories)
        """SELECT video_category, count(video_category)
                FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT video_id FROM who_funds_your_feed.Watches
                WHERE user_id = 10001
                ORDER BY time_watched DESC
                LIMIT 50) as userWatches
                GROUP BY video_category
                ORDER BY COUNT(video_category) DESC """
    with conn.cursor() as cur:
        qryTopCategories = f" SELECT video_category, count(video_category) FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT video_id FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatches GROUP BY video_category ORDER BY COUNT(video_category)"

        try:
            cur.execute(qryTopCategories)
            outputTopCategories = cur.fetchall()

        except pymysql.Error as e:
            outputTopCategories = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }

        reportOutputJSON['outputTopCategories'] = outputTopCategories

   
   
    # Percentage of videos funded by top funder
        """SELECT max(brandFrequencies.brandFrequency)/count(brandFrequencies.video_id) as percentageFromTopSponsor
        FROM
            (SELECT *,
            COUNT(Sponsorships.video_id) OVER(PARTITION BY Sponsorships.brand_name) as brandFrequency
            FROM who_funds_your_feed.Brands
            NATURAL JOIN who_funds_your_feed.Videos
            NATURAL JOIN (SELECT *
                                    FROM who_funds_your_feed.Watches
                                    WHERE user_id = 10001
                                    ORDER BY time_watched DESC
                                    LIMIT 50) as userWatched
            NATURAL JOIN who_funds_your_feed.Sponsorships
            ORDER BY brandFrequency DESC ) as brandFrequencies
        """
    with conn.cursor() as cur:
        qryFunderPercent = f" SELECT max(brandFrequencies.brandFrequency)/count(brandFrequencies.video_id) * 100 as percentageFromTopSponsor FROM (SELECT *, COUNT(Sponsorships.video_id) OVER(PARTITION BY Sponsorships.brand_name) as brandFrequency FROM who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id = "+userId+" ORDER BY time_watched DESC LIMIT 50) as userWatched NATURAL JOIN who_funds_your_feed.Sponsorships ORDER BY brandFrequency DESC ) as brandFrequencies"

        try:
            cur.execute(qryFunderPercent)
            value = cur.fetchall()
            outputFunderPercent = int(value[0]["percentageFromTopSponsor"])

        except pymysql.Error as e:
            outputFunderPercent = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }

        reportOutputJSON['outputTimeSponsoredbyFunder'] = outputFunderPercent

# 3 Other channels funded by your top funder
        """ Select DISTINCT Videos.channel_id
                FROM who_funds_your_feed.Videos NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN
                (SELECT brand_name
                        FROM who_funds_your_feed.Brands
                        NATURAL JOIN who_funds_your_feed.Videos
                        NATURAL JOIN (SELECT *
                                                FROM who_funds_your_feed.Watches
                                                WHERE user_id = 10001
                                                ORDER BY time_watched DESC
                                                LIMIT 50) as userWatched
                        NATURAL JOIN who_funds_your_feed.Sponsorships
                        ORDER BY  COUNT(Sponsorships.video_id) OVER(PARTITION BY Sponsorships.brand_name) DESC 
                        ) as topBrand
                WHERE Sponsorships.brand_name = topBrand.brand_name
                LIMIT 3"""
    
    with conn.cursor() as cur:
        qryFunderChannels = f"Select DISTINCT Videos.channel_id FROM who_funds_your_feed.Videos NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN (SELECT brand_name FROM who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id = " + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched NATURAL JOIN who_funds_your_feed.Sponsorships ORDER BY  COUNT(Sponsorships.video_id) OVER(PARTITION BY Sponsorships.brand_name) DESC  ) as topBrand WHERE Sponsorships.brand_name = topBrand.brand_name LIMIT 3 "
        additionalChannels = []
        
        try:
            cur.execute(qryFunderChannels)

        except pymysql.Error as e:
            print(e)
            return {
                'statusCode': 500
            }

        channels = cur.fetchall()
    
        for channel in channels:
            apiKey = os.environ['YOUTUBE_API_KEY']
            channelId = channel["channel_id"]
            youtubeUrl = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channelId}&key={apiKey}'
            response = requests.get(youtubeUrl)
            channelDetails = response.json()
            channelName = channelDetails['items'][0]['snippet']['title']
            location = channelDetails['items'][0]['snippet']['country'] if "country" in channelDetails['items'][0]['snippet'] else "NA"
            thumbnail = channelDetails['items'][0]['snippet']['thumbnails']['medium']['url']
            vidCount = channelDetails['items'][0]['statistics']['videoCount']
            subCount = channelDetails['items'][0]['statistics']['subscriberCount']
            additionalChannels.append({
                "channelId": channelId,
                "channelName": channelName,
                "channelLocation": location,
                "channelImage": thumbnail,
                "videoCount": vidCount,
                "subCount": subCount
            })
    

        reportOutputJSON['outputFunderChannels'] = additionalChannels
   
   
    body = json.dumps(reportOutputJSON)
    return {
        "statusCode": 200,
        'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json'
        },
        "body": body
    }
