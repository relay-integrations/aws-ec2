FROM relaysh/core:latest-python
RUN pip --no-cache-dir install boto3
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Terminates AWS EC2 instances"
LABEL "org.opencontainers.image.description"="This task terminates a given list of EC2 instances."
LABEL "sh.relay.sdk.version"="v1"
