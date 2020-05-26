#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D

relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
)

print('Connecting to AWS EC2')
ec2 = sess.client('ec2', region_name=relay.get(D.aws.region))
raw_images = ec2.describe_images(Owners=['self'])
image_ids = [image['ImageId'] for image in raw_images['Images']]
print('Found the following images: {}'.format(image_ids))

print('Adding {} image(s) to the output `images`'.format(len(raw_images['Images'])))
relay.outputs.set('images', raw_images['Images'])