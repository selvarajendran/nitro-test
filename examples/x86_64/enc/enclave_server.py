import boto3
from botocore.config import Config

# This config uses the vsock-proxy running on port 8000
config = Config(
    region_name='us-east-1',
    retries={'max_attempts': 3},
    endpoint_url='http://127.0.0.1:8000',  # vsock proxy to KMS
    signature_version='v4'
)

# Create a KMS client
kms = boto3.client('kms', config=config)

# Example: Encrypt something
response = kms.encrypt(
    KeyId='alias/mrk-965d65eaa5cb4ca2b49cea0bea3ae2e1',
    Plaintext=b'hello enclave'
)

print("Ciphertext blob:", response['CiphertextBlob'])