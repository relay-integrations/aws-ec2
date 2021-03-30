FROM relaysh/core:latest-python
RUN pip --no-cache-dir install boto3
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Describe AWS EC2 Key Pairs"
LABEL "org.opencontainers.image.description"="This task describes the EC2 Key Pairs in a given account."
LABEL "sh.relay.sdk.version"="v1"
