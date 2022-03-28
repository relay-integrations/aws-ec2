FROM relaysh/core:latest-python
RUN pip --no-cache-dir install boto3
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Delete AWS EC2 images (AMIs)"
LABEL "org.opencontainers.image.description"="This task deletes the EC2 images (AMIs) in a given region."
LABEL "sh.relay.sdk.version"="v1"
