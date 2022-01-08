

# inputs
# {
# 	videoId: string,
# 	sponshoshipData: {...}
# }
def lambda_handler(event, context):
	videoId = event['videoId']
	return { 
			'videoId' : videoId
	}