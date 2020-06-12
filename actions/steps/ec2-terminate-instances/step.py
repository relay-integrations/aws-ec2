#!/usr/bin/env python
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
ec2 = sess.resource('ec2')

instanceIDs = relay.get(D.instanceIDs)
print('Terminating instances: {}'.format(instanceIDs))
if len(instanceIDs) > 0:
    ec2.instances.filter(InstanceIds=instanceIDs).terminate()
