# aws-ec2-step-key-pairs-describe

This [AWS EC2](https://aws.amazon.com/ec2/) step container lists the key pairs
in an AWS account and sets an output, `keyPairs`, to an array of key pairs in the
provided region and account. 

## Example output `keyPairs`

```
[
   {
      "KeyPairId":"key-0461aba76417b0ae2",
      "KeyFingerprint":"fe:3d:15:2a:a1:ec:91:32:7b:85:33:53:94:d6:96:f5:0b:cd:a2:11",
      "KeyName":"key.pair.1",
      "Tags":[

      ]
   },
   {
      "KeyPairId":"key-0cf8de6e83054c972",
      "KeyFingerprint":"1a:c2:d9:75:e4:e3:7f:7d:39:66:c2:32:25:f6:3f:12",
      "KeyName":"key.pair.2",
      "Tags":[

      ]
   }
]
```