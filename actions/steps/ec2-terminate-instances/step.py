#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D


ni = Interface()

sess = boto3.Session(
  aws_access_key_id=ni.get(D.aws.accessKeyID),
  aws_secret_access_key=ni.get(D.aws.secretAccessKey),
  region_name=ni.get(D.aws.region),
)
ec2 = sess.resource('ec2')

instanceIDs = ni.get(D.instanceIDs)
if len(instanceIDs) > 0:
    ec2.instances.filter(InstanceIds=instanceIDs).terminate()
