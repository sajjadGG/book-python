********
Callable
********


Callable
========
.. code-block:: python

    def hello():
        return 'My name... José Jiménez'


    type(hello())         # <class 'str'>
    hello()               # My name... José Jiménez

    type(hello)           # <class 'function'>
    hello                 # <function hello at 0x0C55D420>

    type('hello')         # <class 'str'>
    'hello'               # 'hello'
    'hello'()             # TypeError: 'str' object is not callable


Returning function
==================
.. code-block:: python

    def lower():
        return 'My name... José Jiménez'

    def higher():
        return lower


    text = higher()     # <function __main__.lower()>
    text()              # 'My name... José Jiménez'


Aliases
=======
.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now()

    print(now)            # 1969-07-21 02:56:15
    time.sleep(10)
    print(now)            # 1969-07-21 02:56:15

.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now

    print(now())          # 1969-07-21 02:56:15
    time.sleep(10)
    print(now())          # 1969-07-21 02:56:25


.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now

    print(now())
    # 1969-07-21 02:56:25

    print(now)
    # <built-in method now of type object at 0x107695638>

    now()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)

    now.__call__()
    # datetime.datetime(1969, 7, 21, 2, 56, 25)


Assignments in Polish
=====================
.. todo:: Create Assignments
