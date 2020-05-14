#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D


def instance_to_dict(ec2, instance):
    shape = ec2.meta.client.meta.service_model.shape_for('Instance')
    attrs = instance.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(instance, mapped)

    return d


ni = Interface()

sess = boto3.Session(
  aws_access_key_id=ni.get(D.aws.accessKeyID),
  aws_secret_access_key=ni.get(D.aws.secretAccessKey),
  region_name=ni.get(D.aws.region),
)
ec2 = sess.resource('ec2')

instances = list(map(partial(instance_to_dict, ec2), ec2.instances.all()))

print('Adding {0} instance(s) to the output `instances`'.format(len(instances)))
ni.outputs.set('instances', instances)
