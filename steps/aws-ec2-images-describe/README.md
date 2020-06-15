# aws-ec2-images-describe

This [AWS EC2](https://aws.amazon.com/ec2/) step container lists the images
in an AWS region that are owned by my account and sets an output, `images`, to an 
array containing information about them. 


## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `images` | array of mappings | The images in the given region owned by the provided account. |

## Example

```yaml
steps:
# ...
- name: describe-images
  image: relaysh/aws-ec2-images-describe
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
```

## Example output `images`

```
[
   {
      "Architecture":"x86_64",
      "CreationDate":"2019-12-13T00:28:44.000Z",
      "ImageId":"ami-0297d6e616d4e04b2",
      "ImageLocation":"180094860577/my-ec2-image-7fe0c3b",
      "ImageType":"machine",
      "Public":False,
      "OwnerId":"180094860577",
      "PlatformDetails":"Linux/UNIX",
      "UsageOperation":"RunInstances",
      "ProductCodes":[
         {
            "ProductCodeId":"awdfeefkw8e5c1q413zgy5pjce",
            "ProductCodeType":"marketplace"
         }
      ],
      "State":"available",
      "BlockDeviceMappings":[
         {
            "DeviceName":"/dev/sda1",
            "Ebs":{
               "DeleteOnTermination":True,
               "SnapshotId":"snap-0afbb7dae94dfbeb8",
               "VolumeSize":32,
               "VolumeType":"gp2",
               "Encrypted":False
            }
         },
         {
            "DeviceName":"/dev/sdb",
            "Ebs":{
               "DeleteOnTermination":True,
               "SnapshotId":"snap-03f20f8f543969dd8",
               "VolumeSize":100,
               "VolumeType":"gp2",
               "Encrypted":False
            }
         }
      ],
      "Description":"My EC2 golden image-7fe0c3b (x86_64)",
      "EnaSupport":True,
      "Hypervisor":"xen",
      "Name":"my-ec2-image-7fe0c3b",
      "RootDeviceName":"/dev/sda1",
      "RootDeviceType":"ebs",
      "SriovNetSupport":"simple",
      "VirtualizationType":"hvm"
   }
]
```