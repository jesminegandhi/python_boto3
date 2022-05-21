## Script to create S3 Bucket

import boto3

client = boto3.client("s3")

client.create_bucket(ACL='public-read',Bucket="jass-new-bucket-0519")
