import boto3
from botocore.config import Config

# Only valid config keys in Config constructor
config = Config(
    region_name='us-east-1',
    retries={'max_attempts': 3}
)

# Specify the vsock proxy endpoint here
kms = boto3.client(
    'kms',
    endpoint_url='http://127.0.0.1:8000',  # Local vsock proxy to KMS
    config=config
)

response = kms.encrypt(
    KeyId='alias/mrk-965d65eaa5cb4ca2b49cea0bea3ae2e1',
    Plaintext=b'hello enclave'
)

print("Encrypted:", response['CiphertextBlob'])
