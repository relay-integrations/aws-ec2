# aws-ec2-step-images-describe

This [AWS EC2](https://aws.amazon.com/ec2/) step deletes the images (AMIs)
corresponding to the image IDs passed in the input parameter `imageIDs`.

If the parameter `dryRun` is set to `true`, the deletion operation will be simulated but
the images will not be deleted.
