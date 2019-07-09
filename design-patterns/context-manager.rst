****************
Context Managers
****************


About Context Managers
======================

Zastosowanie
------------
* Pliki
* Buforowanie danych
* Połączenia do bazy danych
* Transakcje w bazie danych
* Cursory w bazie danych
* Lock
* Stream sieciowe
* Komunikacja po socketach

How to create
-------------
* ``__enter__(self, *args, **kwargs) -> self``
* ``__exit__(self, *args, **kwargs) -> None``

.. code-block:: python
    :caption: How to create Context Managers

    class MyClass:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def hello(self):
            print('hello')


    with MyClass() as cls:
        cls.hello()


Examples
========

Files
-----
.. code-block:: python

    f = open(FILE)
    # ...
    f.close()

.. code-block:: python

    with open(FILE) as file:
        # ...

Database
--------
.. code-block:: python

    import sqlite3


    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT)"""
    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'
    SQL_SELECT = 'SELECT * from astronauts'


    astronauts = [
        {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '61041212346', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
    ]


    with sqlite3.connect(':memory:') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, astronauts)

        for row in db.execute(SQL_SELECT):
            print(row)

Lock
----
.. code-block:: python

    import threading


    lock = threading.Lock()

    with lock:
        my_list.append(item)

replaces the more verbose:

.. code-block:: python

    import threading


    lock = threading.Lock()
    lock.acquire()

    try:
        my_list.append(item)
    finally:
        lock.release()


Contextmanager decorator
========================
* Dzieli naszą funkcję na bloki przed i po ``yield``
* Bloki przed traktuje jako ``__enter__()``
* Bloki za traktuje jako ``__exit__()``

``contextmanager`` decorator
----------------------------
.. code-block:: python

    from contextlib import contextmanager
    import time


    @contextmanager
    def MicroBenchmark():
        start_time = time.time()
        yield
        end_time = time.time()
        duration = end_time - start_time
        print(f'Duration {duration:.4f} seconds')


    with MicroBenchmark():
        max = int(1e8)
        list(range(max))

    # Duration 3.4540 seconds

``ContextDecorator`` class
--------------------------
.. code-block:: python

    from contextlib import ContextDecorator
    import time


    class MicroBenchmark(ContextDecorator):
        def __enter__(self):
            self.start_time = time.time()
            return self

        def __exit__(self, *args):
            end_time = time.time()
            duration = end_time - start_time
            print(f'Duration {duration:.4f} seconds')


    @MicroBenchmark()
    def my_function():
        max = int(1e8)
        list(range(max))


    my_function()
    # Duration 3.3507 seconds


Use Case
--------
.. code-block:: python

    from contextlib import contextmanager


    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")


    with tag("p"):
        print("foo")

    # <p>
    # foo
    # </p>



Assignments
===========

Buffered file
-------------
* Filename: :download:`solution/context_manager_file.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min

#. Stwórz Context Manager dla zapisu do plików
#. Context Manager buforuje dane (nie zapisuje ich na bieżąco)
#. Gdy program wyjdzie z bloku context managera, to nastąpi otwarcie pliku, zapisanie do pliku i jego zamknięcie

.. code-block:: python

    FILENAME = '/tmp/context-manager.txt'

    class File:
        pass


    with File(FILENAME) as file:
        file.append_line(...)
        file.append_line(...)
        file.append_line(...)

    # after block with exits, save to file
