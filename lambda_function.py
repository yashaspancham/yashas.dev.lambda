import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name=os.getenv('AWS_REGION', 'ap-south-1'))

    table_name = os.getenv('TABLE_NAME')
    partition_key = os.getenv('PARTITION_KEY')
    partition_value = os.getenv('PARTITION_VALUE')

    response = dynamodb.update_item(
        TableName=table_name,
        Key={partition_key: {'S': partition_value}},
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':incr': {'N': '1'}},
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
