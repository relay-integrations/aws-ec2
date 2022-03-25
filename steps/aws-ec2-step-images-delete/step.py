#!/usr/bin/env python
import boto3
from relay_sdk import Interface, Dynamic as D
from botocore.exceptions import ClientError

relay = Interface()

session_token = None
try:
  session_token = relay.get(D.aws.connection.sessionToken)
except:
  pass

sess = boto3.Session(
    aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
    aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
    region_name=relay.get(D.aws.region),
    aws_session_token=session_token
)

ec2 = sess.client('ec2')
image_ids = relay.get(D.imageIDs)

try:
  dry_run = relay.get(D.dryRun)
except:
  dry_run = False

print(f'Deleting the following images: {image_ids}, dryRun: {dry_run}')

for image_id in image_ids:
  try:
    print(f'Trying to delete {image_id}... ', end='')
    ec2.deregister_image(
        ImageId=image_id,
        DryRun=dry_run,
    )
    print(f'success.')

  except ClientError as err:
    if err.response['Error']['Code'] in ['DryRunOperation', 'InvalidAMIID.NotFound', 'InvalidAMIID.Unavailable', 'InvalidAMIID.Malformed']:
      print(err)
      continue

    print(
        f'Failed to perform operation on image {image_id}, stopping processing.')
    raise(err)
