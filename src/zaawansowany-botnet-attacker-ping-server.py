import logging
import socketserver

HOST = 'localhost'
PORT = 31337


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.attacker.ping.server')


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        log.info('Received ping from %s:%s' % self.client_address)


if __name__ == '__main__':
    logging.info('Listening for pings on %s...', (HOST, PORT))
    listener = socketserver.UDPServer((HOST, PORT), UDPHandler)

    listener.serve_forever()
