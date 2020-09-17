# aws-ec2-step-instances-reboot

This [AWS EC2](https://aws.amazon.com/ec2/) step container requests that the a
set of given instances reboot immediately.

## Example

```yaml
steps:
# ...
- name: ec2-reboot-instances
  image: relaysh/aws-ec2-step-instances-reboot
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    instanceIDs:
    - i-0123456789abcdef0
    - i-abcdef0123456789a
```
