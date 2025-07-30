import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

TABLE_NAME = os.getenv('TABLE_NAME')
PARTITION_KEY = os.getenv('PARTITION_KEY')
PARTITION_VALUE = os.getenv('PARTITION_VALUE')

def lambda_handler(event, context):
    response = dynamodb.update_item(
        TableName=TABLE_NAME,
        Key={
            PARTITION_KEY: {'S': PARTITION_VALUE}
        },
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={
            '#count': 'count'
        },
        ExpressionAttributeValues={
            ':incr': {'N': '1'}
        },
        ReturnValues='UPDATED_NEW'
    )

    new_count = int(response['Attributes']['count']['N'])

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "OPTIONS,PUT"
        },
        "body": json.dumps({"Visiterscount": new_count})
    }
