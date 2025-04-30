FROM alpine:latest

RUN apk add --no-cache python3 py3-pip
#RUN pip install --no-cache-dir boto3

RUN pip install --no-cache-dir --break-system-packages boto3

RUN pip install --no-cache-dir --break-system-packages aws-nitro-enclaves-sdk

COPY enclave_server.py /app/enclave_server.py

CMD ["python3", "/app/enclave_server.py"]
