#!/usr/bin/env python3

import socketserver
import sys
import logging

from __init__ import COMMAND_CENTER_HOST
from __init__ import COMMAND_CENTER_PORT

from command_center_panel.models.hosts import Host
from command_center_panel.models.logs import Log


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            ip = self.client_address[0]
            port = self.client_address[1]
            msg = self.request[0].strip()

            logging.info('Response received from %s:%s' % (ip, port))
            Log(host=Host.objects.get(ip=ip, port=port), log=msg).save()

        except Exception:
            pass


if __name__ == '__main__':
    addr = (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT + 2)

    logging.info('Listening for logs on %s...', addr)
    listener = socketserver.UDPServer(addr, UDPHandler)

    try:
        listener.serve_forever()
    except KeyboardInterrupt:
        sys.exit()
