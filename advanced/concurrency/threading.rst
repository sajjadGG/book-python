**************
Multithreading
**************


Classification of concurrency problems
======================================
* Martelli Model of Scalability
* 1 core: Single thread and single process
* 2-8 cores: Multiple threads and multiple processes
* 9+ cores: Distributed processing

Martelli's observation: As time goes on, the second category becomes less common and relevant.
Single cores become more powerful. Big datasets grow ever larger [to use 2-8 cores].

Source: [Hettinger2017]_

GIL
===
* Global Interpreter Lock
* CPython has a lock for its internal shared global state
* One lock insteads of hundreds smaller
* The unfortunate effect of GIL is that no more than one thread can run at a time
* For I/O bound applications, GIL doesn't present much of an issue
* For CPU bound applications, using threads makes the application speed worse
* Accordingly, that drives us to multiprocessing to gain more CPU cycles

Source: [Hettinger2017]_


Concurrency Models
==================

Process
-------
#. Co to jest proces?
#. Ile czasu trwa tworzenie procesów?
#. Kto zarządza procesami?
#. Ile może być równoległych procesów?
#. Co to jest ``nice``
#. Jak komunikować się między procesami?

#. Procesy są w pełni niezależne między sobą.
#. Nie trzeba stawiać locków, bo nie wchodzą sobie w grę
#. Działanie jednego nie wpływa na drugi
#. Pamięć jest odseparowana
#. Wadą procesów jest brak komunikacji (dlatego potrzebne są metody IPC, np. pickle)
#. Bardzo duży koszt związany z komunikacją i serializacją

Thread
------
#. Co to jest wątek?
#. Ile czasu trwa tworzenie wątków?
#. Kto zarządza wątkami?
#. Ile może być równoległych wątków?
#. Ile wątków może być w ramach jednego procesu?
#. Jak komunikować się między wątkami?
#. Czy współdzielenie pamięci przez wątki jest dobre czy złe?

* Zaletą wątków jest to, że mają współdzielony stan
* Jeden wątek może zapisać kod do pamięci a drugi odczytać bez narzutu komunikacyjnego
* Wadą jest również współdzielony stan i race condition
* Ideą wątków jest tani dostęp do współdzielonej pamięci, tylko trzeba wszędzie wstawiać locki
* Run very fast, but hard to get correct
* It's insanely difficult to create large multi-threaded programs with multiple locks
* Even if you lock resource, there is no protection if other parts of the system do not even try to acquire the lock
* Threads switch preemptively
* Preemptively means that the thread manager decides to switch tasks for you (you don't have to explicitly say to do so). Programmer has to do very little.
* This is convenient because you dont need to add explicit code to cause a task switch
* The cost of this convenience is that you have to assume a switch can happen at any time
* Accordingly, critical sections have to be a guarded with locks
*The limit on threads is total CPU power minus the cost of tasks switches and synchronization overhead


Source: [Hettinger2017]_

Async
-----
* Disadvantage: Async switches cooperatively, so you do need to add explicit code ``yield`` or ``await`` to cause a task to switch.
* Now you control when tasks switches occur, so locks and other synchronization are no longer needed.
* Also, cost task switches is incredibly low. Calling a pure Python function has more overhead than restarting a generator or awaitable.
* Function builds stack each time it's called, whereas async uses generators underneath, which already has stack created
* This is the cheapest way to task switch
* In terms of speed async servers blows threaded servers in means of thousands
* This means that ``async`` is very cheap
* Disadvantage: Everything you will do need a non-blocking version of just about everything you do (for example ``open()``)
* Accordingly, the async world has a huge ecosystem of support tools.
* Disadvantage: this increases the learning curve
* Coding is easier to get right, than threads
* Disadvantage: create event loop, acquire, crate non-blocking versions of your code
* Disadvantage: You think you know Python, there is a second half to learn (async).
* Async is the future of programming

Threads vs processes
--------------------
#. Czym się różnią wątki od procesów?
#. Ile może być wątków przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Ile może być procesów przetwarzanych równolegle na procesorze czterordzeniowym (z i bez Hyper Threading)?
#. Jak na wątki i procesy wpływa GIL?

Threads vs Async
----------------
* Async maximizes CPU utilization because it has less overhead than threads.
* Threading typically works with existing code and tools as long as locks are added around critical sections
* For complex systems, async is much easier to get right than threads with locks
* Threads require very little tooling (locks and queues)
* Async needs a great deal of tooling (futures, event loops, and non-blocking version of just about everything.

Source: [Hettinger2017]_

Context Switching
-----------------
* Za każdym razem kiedy robisz ``print()`` kod automatycznie wykonuje Context Switch

Testing
-------
* In concurrent programs (threading, multiprocessing) testing can hide bugs and errors
* Some lines of code works so fast, that it requires million runs to make errors to appear
* But if you put ``sleep()`` than errors will show up
* In Internet of Things (IoT) I'd prefer to stand in front of a car which has code written in async way, than a threaded way
* Async is profoundly easier to debug and get it right

Source: [Hettinger2017]_

Rules
-----
#. If step A and B must be run sequentially, put them in the same thread
#. If there is several parallel threads launched and you want to be sure that all are complete, just ``join()`` all of the threads. It's called "barrier". Example: Several programmers make improvements to the website, they has to merge their work, before releasing website to the public.
#. Daemon thread is a service worker, a task which never suppose to finish (by infinite loop). Instead you ``join()`` on the queue itself. It waits until all the requested tasks are marked as being done. Example: a printer sits in the office, it waits for documents, when document arrives, printer prints it, and wait for another job, printer never finish


Source: [Hettinger2017]_


Problemy z wątkami
==================
* Dead Lock (Zakleszczania)
* Race Condition
* Starvation (Głodzenie)
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

References
==========
.. [Hettinger2017] Hettinger, Raymond. Keynote on Concurrency. PyBay 2017. https://youtu.be/9zinZmE3Ogk?t=1243


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
