import subprocess
from shlex import shlex
from queue import Queue
from threading import Timer

TIMEOUT = 2.0
DELAY = 5.0
TODO = [
    'ping python.astrotech.io',
    'ls -la',
    'echo "hello world"',
    'cat /etc/passwd',
]

work_queue = Queue()


def run():
    while True:
        cmd = work_queue.get()
        cmd = shlex(cmd)

        try:
            subprocess.run(cmd, timeout=TIMEOUT, shell=True)
        except subprocess.TimeoutExpired:
            print('Timeout')

        work_queue.task_done()


t = Timer(DELAY, run)
t.start()

# Zapełnij kolejkę
for todo in TODO:
    work_queue.put(todo)

# wait to complete all tasks
print('before join')
t.join(timeout=TIMEOUT)
print('afer join')

print('done.')
