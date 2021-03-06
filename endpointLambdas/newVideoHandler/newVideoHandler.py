import pymysql
import json
import re
import RDSconfigs
from categoryMapping import categoryMap

rdsHost = RDSconfigs.db_endpoint
name = RDSconfigs.db_username
password = RDSconfigs.db_password
dbName = RDSconfigs.db_name

connection = {
	"host": rdsHost,
	"password": password,
    "port": 3306,
    "user": name,
    "db": dbName,
    "connect_timeout": 5,
    "cursorclass": pymysql.cursors.DictCursor
}


conn = pymysql.connect(**connection)

headers = {
							'Access-Control-Allow-Origin': '*',
							'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
							'Access-Control-Allow-Credentials': 'true',
							'Content-Type': 'application/json'
					}

# input
# {
# 	youtubeVideoId: string,
# 	youtubeApiResponse: {
			# 	"kind": string,
			# 	"etag": string,
			# 	"items": [
			# 		{
			# 			...
			# 			"snippet": {
			# 				...
			# 				"title": "Your body language may shape who you are | Amy Cuddy",
			# 				"description": "Body",
			# 				...
			# 				"channelTitle": "TED",
			# 				....
			# 				"categoryId": "22",
			# 				...
			# 			},
			# 			"contentDetails": {
			# 				"duration": "PT21M3S",
			# 				...
			# 			},
			# 			...
			# 		}
			# 	]
# 		}
# 	sponsorships: [
# 		{name: "helloFresh", url: "http....com"},
# 	]
# }

def lambda_handler(event, context):
	videoId = event['youtubeVideoId']
	videoTitle = event['youtubeApiResponse']['items'][0]['snippet']['title'].replace("'", "&#39;").replace("\"", "&#34;")
	channelId = event['youtubeApiResponse']['items'][0]['snippet']['channelId']
	category = categoryMap[int(event['youtubeApiResponse']['items'][0]['snippet']['categoryId'])]
	runtimeHours = re.findall(r"\d{1,2}H", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']) if len(re.findall(r"\d{1,2}H", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']))>0 else ['0H']
	runtimeMinutes = re.findall(r"\d{1,2}M", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']) if len(re.findall(r"\d{1,2}M", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']))>0 else ['0M']
	runtimeSeconds = re.findall(r"\d{1,2}S", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']) if len(re.findall(r"\d{1,2}S", event['youtubeApiResponse']['items'][0]['contentDetails']['duration']))>0 else ['0S']
	duration = int(runtimeHours[0][:-1])*3600 + int(runtimeMinutes[0][:-1])*60 + int(runtimeSeconds[0][:-1])
	isSponsored = True if len(event['sponsorships']) >0 else False
	# Add video to video table
	with conn.cursor() as cur:
		qry = f'INSERT INTO Videos (video_id, title, channel_id, video_category, video_duration_secs, is_sponsored) Values ("{videoId}", "{videoTitle}", "{channelId}", "{category}", {duration}, {isSponsored});'
		try:
			cur.execute(qry)
		except pymysql.Error as e:
			#  duplicate key case
			if e.args[0] == 1062:
				return {
					'statusCode': 200,
					'headers': headers
				}
			else:
				return {
					'statusCode': 500,
					'headers': headers,
					'body': ("Error %d: %s" % (e.args[0], e.args[1]))
				}
	# check and add new sponsors to brand table
	if len(event["sponsorships"]) >0:
		with conn.cursor() as cur:
			sponsorNames = [x["name"] for x in event["sponsorships"]]
			sponsors = ",".join(map(lambda x: "'" + x + "'" , sponsorNames))
			qry = f"SELECT brand_name FROM Brands WHERE brand_name IN ({sponsors})"
			cur.execute(qry)
			existingSponsors = [x["brand_name"] for x in cur.fetchall()]
			newSponsors = [x for x in event["sponsorships"] if x["name"] not in set(existingSponsors)]
			
		if len(newSponsors) > 0:
			# insert new sponsors
			for newSponsor in newSponsors:
				with conn.cursor() as cur:
					sponsorName = newSponsor["name"]
					sponsorUrl = newSponsor.get('url')
					sponsorUrl = f"'{sponsorUrl}'" if sponsorUrl else "NULL"
					qry = f"INSERT INTO Brands (brand_name, brand_url) Values ('{sponsorName}', {sponsorUrl});"
					cur.execute(qry)

		# create video to brand relationship
		for brandName in event['sponsorships']:
			with conn.cursor() as cur:
				name = brandName["name"]
				qry = f"INSERT INTO Sponsorships (brand_name, video_id) Values ('{name}','{videoId}');"
				try: 
					cur.execute(qry)
				except pymysql.Error as e:
					#  duplicate key case
					if e.args[0] == 1062:
						return {
							'statusCode': 200,
							'headers': headers
						}
					else:
						return {
							'statusCode': 500,
							'headers': headers,
							'body': ("Error %d: %s" % (e.args[0], e.args[1]))
						}
	
	with conn.cursor() as cur:
		timestamp = event["timestamp"]
		userId = event["userId"]
		qry2 = f"INSERT INTO Watches (user_id, video_id, time_watched) Values ('{userId}', '{videoId}', '{timestamp}');"
		try:
			cur.execute(qry2)
		except pymysql.Error as e:
			#  duplicate key case
			if e.args[0] == 1062:
				return {
					'statusCode': 200,
					'headers': headers
				}
			else:
				return {
					'statusCode': 500,
					'headers': headers,
					'body': ("Error %d: %s" % (e.args[0], e.args[1]))
				}
	conn.commit()
	return {
			'statusCode': 200,
			'headers': headers
		}
 
