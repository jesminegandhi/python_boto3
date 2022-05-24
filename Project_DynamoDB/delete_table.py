## Script to delete the DynamoDB table (Supermarket)

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_table(
    TableName='Supermarket'
)