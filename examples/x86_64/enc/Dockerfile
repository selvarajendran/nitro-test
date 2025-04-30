FROM amazonlinux:2

RUN yum install -y \
    python3 \
    python3-pip \
    git \
    gcc \
    make \
    unzip \
    curl \
    protobuf-devel \
    grpc-devel \
    openssl-devel \
    cmake \
    ca-certificates \
 && update-ca-trust force-enable \
 && update-ca-trust extract \
 && yum clean all

# Download SDK
RUN curl -L -o sdk.zip https://github.com/aws/aws-nitro-enclaves-sdk-python/archive/refs/heads/main.zip \
    && unzip sdk.zip \
    && cd aws-nitro-enclaves-sdk-python-main \
    && pip3 install .

COPY enclave_server.py /app/enclave_server.py
WORKDIR /app
ENTRYPOINT ["python3", "enclave_server.py"]
