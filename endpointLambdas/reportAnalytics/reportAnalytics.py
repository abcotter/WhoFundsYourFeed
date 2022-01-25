import pymysql
import json
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

def lambda_handler(event, context):
    body = json.loads(event['body'])
    userId = body['userId']
   
    reportOutputJSON = []

    # % of time watched that is sponsored vs not
    """SELECT  SUM(CASE WHEN isSponsored = TRUE THEN video_duration_sec ELSE 0 END) AS sponsoredWatchTime *100/Sum(video_duration_sec)
    FROM Videos innerjoin
                (SELECT *
                FROM Watches
                WHERE user_id = $user_id
                ORDER BY time_watched DESC LIMIT 50) as watchHistory; """
        
    with conn.cursor() as cur:
        qryTimeSponsored = f" SELECT  SUM(CASE WHEN isSponsored = TRUE THEN video_duration_sec ELSE 0 END) AS sponsoredWatchTime *100/Sum(video_duration_sec) FROM Videos innerjoin (SELECT * FROM Watches WHERE user_id = "+ userId + " ORDER BY time_watched DESC LIMIT 50) as watchHistory;"

        try:
            cur.execute(qryTimeSponsored)

        except pymysql.Error as e:
            return {
                'statusCode': 500,
                'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
                }

        # TO DO: find a way to return this as a single value/int actually
        outputTimeSponsored = cur.fetchall()
        reportOutputJSON[outputTimeSponsored] = outputTimeSponsored


        # % of videos watched that are sponsored
        """ SELECT SUM(CASE WHEN isSponsored THEN 1 ELSE 0 END)*100 / COUNT(*)
        FROM Videos
        innerjoin (SELECT *
                                FROM Watches`
                                WHERE user_id = $user_id
                                ORDER BY time_watched DESC
                                LIMIT 50) """

    with conn.cursor() as cur:
        qryVideoSponsored = f" SELECT SUM(CASE WHEN isSponsored THEN 1 ELSE 0 END)*100 / COUNT(*) FROM Videos innerjoin (SELECT * FROM Watches WHERE user_id ="+ userId + " ORDER BY time_watched DESC LIMIT 50)"

        try:
            cur.execute(qryVideoSponsored)

        except pymysql.Error as e:
            return {
                'statusCode': 500,
                'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
                }

    # TO DO: find a way to return this as a single value/int actually
        outputVideoSponsored = cur.fetchall()
        reportOutputJSON[outputVideoSponsored] = outputVideoSponsored
    
        # Most frequently occuring companies
        """ SELECT brand_name, COUNT(brand_name) AS brandFrequency
        FROM Brand
        innerjoin Videos
        innerjoin (SELECT *
                                FROM Watches
                                WHERE user_id = $user_id
                                ORDER BY time_watched DESC
                                LIMIT 50)
        innerjoin Sponsorhips
        GROUPBY brand_name
        ORDER BY brandFrequency DESC
        LIMIT 5 """
    with conn.cursor() as cur:
        qryFrequentCompanies = f" SELECT brand_name FROM (SELECT brand_name, COUNT(brand_name) AS brandFrequency FROM Brand innerjoin Videos innerjoin (SELECT * FROM Watches WHERE user_id =" + userId + "ORDER BY time_watched DESC LIMIT 50) innerjoin Sponsorhips GROUPBY brand_name ORDER BY brandFrequency DESC LIMIT 5)"

        try:
            cur.execute(qryFrequentCompanies)

        except pymysql.Error as e:
            return {
                'statusCode': 500,
                'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
                }

        outputFrequentCompanies = cur.fetchall()
        reportOutputJSON[outputFrequentCompanies] = outputFrequentCompanies
    
        # our top channels top sponsors (channels you watch a lot and who are their sponsors)
        """ SELECT topChannels.channel_name, brand_name
        From Sponsorships innerjoin Brand innerjoin
                (SELECT channel_name, COUNT(channel_name) AS channelFrequency
                        FROM Videos
                        innerjoin (SELECT *
                                                FROM Watches
                                                WHERE user_id = $user_id
                                                ORDER BY time_watched DESC
                                                LIMIT 50)
                        GROUPBY channel_name
                        ORDER BY channelFrequency DESC
                        LIMIT 5) AS topChannels
        WHERE channel_name = topChannels.channel_name
        LIMIT 5 """

    with conn.cursor() as cur:
        qryChannelSponsors = f"SELECT brand_name FROM SELECT topChannels.channel_name, brand_name From Sponsorships innerjoin Brand innerjoin (SELECT channel_name, COUNT(channel_name) AS channelFrequency FROM Videos innerjoin (SELECT FROM Watches WHERE user_id =" + userid + "ORDER BY time_watched DESC LIMIT 50) GROUPBY channel_name ORDER BY channelFrequency DESC LIMIT 5) AS topChannels WHERE channel_name = topChannels.channel_name LIMIT 5"

        try:
            cur.execute(qryChannelSponsors)

        except pymysql.Error as e:
            return {
                'statusCode': 500,
                'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
                }

        outputChannelSponsors = cur.fetchall()
        reportOutputJSON[outputChannelSponsors] = outputChannelSponsors

        # What makes you unique (your top categories)
        """ SELECT video_category
        FROM Videos
        innerjoin (SELECT video_category, COUNT(video_category) as categoryFrequency
                                FROM videos innerjoin Watches
                                WHERE user_id = $user_id
                                ORDER BY time_watched DESC
                                LIMIT 50)
        GROUPBY video_category
        ORDER BY categoryFrequency DESC
        LIMIT 1 """
    with conn.cursor() as cur:
        qryTopCategories = f" SELECT video_category FROM Videos innerjoin (SELECT video_category, COUNT(video_category) as categoryFrequency FROM videos innerjoin Watches WHERE user_id = " + userId + " ORDER BY time_watched DESC LIMIT 50) GROUPBY video_category ORDER BY categoryFrequency DESC LIMIT 1"

        try:
            cur.execute(qryTopCategories)

        except pymysql.Error as e:
            return {
                'statusCode': 500,
                'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
                }

        outputTopCategories = cur.fetchall()
        reportOutputJSON[outputTopCategories] = outputTopCategories
    
    body = json.dumps(reportOutputJSON)
