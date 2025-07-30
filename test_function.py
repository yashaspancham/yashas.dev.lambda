import json
import os
import boto3
from moto import mock_dynamodb
import lambda_function

@mock_dynamodb
def test_lambda_handler():
    # Set environment variables used by the Lambda function
    os.environ["TABLE_NAME"] = "TestTable"
    os.environ["PARTITION_KEY"] = "counter"
    os.environ["PARTITION_VALUE"] = "visits"

    # Setup mocked DynamoDB
    client = boto3.client("dynamodb", region_name="us-east-1")
    client.create_table(
        TableName="TestTable",
        KeySchema=[{"AttributeName": "counter", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "counter", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )
    client.put_item(
        TableName="TestTable",
        Item={
            "counter": {"S": "visits"},
            "count": {"N": "0"}
        }
    )

    # Call the lambda handler
    response = lambda_function.lambda_handler({}, {})
    body = json.loads(response["body"])

    # Assertions
    assert response["statusCode"] == 200
    assert "visitorsCount" in body
    assert isinstance(body["visitorsCount"], int)
