****************
Context Managers
****************


Protocol
========
* ``__enter__(self) -> self``
* ``__exit__(self, *args) -> None``


Application
===========
* Files
* Buffering data
* Database connection
* Database transactions
* Database cursors
* Locks
* Network sockets
* Network streams
* HTTP sessions


Implementation
==============
.. code-block:: python
    :caption: How to create Context Managers

    class MyClass:
        def __enter__(self):
            print('Entering the block')
            return self

        def __exit__(self, *args):
            print('Exiting the block')
            return None

        def do_something(self):
            print('I am inside')


    with MyClass() as cls:
        cls.do_something()

    # Entering the block
    # I am inside
    # Exiting the block


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
            first_name TEXT,
            last_name TEXT)"""
    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :first_name, :last_name)'
    SQL_SELECT = 'SELECT * from astronauts'


    astronauts = [
        {'pesel': '61041212345', 'first_name': 'José', 'last_name': 'Jiménez'},
        {'pesel': '61041212346', 'first_name': 'Jan', 'last_name': 'Twardowski'},
        {'pesel': '61041212347', 'first_name': 'Melissa', 'last_name': 'Lewis'},
        {'pesel': '61041212348', 'first_name': 'Alex', 'last_name': 'Vogel'},
        {'pesel': '61041212349', 'first_name': 'Ryan', 'last_name': 'Stone'},
    ]


    with sqlite3.connect(':memory:') as db:
        db.execute(SQL_CREATE_TABLE)
        db.executemany(SQL_INSERT, astronauts)

        for row in db.execute(SQL_SELECT):
            print(row)

Lock
----
.. code-block:: python

    from threading import Lock

    my_list = [1, 2, 3]


    with Lock() as lock:
        my_list.append(4)


.. code-block:: python

    from threading import Lock

    my_list = [1, 2, 3]
    lock = Lock()


    with lock:
        my_list.append(4)


Contextmanager decorator
========================
* Split function for before and after ``yield``
* Code before ``yield`` becomes ``__enter__()``
* Code after ``yield`` becomes ``__exit__()``

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
        list(range(100_000_000))

    # Duration 3.3795 seconds

``ContextDecorator`` class
--------------------------
.. code-block:: python

    from contextlib import ContextDecorator
    import time


    class Timeit(ContextDecorator):
        def __enter__(self):
            self.start_time = time.time()
            return self

        def __exit__(self, *args):
            end_time = time.time()
            duration = end_time - self.start_time
            print(f'Duration {duration:.4f} seconds')


    @Timeit()
    def my_function():
        list(range(100_000_000))


    my_function()
    # Duration 3.4697 seconds

.. code-block:: python

    import time


    class Timeit:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            self.start_time = time.time()
            return self

        def __exit__(self, *arg, **kwargs):
            self.end_time = time.time()
            duration = self.end_time - self.start_time
            print(f'Duration of {self.name} is {duration:f} seconds')


    a = 'a'
    b = 'b'

    with Timeit('f-string'):
        f'result of a+b is: {a} {b}'

    with Timeit('string concat'):
        'result of a+b is: ' + a + b

    with Timeit('str.format()'):
        'result of a+b is: {0}{1}'.format(a, b)

    with Timeit('%-style'):
        'result of a+b is: %s%s' % (a, b)

    # Duration of f-string is 0.000002 seconds
    # Duration of string concat is 0.000001 seconds
    # Duration of str.format() is 0.000003 seconds
    # Duration of %-style is 0.000002 seconds

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
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/context_manager_file.py`

:English:
    #. Take input code from listing below
    #. Create Context manager for file which buffers data before save
    #. When block closes, then open file and write data
    #. How to make buffer save data every X bytes?
    #. How to make buffer save data every X seconds?
    #. How to make buffer save data in the background, but it could be still used?

:Polish:
    #. Weź kod wejściowy z listingu poniżej
    #. Stwórz Context Manager dla plików, który buforuje dane przed zapisem
    #. Gdy nastąpi wyjście z bloku context managera, to otwórz plik i zapisz dane
    #. Jak zrobić, aby bufor zapisywał dane na dysku co X bajtów?
    #. Jak zrobić, aby bufor zapisywał dane na dysku co X sekund?
    #. Jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?

:Input:
    .. code-block:: python

        FILENAME = '/tmp/context-manager.txt'

        class File:
            pass


        with File(FILENAME) as file:
            file.append_line(...)
            file.append_line(...)
            file.append_line(...)

