import json
import lambda_function
from moto import mock_dynamodbv2
import boto3
import os

@mock_dynamodbv2
def test_lambda_handler():
    print("✅ test_lambda_handler is running...")

    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["TABLE_NAME"] = "TestTable"
    os.environ["PARTITION_KEY"] = "counter"
    os.environ["PARTITION_VALUE"] = "visits"

    client = boto3.client('dynamodb', region_name='us-east-1')
    client.create_table(
        TableName="TestTable",
        KeySchema=[{"AttributeName": "counter", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "counter", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )
    client.put_item(
        TableName="TestTable",
        Item={"counter": {"S": "visits"}, "count": {"N": "0"}}
    )

    response = lambda_function.lambda_handler({}, {})
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "visitorsCount" in body
    assert isinstance(body["visitorsCount"], int)
