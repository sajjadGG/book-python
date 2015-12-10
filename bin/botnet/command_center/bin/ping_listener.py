#!/usr/bin/env python3

import socketserver
import sys
import logging

from __init__ import COMMAND_CENTER_HOST
from __init__ import COMMAND_CENTER_PORT

from command_center_panel.models.hosts import Host
from command_center_panel.models.pings import Ping


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            msg = self.request[0].strip()
            ip, port = msg.split(':')
            logging.info('Ping received from %s' % msg)
        except Exception:
            return

        host, _ = Host.objects.get_or_create(ip=ip, port=port)
        Ping.objects.create(host=host)


if __name__ == '__main__':
    addr = (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT)

    logging.info('Listening for pings on %s...', addr)
    listener = socketserver.UDPServer(addr, UDPHandler)

    listener.serve_forever()
