#!/usr/bin/env python3

import queue
import threading
import time

global_exit_flag = 0


class myThread (threading.Thread):

    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting %s" % self.name)
        process_data(self.name, self.q)
        print("Exiting %s" % self.name)


def process_data(threadName, q):
    while not global_exit_flag:
        queue_lock.acquire()

        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queue_lock.release()

        time.sleep(1)


thread_names = ["Thread-1", "Thread-2", "Thread-3"]
jobs = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1


# Create new threads
for name in thread_names:
    thread = myThread(thread_id, name, work_queue)
    thread.start()
    threads.append(thread)
    thread_id += 1


# Fill the queue
queue_lock.acquire()
for word in jobs:
    work_queue.put(word)
queue_lock.release()


# Wait for queue to empty
while not work_queue.empty():
    pass

# Notify threads it's time to exit
global_exit_flag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exiting Main Thread")
