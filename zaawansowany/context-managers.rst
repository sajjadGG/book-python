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


.. code-block:: python

    @contextmanager
    def FileName(*args, **kwargs):
       with File(*args, **kwargs) as f:
           yield f.name
