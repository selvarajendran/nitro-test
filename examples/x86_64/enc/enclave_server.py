from aws_kms import AwsKmsClient
import base64

# Port should match the port where kms-server is running (on the host)
VSOCK_PORT = 8001  # default port for kms-server
KEY_ID = "arn:aws:kms:us-east-1:798842239772:key/mrk-965d65eaa5cb4ca2b49cea0bea3ae2e1"

def main():
    # Connect to KMS server on host via vsock
    client = AwsKmsClient(vsock_port=VSOCK_PORT)

    # Request to generate a data key
    print("[*] Requesting data key from KMS...")
    response = client.generate_data_key(key_id=KEY_ID, key_spec='AES_256')

    # Encrypted key (can be stored)
    encrypted_key_b64 = base64.b64encode(response['CiphertextBlob']).decode()
    print("[+] Encrypted data key (base64):", encrypted_key_b64)

    # Plaintext key (use this for actual encryption, but don’t store it!)
    plaintext_key = base64.b64encode(response['Plaintext']).decode()
    print("[+] Plaintext data key (base64):", plaintext_key)

if __name__ == "__main__":
    main()
