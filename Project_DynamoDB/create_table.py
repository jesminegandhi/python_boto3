## Script to create a 'Supermarket' DynamoDB table with 'Category' as Partition key & 'Food' as Sort key

import boto3

dynamoDB = boto3.client('dynamodb')

table = dynamoDB.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Category',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Food',
            'AttributeType': 'S'
        }
    ],
    TableName='Supermarket',    # Table Name
    KeySchema=[
        {
            'AttributeName': 'Category',
            'KeyType': 'HASH'   # Partition key
        },
        {
            'AttributeName': 'Food',
            'KeyType': 'RANGE'  # Sort Key
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)