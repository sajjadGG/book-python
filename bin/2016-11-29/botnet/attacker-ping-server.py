import logging
import socketserver


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.attacker.ping.server')


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        log.info('Received ping from %s:%s' % self.client_address)


if __name__ == '__main__':
    addr = ('localhost', 31337)

    logging.info('Listening for pings on %s...', addr)
    listener = socketserver.UDPServer(addr, UDPHandler)

    listener.serve_forever()
