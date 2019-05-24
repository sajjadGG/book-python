import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337
PAYLOAD = 'Hello World'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    print(f'Connecting to {SERVER_HOST}:{SERVER_PORT}/TCP')
    sock.connect((SERVER_HOST, SERVER_PORT))

    print(f'Sending: "{PAYLOAD}"')
    sock.sendall(PAYLOAD.encode())

    data = sock.recv(1024).decode()
    print(f'Received: "{data}"')
