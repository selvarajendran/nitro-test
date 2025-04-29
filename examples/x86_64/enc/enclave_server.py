import socket
import os
import re
import boto3

pod_name = os.getenv("POD_NAME", "unknown-0")

kms_client = boto3.client('kms', region_name='us-east-1')  # Specify your region here

plaintext = b"Hello, this is a secret message!"

# Encrypt the data
response = kms_client.encrypt(
    KeyId='arn:aws:kms:us-east-1:798842239772:key/mrk-965d65eaa5cb4ca2b49cea0bea3ae2e1',  # Replace with your actual key ARN
    Plaintext=plaintext
)

ciphertext_blob = response['CiphertextBlob']

print("Encrypted data", ciphertext_blob)

print("pod_name:", pod_name)

# List of ports (define as per requirement)
PORTS = [5005, 5006, 5007, 5008, 5009]

# Extract the index from the pod name
match = re.search(r"-(\d+)$", pod_name)
if match:
    index = int(match.group(1))
else:
    index = 0  # Default index if extraction fails

print("index:", index)

#VSOCK_PORT = 5005  # Choose a port for communication

VSOCK_PORT = PORTS[index % len(PORTS)]

print("VSOCK_PORT:", VSOCK_PORT)

#VSOCK_PORT = 5005  # Choose a port for communication

# Create a vsock server socket
server = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
server.bind((socket.VMADDR_CID_ANY, VSOCK_PORT))
server.listen(1)

print(f"Enclave listening on vsock port {VSOCK_PORT}...")

while True:
    try:
        conn, _ = server.accept()
        data = conn.recv(1024)
        print("Received:", data.decode())
        conn.sendall(b"Hello from Enclave!")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)  # Prevent high CPU usage if looping
