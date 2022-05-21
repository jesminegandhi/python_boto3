## Script to create AWS EBS Volume from Snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-2c',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-0f4a791ad466d1634',
      VolumeType='gp2')