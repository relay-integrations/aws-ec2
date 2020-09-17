# aws-ec2-step-instances-terminate

This [AWS EC2](https://aws.amazon.com/ec2/) step container terminates a given
set of EC2 instances.

## Example

```yaml
steps:
# ...
- name: ec2-terminate-instances
  image: relaysh/aws-ec2-step-instances-terminate
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    instanceIDs:
    - i-0123456789abcdef0
    - i-abcdef0123456789a
```
