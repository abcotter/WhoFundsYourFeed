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


# inputs
# {
# 	youtubeVideoId: string
# }
def lambda_handler(event, context):
	videoId = event['youtubeVideoId']
	with conn.cursor() as cur:
			qry = f"SELECT * FROM Videos WHERE video_id = '{videoId}';"
			cur.execute(qry)
			row = cur.fetchone()
	
	result = True if len(row) >= 1 else False

	return {
			'statusCode': 200,
			'headers': {
					'Access-Control-Allow-Origin': '*',
					'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
					'Access-Control-Allow-Credentials': 'true',
					'Content-Type': 'application/json'
			},
			'body': json.dumps(result)
	}