#!/usr/bin/env python3

import queue
import logging
import threading


kolejka = queue.Queue()


class Worker(threading.Thread):
    daemon = True

    def run(self):
        while True:
            job = kolejka.get()

            # Tutaj wykonaj pracę
            logging.warning('Will do the work: %s' % job)

            kolejka.task_done()


def spawn_workers(number_of_workers):
    for i in range(number_of_workers):
        Worker().start()


if __name__ == '__main__':
    spawn_workers(3)

    # Zapełnij kolejkę
    for todo in ['ping', 'ls -la', 'echo "hello world"', 'cat /etc/passwd']:
        kolejka.put(todo)

    # wait to complete all tasks
    kolejka.join()

