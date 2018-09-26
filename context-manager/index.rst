****************
Context Managers
****************

Local variables in Python have function scope, and thus the target of a with statement, if any, is still visible after the block has exited, though ``__exit__()`` has already been called on the context manager (the argument of the with statement), and thus is often not useful or valid.

* ``__enter__()``
* ``__exit__()``

Zastosowanie
------------
* Połączenia do bazy danych
* Pliki
* Stream siecowe

Przykład
--------
.. code-block:: python

    f = open(filename)
    # ...
    f.close()

.. code-block:: python

    f = open(filename)
    try:
        # ...
    finally:
        f.close()

.. code-block:: python

    with open(filename) as f:
        # ...

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

Database
--------
.. code-block:: python

    import sqlite3

    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS kontakty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT
        )
    """

    SQL_INSERT = """
        INSERT INTO kontakty VALUES (
            NULL,
            :pesel,
            :firstname,
            :lastname
        )
    """

    ksiazka_adresowa = [
        {'pesel': '61041206070', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '69072114561', 'firstname': 'Matt', 'lastname': 'Kowalski'},
        {'pesel': '69072114562', 'firstname': 'Mark', 'lastname': 'Watney'},
        {'pesel': '69072114563', 'firstname': 'Melissa', 'lastname': 'Lewis'},
    ]

    with sqlite3.connect(':memory:') as connection:
        connection.execute(SQL_CREATE_TABLE)
        cursor.executemany(SQL_INSERT, ksiazka_adresowa)

Contextmanager decorator
------------------------
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

Dzieli naszą funkcję na bloki przed i po ``yield``.

- Bloki przed traktuje jako ``__enter__()``
- Bloki za traktuje jako ``__exit__()``

.. code-block:: python

    from contextlib import ContextDecorator

    class makeparagraph(ContextDecorator):
        def __enter__(self):
            print('<p>')
            return self

        def __exit__(self, *exc):
            print('</p>')
            return False

    @makeparagraph()
    def generate_html():
        print('Here is some non-HTML')

    generate_html()

.. code-block:: html

    <p>
    Here is some non-HTML
    </p>

timing
------
.. code-block:: python

    import contextlib
    import time
    
    @contextlib.contextmanager
    def time_print(task_name):
        t = time.time()
        try:
            yield
        finally:
            print task_name, "took", time.time() - t, "seconds."
    
    with time_print("processes"):
        [doproc() for _ in range(500)]
    
    # processes took 15.236166954 seconds.
    
    with time_print("threads"):
        [dothread() for _ in range(500)]
    
    # threads took 0.11357998848 seconds.


Assignments
===========

Buffered file
-------------
#. Stwórz Context Manager dla zapisu do plików
#. Context Manager buforuje dane (nie zapisuje ich na bieżąco
#. Gdy program wyjdzie z bloku context managera, to nastąpi zapisanie do pliku
