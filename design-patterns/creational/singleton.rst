Singleton
=========


Rationale
---------
* EN: Singleton
* PL: Singleton
* Type: object


Use Cases
---------
* Database connection pool
* HTTP Gateway


Design
------
.. code-block:: python

    class Singleton:
        _instance = None

        @classmethod
        def get_instance(cls):
            if not cls._instance:
                cls._instance = ...
            return cls._instance


    # Creating first instance for the first time
    first = Singleton.get_instance()

    # Connecting for the second time
    # Will use existing instance
    second = Singleton.get_instance()


Example
-------
.. code-block:: python

    class DB:
        _connection = None

        @classmethod
        def connect(cls):
            if not cls._connection:
                print('Establishing connection...')
                cls._connection = ...
            return cls._connection


    # Connecting for the first time
    # Will establish new connection
    first = DB.connect()

    # Connecting for the second time
    # Will use existing connection to the DB
    # The same handle as `first`
    second = DB.connect()


Assignments
-----------
.. todo:: Create assignments

