FROM amazonlinux:2

# Install dependencies
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
    && yum clean all

# Clone and install aws-nitro-enclaves-sdk-python
RUN git clone https://github.com/aws/aws-nitro-enclaves-sdk-python.git /sdk \
    && cd /sdk \
    && pip3 install .

# Copy your enclave app
COPY enclave_server.py /app/enclave_server.py
WORKDIR /app

ENTRYPOINT ["python3", "enclave_server.py"]
