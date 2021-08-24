Async Programming
=================


.. glossary::

    promises
    futures
    coroutines
    awaitable
    queue


Rationale
---------
* ``asyncio`` in stdlib
* ``async`` keyword
* ``await`` keyword
* CPU-bound Concurrency:

    * Using Queues and Multiprocessing
    * Using Futures and Multiprocessing

* I/O-bound Concurrency:

    * Using Queues and Threading
    * Using Futures and Threading


Type Annotations
----------------
* ``collections.abc.Awaitable``
* ``collections.abc.Coroutine``
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``


Async Programming
-----------------
* Source: https://www.youtube.com/watch?v=F19R_M4Nay4
* Source: https://talkpython.fm/async
* By Michael Kennedy

.. figure:: img/sync-execution-sequence.png
.. figure:: img/sync-execution-timeline.png
.. figure:: img/async-execution-sequence.png
.. figure:: img/async-execution-timeline.png
.. figure:: img/eventloop-sync.png
.. figure:: img/eventloop-async.png
.. figure:: img/async-python.png
.. figure:: img/async-threads.png
.. figure:: img/async-gil.png
.. figure:: img/async-anatomy.png
.. figure:: img/uvloop-doc.png
.. figure:: img/uvloop-using.png


Awaitable
---------
* Coroutine
* ``__await__``


Iterator
--------
* ``__aiter__``
* ``__anext__``

>>> class Reader:
...     async def readline(self):
...         ...
...
...     def __aiter__(self):
...         return self
...
...     async def __anext__(self):
...         val = await self.readline()
...         if val == b'':
...             raise StopAsyncIteration
...         return val


Context Manager
---------------
* ``__aenter__``
* ``__aexit__``

>>> class AsyncContextManager:
...     async def __aenter__(self):
...         await print('entering context')
...
...     async def __aexit__(self, exc_type, exc, tb):
...         await print('exiting context')


3rd Party Library - Unsync
--------------------------
* Library decides which to run, thread, asyncio or sync

.. code-block:: console

    $ pip install unsync

.. code-block:: python

    @unsync
    def my_function():
        pass


References
----------
* https://www.youtube.com/watch?v=Pe3b9bdRtiE
* https://www.youtube.com/watch?v=Xbl7XjFYsN4
