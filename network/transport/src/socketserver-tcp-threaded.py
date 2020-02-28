import socket
import threading
from socketserver import ThreadingTCPServer, BaseRequestHandler


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1337


class RequestHandler(BaseRequestHandler):
    def handle(self):
        received = self.request.recv(1024).decode()
        print(f'From: {self.client_address}/TCP, received: "{received}"')

        response = 'Thanks'
        self.request.sendto(response.encode(), self.client_address)


def send_message(server_host, server_port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_host, server_port))
        sock.sendall(message.encode())
        response = sock.recv(1024).decode()
        print(f'Received: {response}')


with ThreadingTCPServer((SERVER_HOST, SERVER_PORT), RequestHandler) as server:
    # Start a thread with the server -- that thread will then start one more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)

    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print(f'Server loop running in thread: {server_thread.name}')

    send_message(SERVER_HOST, SERVER_PORT, 'Hello World 1')
    send_message(SERVER_HOST, SERVER_PORT, 'Hello World 2')
    send_message(SERVER_HOST, SERVER_PORT, 'Hello World 3')

    server.shutdown()

