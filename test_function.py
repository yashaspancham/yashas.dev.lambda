import json
import lambda_function  # This is your Lambda function module
from moto import mock_dynamodb
import boto3
import os

@mock_dynamodb
def test_lambda_handler():
    print("✅ test_lambda_handler is running...")

    # Set env variables before boto3 client is created
    os.environ["AWS_REGION"] = "us-east-1"
    os.environ["TABLE_NAME"] = "TestTable"
    os.environ["PARTITION_KEY"] = "counter"
    os.environ["PARTITION_VALUE"] = "visits"

    # Create mocked DynamoDB table
    client = boto3.client('dynamodb', region_name="us-east-1")
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

    # Call your lambda handler
    response = lambda_function.lambda_handler({}, {})
    body = json.loads(response["body"])

    # Assertions (update to match your Lambda output)
    assert response["statusCode"] == 200
    assert "Visiterscount" in body
    assert isinstance(body["Visiterscount"], int)
