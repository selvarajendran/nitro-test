FROM alpine:latest

RUN apk add --no-cache python3 py3-pip
COPY enclave_server.py /app/enclave_server.py

CMD ["python3", "/app/enclave_server.py"]
