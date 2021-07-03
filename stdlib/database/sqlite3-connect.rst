Database Connect
================


Rationale
---------
* Can connect to file or to in-memory
* sqlite3.connect() -> connection
* connection.close()


In-Memory Database
------------------
* Useful for tests
* Very fast
* Remember to close connection

Connection to in-memory database:

>>> import sqlite3
>>>
>>>
>>> db = sqlite3.connect(':memory:')
>>> db.close()


File Database
-------------
* Connection will create file if not exists
* Remember to close connection

Connection to database file:

>>> import sqlite3
>>>
>>>
>>> db = sqlite3.connect('/tmp/database.sqlite3')
>>> db.close()


Context Managers
----------------
* Prefer using context manager
* No need to remember about closing connection
* Prepare your data and statements before connection
* Works with either in-memory or file database

>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     ...
