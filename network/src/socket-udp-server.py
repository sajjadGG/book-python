import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    print(f'Listening on {SERVER_HOST}:{SERVER_PORT}/UDP...')
    sock.bind((SERVER_HOST, SERVER_PORT))

    while True:
        received, addr = sock.recvfrom(1024)
        received = received.decode()

        print(f'From: {addr}, received: "{received}"')
