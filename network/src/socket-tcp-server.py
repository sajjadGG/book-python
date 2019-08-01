import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    print(f'Listening on {SERVER_HOST}:{SERVER_PORT}/TCP...')
    sock.bind((SERVER_HOST, SERVER_PORT))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()

        received = conn.recv(1024).decode()
        print(f'From: {addr}, received: "{received}"')

        response = 'Thanks'
        conn.sendall(response.encode())

        if not received:
            print(f'Client {addr} disconnected.')
            conn.close()
