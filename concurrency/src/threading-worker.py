from queue import Queue
import logging
from threading import Thread


class Worker(Thread):
    def run(self):
        while True:
            # Remove and return an item from the queue.
            job = work_queue.get()

            # Execute work
            logging.warning(f'Will do the work: {job}')

            # Indicate that a formerly enqueued task is complete.
            work_queue.task_done()


def spawn_worker(count=1):
    for i in range(count):
        Worker().start()


if __name__ == '__main__':
    work_queue = Queue()
    spawn_worker(3)

    TODO = [
        'ping',
        'ls -la',
        'echo "hello world"',
        'cat /etc/passwd'
    ]

    # Schedule tasks to do
    for todo in TODO:
        work_queue.put(todo)

    # wait to complete all tasks
    work_queue.join()
