import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    print(f'Connecting to {SERVER_HOST}:{SERVER_PORT}/UDP')
    sock.connect((SERVER_HOST, SERVER_PORT))

    payload = 'Hello World'
    sock.sendall(payload.encode())

    received = sock.recv(1024).decode()
    print(f'Received: {received}')
