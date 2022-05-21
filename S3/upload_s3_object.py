## Script to upload object to S3 Bucket

import boto3

## Upload single file to the S3 Bucket

s3_resource = boto3.client('s3')

s3_resource.upload_file('/home/ec2-user/environment/python_boto3/aws.jpg','jass-new-bucket-0519','aws.png')

## Upload multiple files to the S3 bucket

import os
import glob

cwd=os.getcwd()

cwd=cwd+"/files/"

files=glob.glob(cwd+"*.png")


for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="jass-new-bucket-0519",
    Key=file.split("/")[-1])    