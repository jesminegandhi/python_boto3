## Script to describe an EBS Volume Snapshot

import boto3

ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=[
          'snap-09f16a819a59819f9'
      ])