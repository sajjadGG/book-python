Database API
============

Rationale
---------
* :pep:`249` -- Python Database API
* DB API v2
* System for providing Python database interfaces
* Non-trivial to write app with polyglot persistence
* Transactions begin implicitly (no BEGIN method)
* Transaction has to be committed or rollback explicitly (COMMIT, ROLLBACK)
* Implicit transaction can be turned off using autocommit mode, which is now a common feature (though not a part of the :pep:`249`)


API
---
.. code-block:: python

    sqlite3.connect(...) -> connection

    connection.execute(...) -> result
    connection.executemany(...) -> list[result]
    connection.fetchmany(...) -> list[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
    connection.close()
