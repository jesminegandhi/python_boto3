## Script to delete object or objects from S3 Bucket

import boto3

s3_resource = boto3.client('s3')

## Delete single object from the S3 Bucket
s3_resource.delete_object(Bucket='jass-new-bucket-0519',Key='pic1.png')

## Find all the objects from the Bucket
objects=s3_resource.list_objects(Bucket="jass-new-bucket-0519")["Contents"]

## Obtain the length of the Bucket
len(objects)

## Delete multiple objects from the S3 Bucket
for object in objects:
    response=s3_resource.delete_object(Bucket='jass-new-bucket-0519',Key=object["Key"])
    #print(response)