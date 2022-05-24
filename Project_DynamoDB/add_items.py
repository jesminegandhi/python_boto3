## Script to add items to the DynamoDB table (Supermarket)

import boto3
import json

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Supermarket')

with open("supermarketList.json") as json_file:
    items = json.load(json_file)
    for item in items:
        Category = item['Category']
        Food = item['Food']
        
        print("Adding item :", Food)

        table.put_item(
            Item={
                'Category': Category,
                'Food': Food
            }
        )