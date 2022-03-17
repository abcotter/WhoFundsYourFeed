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
# 	userEmail: String
# }
def lambda_handler(event, context):
	userEmail = event['userEmail']

	with conn.cursor() as cur:
		qry = f"INSERT INTO Users (user_name) Values ('{userEmail}');"
		try: 
			cur.execute(qry)
		except pymysql.Error as e:
			#  duplicate key case
			if e.args[0] != 1062:
		
				return {
					'statusCode': 500,
					'headers': headers,
					'body': json.dumps(("Error %d: %s" % (e.args[0], e.args[1])))
				}
		conn.commit()
    
	with conn.cursor() as cur:
		qry = f"SELECT user_id FROM Users where user_name='{userEmail}';"
		cur.execute(qry)
		user_id = cur.fetchone().get('user_id')

	return {
			'statusCode': 200,
			'headers': headers,
            'userId': user_id
		}
