## Script to list objects from S3 Bucket

import boto3

s3_resource = boto3.client('s3')

## Find all the objects from the Bucket
objects=s3_resource.list_objects(Bucket="jass-new-bucket-0519")["Contents"]

## To obtain the length of Bucket (Length would be 0 if no objects)
len(objects)

## Condition to check if there is any object in the Bucket
if len(objects)>0:
    print("Objects exist in Bucket")

## Print the Object Key Value
for object in objects:
    print(object["Key"])