import pymysql
import json
import RDSconfigs

rdsHost = RDSconfigs.db_endpoint
name = RDSconfigs.db_username
password = RDSconfigs.db_password
dbName = RDSconfigs.db_name
port = 3306


conn = pymysql.connect(host=rdsHost,user=name,
												passwd=password,db=dbName,
												connect_timeout=5,
												cursorclass=pymysql.cursors.DictCursor)

headers = {
							'Access-Control-Allow-Origin': '*',
							'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
							'Access-Control-Allow-Credentials': 'true',
							'Content-Type': 'application/json'
					}

# input
# {
# 	userId: int,
# 	youtubeVideoId: string,
# 	timestamp: UTC timestamp
# }
def lambda_handler(event, context):
	userId = event['userId']
	videoId = event['youtubeVideoId']
	timestamp = event['timestamp']

	with conn.cursor() as cur:
		qry = f"INSERT INTO Watches (user_id, video_id, time_watched) Values ('{userId}', '{videoId}', '{timestamp}');"
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
		conn.commit()
		row = cur.rowcount

	if row >= 1:
		return {
			'statusCode': 200,
			'headers': headers
		}
	else:
		return {
			'statusCode': 500,
			'headers': headers
		}
