## Script to query the DynamoDB table (Supermarket) wrt Partition key value: 'Protein'

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.query(
    TableName='Supermarket',
    ExpressionAttributeValues={
        ':ident':{
            'S': 'Protein',
        },
    },
    KeyConditionExpression='Category = :ident',
    ProjectionExpression='Food'
)

print(response['Items'])