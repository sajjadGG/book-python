**************
Multithreading
**************


Threads vs processes
====================

Process
-------
#. Co to jest proces?
#. Ile czasu trwa tworzenie procesów?
#. Kto zarządza procesami?
#. Ile może być równoległych procesów?
#. Co to jest ``nice``
#. Jak komunikować się między procesami?

Thread
------
#. Co to jest wątek?
#. Ile czasu trwa tworzenie wątków?
#. Kto zarządza wątkami?
#. Ile może być równoległych wątków?
#. Ile wątków może być w ramach jednego procesu?
#. Jak komunikować się między wątkami?
#. Czy współdzielenie pamięci przez wątki jest dobre czy złe?

Threads vs processes
--------------------
#. Czym się różnią wątki od procesów?
#. Ile może być wątków przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Ile może być procesów przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Jak na wątki i procesy wpływa GIL?


Problemy z wątkami
==================
* Zakleszczania
* Race Condition
* Głodzenie
* Problem 5 filozofów:

    * 5 filozofów (albo rozmyśla, albo je)
    * 5 misek ze spaghetti,
    * 5 widelców,
    * 2 widelce potrzebne aby zjeść,
    * problem zakleszczania

* Problem producenta i konsumenta
* Problem czytelników i pisarzy

``threading``
=============

``daemon`` flag
---------------
* https://stackoverflow.com/a/190017/228517

Some threads do background tasks, like sending keepalive packets, or performing periodic garbage collection, or whatever. These are only useful when the main program is running, and it's okay to kill them off once the other, non-daemon, threads have exited.

Without daemon threads, you'd have to keep track of them, and tell them to exit, before your program can completely quit. By setting them as daemon threads, you can let them run and forget about them, and when your program quits, any daemon threads are killed automatically.

Delay execution
---------------
* dlaczego nie ``time.sleep()``
* rekurencyjny timer

.. code-block:: python
    :caption: Delay execution

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Hello world!')


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')


Recurrent timer
---------------
.. code-block:: python
    :caption: Recurrent timer

    from threading import Timer


    DELAY_SECONDS = 5.0

    def hello():
        print('Timer Thread')
        Timer(DELAY_SECONDS, hello).start()


    t = Timer(DELAY_SECONDS, hello)
    t.start()

    print('Main Thread')

Tworzenie wątków
================
.. code-block:: python

    from threading import Thread


    class MyThread(Thread):
        def run(self):
            print('hello')


    t = MyThread()
    t.start()


Synchronizacja wątków
=====================
.. code-block:: python

    from threading import Thread


    class MyThread(Thread):
        def run(self):
            print('hello')


    t1 = MyThread()
    t1.start()

    t2 = MyThread()
    t2.start()

    t1.join()
    t2.join()

.. code-block:: python

    from threading import Thread

    RUNNING = []


    class MyThread(Thread):
        def run(self):
            print('hello')


    t1 = MyThread()
    t1.start()
    RUNNING.append(t1)

    t2 = MyThread()
    t2.start()
    RUNNING.append(t2)

    for thread in RUNNING:
        thread.join()

.. code-block:: python

    from threading import Thread

    RUNNING = []


    class MyThread(Thread):
        def run(self):
            print('hello')


    def spawn(cls, count=1):
        for i in range(count):
            t = cls()
            t.start()
            RUNNING.append(t)


    spawn(MyThread, count=10)


    for thread in RUNNING:
        thread.join()


Zamykanie wątków
================
.. code-block:: python
    :caption: Synchronizacja wątków

    from queue import Queue
    from threading import Thread, Lock
    from time import sleep


    EXIT = False
    LOCK = Lock()
    TODO = Queue()
    RUNNING = []


    class MyThread(Thread):
        def run(self):
            while not EXIT:
                # Remove and return an item from the queue.
                job = TODO.get()

                # Execute work
                print(f'Will do the work: {job}')

                # Indicate that a formerly enqueued task is complete.
                TODO.task_done()
                sleep(1)

            print(f'Exiting {self.name}')


    # Create new threads
    def spawn_worker(count=1):
        for i in range(count):
            thread = MyThread()
            thread.start()
            RUNNING.append(thread)


    if __name__ == '__main__':
        spawn_worker(5)

        # Fill the queue
        with LOCK:
            for task in ['One', 'Two', 'Three', 'Four', 'Five']:
                TODO.put(task)

        # Wait for queue to empty
        while not TODO.empty():
            pass

        # Notify threads it's time to exit
        EXIT = True

        # Wait for all threads to complete
        for thread in RUNNING:
            thread.join()

        print(f'Exiting Main Thread')


Workery
=======
.. code-block:: python
    :caption: Model Workerów

    from queue import Queue
    from threading import Thread

    TODO = Queue()


    class Worker(Thread):
        def run(self):
            while True:
                # Remove and return an item from the queue.
                job = TODO.get()

                # Execute work
                print(f'Will do the work: {job}')

                # Indicate that a formerly enqueued task is complete.
                TODO.task_done()


    def spawn_worker(count=1):
        for i in range(count):
            Worker().start()


    if __name__ == '__main__':
        spawn_worker(3)

        TODO.put('ping')
        TODO.put('ls -la')
        TODO.put('echo "hello world"')
        TODO.put('cat /etc/passwd')

        # wait to complete all tasks
        TODO.join()


Assignments
===========

Wielowątkowość
--------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 30 min
* Solution: :download:`solution/threading_timer.py`

#. Stwórz kolejkę ``queue`` do której dodasz różne polecenia systemowe do wykonania, np.:

    * Linux/macOS: ``['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']``,
    * Windows: ``['dir c:\\Users', 'echo "test"', 'type %HOMEPATH%\Desktop\README.txt']``.

#. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki
#. Wątki powinny być uruchamiane jako ``subprocess.run()`` w systemie operacyjnym z timeoutem równym ``TIMEOUT = 2.0`` sekundy
#. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
#. Wątki mają być uruchomione w tle (ang. ``daemon``)

:Extra task:
    #. Wątki powinny być uśpione za pomocą ``Timer`` przez ``DELAY = 5.0`` sekund, a następnie ruszyć do roboty
    #. Parametry rozbij za pomocą ``shlex``
    #. Użyj logowania za pomocą biblioteki ``logging`` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku.

:Hint:
    Ustaw parametr ``shell=True`` dla ``subprocess.run()``
