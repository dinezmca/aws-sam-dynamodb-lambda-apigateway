import json
import boto3
import os

print('Loading function')
region = os.environ['REGION_NAME']
table_name = os.environ['TABLE_NAME']
dynamo = boto3.client('dynamodb', region_name=region)
def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    print("Recived event ---", json.dumps(event,  indent=2))
    scan_result = dynamo.scan(TableName =table_name)
    return respond(None, res=scan_result)
