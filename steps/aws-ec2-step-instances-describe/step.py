#!/usr/bin/env python
import re
from functools import partial

import boto3
import requests
from relay_sdk import Dynamic as D
from relay_sdk import Interface


def instance_to_dict(ec2, instance):
    shape = ec2.meta.client.meta.service_model.shape_for('Instance')
    attrs = instance.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(instance, mapped)

    return d


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

list_of_filters = []
try:
  pattern = re.compile(r'(?<!^)(?=[A-Z])')

  raw_filters = relay.get(D.filters)
  for key, value in raw_filters.items():
    f = {}
    f['Name'] = pattern.sub('-', key).lower()
    f['Values'] = [value]
    list_of_filters.append(f)
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 422:
        pass
    else:
        raise
  
ec2 = sess.resource('ec2')

# Get instances
raw_instances = None
if (len(list_of_filters) != 0): 
  raw_instances = ec2.instances.filter(Filters=list_of_filters)
else: 
  raw_instances = ec2.instances.all()

instance_list = [instance for instance in raw_instances]
if (len(instance_list) == 0):
    relay.outputs.set('instances', list())
    print("No instances found")
    exit(0)

print('Found the following EC2 instances:\n')
print("{:<30} {:<30} {:<30}".format('ID', 'STATE', 'TYPE'))
for instance in raw_instances:
  print("{:<30} {:<30} {:<30}".format(instance.instance_id, instance.state['Name'], instance.instance_type))
instances = list(map(partial(instance_to_dict, ec2), raw_instances))

print('\nAdding {0} instance(s) to the output `instances`'.format(len(instances)))
relay.outputs.set('instances', instances)
