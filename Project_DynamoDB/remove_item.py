## Script to remove an item from the DynamoDB table (Supermarket)

import boto3

client = boto3.client('dynamodb')

response = client.delete_item(
    TableName='Supermarket',
    Key={'Category': {'S': 'Dairy'}, 'Food': {'S': 'Milk'}, 
    }
)