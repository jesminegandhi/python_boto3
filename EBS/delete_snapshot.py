## Script to delete snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-0467305c5be0929eb')