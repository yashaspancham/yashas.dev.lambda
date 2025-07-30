import boto3
import os
import json

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name=os.getenv("AWS_REGION", "us-east-1"))

    table_name = os.environ["TABLE_NAME"]
    key = os.environ["PARTITION_KEY"]
    value = os.environ["PARTITION_VALUE"]

    response = dynamodb.get_item(
        TableName=table_name,
        Key={key: {"S": value}}
    )

    count = int(response["Item"]["count"]["N"])
    count += 1

    dynamodb.put_item(
        TableName=table_name,
        Item={
            key: {"S": value},
            "count": {"N": str(count)}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"visitorsCount": count})
    }
