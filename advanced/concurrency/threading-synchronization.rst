Threading Synchronization
=========================


Rationale
---------
* Thread Synchronisation


Locks
-----
* Locks don't lock anything. They are just flags and can be ignored. It is a cooperative tool, not an enforced tool
* IIn general, locks should be considered a low level primitive that is difficult to reason about nontrivial examples. For more complex applications, you're almost always better of with using atomic message queues.
* The more locks you acquire at one time, the more you loose the advantages of concurrency

Source: [#Hettinger2017]_


Example
-------
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
