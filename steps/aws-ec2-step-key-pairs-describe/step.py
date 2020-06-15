#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D

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
key_pairs = ec2.describe_key_pairs()['KeyPairs']
print('Found {} key pairs:'.format(len(key_pairs)))
print("{:<30} {:<100} {:<50}".format('ID', 'NAME', 'TAGS'))
for key in key_pairs:
  print("{:<30} {:<100} {:<50}".format(key['KeyPairId'], key['KeyName'], str(key['Tags'])))

# Setting output `keyPairs` to list of key pairs 
print('\nAdding {} key pair(s) to the output `keyPairs`'.format(len(key_pairs)))
relay.outputs.set('keyPairs', key_pairs)