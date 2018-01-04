************************
Kolejki, wątki i procesy
************************

Kolejki - Queue
===============

FIFO
----

LIFO (stack)
------------

Network Queue
-------------

* Synchronizacja
* Routing

Priority Queue
--------------

* Priorytetyzacja
* Wywłaszczenie

Wątki a procesy
===============

* Czym się różnią wątki od procesów?
* Ile wątków może być w ramach procesów?
* Jak komunikować się między wątkami?
* Jak komunikować się między procesami?
* Ile może być wątków na procesorze czterordzeniowym (z i bez Hyper Threading)?
* Ile może być procesów na procesorze czterordzeniowym (z i bez Hyper Threading)?

Wątki
=====

Tworzenie wątków
----------------

.. code-block:: python

    from threading import Timer


    def hello():
        print('Timer Thread')

    t = Timer(5.0, hello)
    t.start()

    print('Main Thread')

Synchronizacja wątków
---------------------

.. code-block:: python

    import queue
    import threading
    import time


    class MyThread(threading.Thread):

        def __init__(self, thread_name, work_queue):
            self.thread_name = thread_name
            self.work_queue = work_queue
            super().__init__()

        def run(self):
            print(f'Starting {self.thread_name}')

            while not exit_flag:
                lock.acquire()

                if not work_queue.empty():
                    data = work_queue.get()
                    lock.release()

                    # Release Queue before processing
                    print(f'{self.thread_name} processing {data}')
                else:
                    lock.release()

                time.sleep(2)

            print(f'Exiting {self.thread_name}')


    exit_flag = 0
    lock = threading.Lock()
    work_queue = queue.Queue()
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


Zamykanie wątków
----------------

Workery
-------

.. code-block:: python

    import queue
    import logging
    import threading


    work_queue = queue.Queue()


    class Worker(threading.Thread):
        daemon = True

        def run(self):
            while True:
                # Remove and return an item from the queue.
                job = work_queue.get()

                # Execute work
                logging.warning('Will do the work: %s' % job)

                # Indicate that a formerly enqueued task is complete.
                work_queue.task_done()


    def spawn_worker(how_many):
         for i in range(how_many):
            Worker().start()


    if __name__ == '__main__':
        spawn_worker(3)

        # Zapełnij kolejkę
        for todo in ['ping', 'ls -la', 'echo "hello world"', 'cat /etc/passwd']:
            work_queue.put(todo)

        # wait to complete all tasks
        work_queue.join()



Procesy
=======

Tworzenie procesów
------------------

Synchronizacja procesów
-----------------------

IPC - komunikacja międzyprocesowa
---------------------------------

:figury.py:
    .. code-block:: python

        class Prostokat:

            def __init__(self, a, b):
                self.a = float(a)
                self.b = float(b)

            def pole(self):
                return self.a * self.b

            def obwod(self):
                return (self.a + self.b) * 2

            def __str__(self):
                return 'Prostokat(a=%s, b=%s)' % (self.a, self.b)

:processes-client.py:
    .. code-block:: python

        from multiprocessing.connection import Client
        import logging
        import pickle
        from .figury import Prostokat


        rectangle = Prostokat(a=5, b=10)
        rect = pickle.dumps(rectangle)

        address = ('localhost', 6000)
        conn = Client(address, authkey=b'secret password')

        logging.warning('Sending objects')
        conn.send([rect, 'a', 2.5, None, int, sum])

        logging.warning('Sending close')
        conn.send('close')

        conn.close()

:processes-listener.py:
    .. code-block:: python

        from multiprocessing.connection import Listener
        import logging
        import pickle
        from .figury import Prostokat


        address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

        logging.warning('Listening on %s:%s' % address)
        listener = Listener(address, authkey=b'secret password')
        conn = listener.accept()

        logging.warning('connection accepted from %s %s' % listener.last_accepted)


        while True:
            msg = conn.recv()
            logging.warning('Received: %s' % msg)

            if msg == 'close':
                conn.close()
                break
            else:
                # do something with msg
                prostokat = pickle.loads(msg[0])
                logging.warning('Prostokat %s' % prostokat)
                print('Pole: %s' % prostokat.pole())


        listener.close()




Zamykanie procesów
------------------

Zadania kontrolne
=================

Wielowątkowość
--------------

* Stwórz kolejkę ``queue`` do której dodasz różne polecenia systemowe do wykonania, np. ``['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']``.
* Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki.
* Wątki powinny być uruchamiane jako ``subprocess`` w systemie operacyjnym z timeoutem równym ``PROCESSING_TIMEOUT = 2.0`` sekundy
* Ilość poleceń może się zwiększać w miarę wykonywania zadania.
* Wątki powinny być uśpione za pomocą ``Timer`` przez 5.0 sekund, a następnie ruszyć do roboty.
* Wątki mają być uruchomione w tle (ang. ``daemon``)
* Użyj logowania za pomocą biblioteki ``logging`` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku
* Napisz testy do workerów i kolejki

:Podpowiedź:
    .. code-block:: python

        import subprocess
        import shlex

        cmd = 'ls -la'

        with subprocess.Popen(shlex.split(cmd), stdout=PIPE) as proc:
            log.write(proc.stdout.read())
