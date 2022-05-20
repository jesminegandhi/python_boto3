## Script to list all the S3 Buckets

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets = response["Buckets"]

## Printing all the Bucket by the Key value "Name" & "Creation Date"
for bucket in buckets:
    print(bucket["Name"])
    print(bucket["CreationDate"])

    