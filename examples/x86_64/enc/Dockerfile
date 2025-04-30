FROM amazonlinux:2

# Install base dependencies
RUN yum install -y \
    python3 \
    python3-pip \
    git \
    gcc \
    make \
    protobuf-devel \
    grpc-devel \
    openssl-devel \
    cmake \
    ca-certificates \
 && update-ca-trust force-enable \
 && update-ca-trust extract \
 && yum clean all

# Clone and install Nitro Enclaves Python SDK
RUN git config --global http.sslVerify false \
 && git clone https://github.com/aws/aws-nitro-enclaves-sdk-python.git /sdk \
 && cd /sdk \
 && pip3 install .

# Copy your enclave app
COPY enclave_server.py /app/enclave_server.py
WORKDIR /app

ENTRYPOINT ["python3", "enclave_server.py"]
