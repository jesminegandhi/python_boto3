## Script to Remove VPC using Python

import boto3

client=boto3.client("ec2")

client.delete_vpc(VpcId='vpc-0da84477846b3153d')
  
