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


Dzieli naszą funkcję na bloki przed i po ``yield``.

- Bloki przed traktuje jako ``__enter__()``
- Bloki za traktuje jako ``__exit__()``

.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print("<%s>" % name)
        yield
        print("</%s>" % name)

    >>> with tag("h1"):
    ...    print("foo")
    ...
    <h1>
    foo
    </h1>

Przykład praktyczny
-------------------
.. literalinclude:: src/context-manager.py
    :name: listing-context-manager
    :language: python
    :caption: Context Manager