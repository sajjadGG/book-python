#!/usr/bin/env python3

import queue
import logging
import threading


TODO = ['ping', 'ls -la', 'echo']
q = queue.Queue()


def do_work(work):
    logging.warning('Will do the work: %s' % work)


def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


def spawn_workers(number_of_workers):
    for i in range(number_of_workers):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()


def populate_queue(todo):
    for item in TODO:
        q.put(item)


if __name__ == '__main__':
    spawn_workers(3)
    populate_queue(TODO)

    # wait to complete all tasks
    q.join()

