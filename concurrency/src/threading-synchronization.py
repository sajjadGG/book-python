from queue import Queue
from threading import Thread, Lock
from time import sleep


class MyThread(Thread):
    def __init__(self, thread_name, work_queue):
        self.thread_name = thread_name
        self.work_queue = work_queue
        super().__init__()

    def run(self):
        print(f'Starting {self.thread_name}')

        while not exit_flag:
            lock.acquire()

            if not self.work_queue.empty():
                data = work_queue.get()
                lock.release()

                # Release Queue before processing
                print(f'{self.thread_name} processing {data}')
            else:
                lock.release()

            sleep(1)

        print(f'Exiting {self.thread_name}')


exit_flag = 0
lock = Lock()
work_queue = Queue()
running_threads = []

# Create new threads
for name in ['Thread-1', 'Thread-2', 'Thread-3']:
    thread = MyThread(name, work_queue)
    thread.start()
    running_threads.append(thread)

# Fill the queue
lock.acquire()
for word in ['One', 'Two', 'Three', 'Four', 'Five']:
    work_queue.put(word)
lock.release()

# Wait for queue to empty
while not work_queue.empty():
    pass

# Notify threads it's time to exit
exit_flag = 1

# Wait for all threads to complete
for thread in running_threads:
    thread.join()

print(f'Exiting Main Thread')
