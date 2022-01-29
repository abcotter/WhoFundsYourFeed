import json
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


def lambda_handler(event, context):
    userId = json.loads(event['userId'])
    userId = str(userId)
    reportOutputJSON = {}

    # % of time watched that is sponsored vs not
    """SELECT SUM(CASE WHEN is_sponsored = TRUE THEN video_duration_secs ELSE 0 END) *100 /SUM(video_duration_secs)
        FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT *
                FROM who_funds_your_feed.Watches
                WHERE user_id = 10001
                ORDER BY time_watched DESC LIMIT 50) as watchHistory;"""

    with conn.cursor() as cur:
        qryTimeSponsored = f"SELECT SUM(CASE WHEN is_sponsored = TRUE THEN video_duration_secs ELSE 0 END) *100 /SUM(video_duration_secs) FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as watchHistory;"

        try:
            cur.execute(qryTimeSponsored)
            outputTimeSponsored = cur.fetchall()
            

        except pymysql.Error as e:
            outputTimeSponsored = "System Error"
            print(e)
            return {
                'statusCode': 500,    
            }
    
        reportOutputJSON['outputTimeSponsored'] = outputTimeSponsored        

        # % of videos watched that are sponsored
        """ SELECT SUM(CASE WHEN is_sponsored THEN 1 ELSE 0 END)*100 / COUNT(*)
        FROM who_funds_your_feed.Videos
        NATURAL JOIN (SELECT *
                                FROM who_funds_your_feed.Watches
                                WHERE user_id = 10001
                                ORDER BY time_watched DESC
                                LIMIT 50) as userWatched """

    with conn.cursor() as cur:
        qryVideoSponsored = f" SELECT SUM(CASE WHEN is_sponsored THEN 1 ELSE 0 END)*100 / COUNT(*) FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id = " + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched"

        try:
            cur.execute(qryVideoSponsored)
            outputVideoSponsored = cur.fetchall()

        except pymysql.Error as e:
            outputVideoSponsored = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }

        reportOutputJSON['outputVideoSponsored'] = outputVideoSponsored

        # Most frequently occuring companies
        """ SELECT brand_name 
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
        qryFrequentCompanies = f" SELECT brand_name FROM who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched NATURAL JOIN who_funds_your_feed.Sponsorships GROUP BY brand_name ORDER BY COUNT(brand_name) DESC LIMIT 5 "

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

        # our top channels top sponsors (channels you watch a lot and who are their sponsors)
        """ SELECT brand_name
        From who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN
                (SELECT video_id, channel_name
                        FROM who_funds_your_feed.Videos
                        NATURAL JOIN (SELECT *
                                                FROM who_funds_your_feed.Watches
                                                WHERE user_id = 10001
                                                ORDER BY time_watched DESC
                                                LIMIT 50) as userWatched
						WHERE is_sponsored = TRUE
                        GROUP BY channel_name
                        ORDER BY COUNT(channel_name) DESC
                        LIMIT 5) AS topChannels
        WHERE Sponsorships.video_id = topChannels.video_id
        LIMIT 5"""

    with conn.cursor() as cur:
        qryChannelSponsors = f"SELECT brand_name From who_funds_your_feed.Brands NATURAL JOIN who_funds_your_feed.Sponsorships NATURAL JOIN (SELECT video_id, channel_name FROM who_funds_your_feed.Videos NATURAL JOIN (SELECT * FROM who_funds_your_feed.Watches WHERE user_id =" + userId + " ORDER BY time_watched DESC LIMIT 50) as userWatched WHERE is_sponsored = TRUE GROUP BY channel_name ORDER BY COUNT(channel_name) DESC LIMIT 5) AS topChannels WHERE Sponsorships.video_id = topChannels.video_id LIMIT 5"

        try:
            cur.execute(qryChannelSponsors)
            outputChannelSponsors = cur.fetchall()

        except pymysql.Error as e:
            outputChannelSponsors = "System Error"
            print(e)
            return {
                'statusCode': 500,
            }

        reportOutputJSON['outputChannelSponsors'] = outputChannelSponsors

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

    body = json.dumps(reportOutputJSON)
