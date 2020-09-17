# aws-ec2-step-instances-stop

This [AWS EC2](https://aws.amazon.com/ec2/) step container requests that the a
set of given instances stop immediately.

## Example

```yaml
steps:
# ...
- name: ec2-stop-instances
  image: relaysh/aws-ec2-step-instances-stop
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    instanceIDs:
    - i-0123456789abcdef0
    - i-abcdef0123456789a
```
