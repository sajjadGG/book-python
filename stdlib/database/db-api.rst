************
Database API
************

Rationale
=========
* DB API v2

.. code-block:: python

    sqlite3.connect(...) -> connection

    connection.execute(...) -> result
    connection.executemany(...) -> List[result]
    connection.fetchmany(...) -> List[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
