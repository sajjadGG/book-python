.. _Advanced Functions:

******************
Advanced Functions
******************


Type annotations
================
* Since Python 3.5
* Types are not forced
* Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
* Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers(1, 2)
    # 3

.. code-block:: python
    :caption: Python will execute without even warning. Your IDE and ``mypy`` will yield errors.

    def add_numbers(a: int, b: int) -> int:
        return a + b

    add_numbers('Jan', 'Twardowski')
    # 'JanTwardowski'

.. note:: More about this topic at :ref:`Type Annotation`


Callable
========
.. code-block:: python

    def hello():
        return 'My name... José Jiménez'


    type(hello)           # <class 'function'>
    hello                 # <function hello at 0x0C55D420>

    type(hello())         # <class 'str'>
    hello()               # My name... José Jiménez

    type('hello')         # <class 'str'>
    'hello'               # 'hello'
    'hello'()             # TypeError: 'str' object is not callable

Returning function (callable)
-----------------------------
.. code-block:: python

    def lower():
        return 'My name... José Jiménez'

    def higher():
        return hello

    text = higher()     # <function __main__.lower()>
    text()              # 'My name... José Jiménez'

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now()

    print(now)            # 1969-07-21 14:56:15
    time.sleep(10)
    print(now)            # 1969-07-21 14:56:15

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now

    print(now())          # 1969-07-21 14:56:15
    time.sleep(10)
    print(now())          # 1969-07-21 14:56:25


.. code-block:: python

    import datetime
    import time


    now = datetime.datetime.now

    print(now())
    # 1969-07-21 14:56:25

    print(now)
    # <built-in method now of type object at 0x107695638>

    now()
    # datetime.datetime(1969, 7, 21, 14, 56, 25)

    now.__call__()
    # datetime.datetime(1969, 7, 21, 14, 56, 25)


Assignments
===========
.. todo:: Create Assignments
