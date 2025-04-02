import socket

VSOCK_PORT = 5005  # Choose a port for communication

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
