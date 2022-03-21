AsyncIO Awaitable
=================


Important
---------
* Object is an awaitable if it can be used in an ``await`` expression
* Awaitable objects: Coroutines, Tasks, Futures
* ``__await__`` and ``await`` keyword

.. glossary::

    aw
    awaitable
        Object is an awaitable if it can be used in an ``await`` expression

    aws
        Awaitables

    coroutine
        Coroutine - a function which can run concurrently.

    tasks
        Runs thing in the "background". Can be awaited and cancelled.

    future


Awaitables
----------
There are three main types of awaitable objects:

    * Coroutines,
    * Tasks,
    * Futures.

Coroutines are a low level concept and doesn't know about asyncio concepts
such as EventLoop and Cancellations.

Tasks wraps around a coroutine object and allows for handling exceptions,
gathering results etc.


Objects
-------
Features of Python:

>>> from collections.abc import Awaitable
>>> from collections.abc import Coroutine

Features of AsyncIO library:

>>> from asyncio import Future
>>> from asyncio import Task

.. figure:: img/asyncio-awaitables.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


Type Annotations
----------------
>>> from collections.abc import Awaitable
>>> from collections.abc import Coroutine
>>> from collections.abc import AsyncIterable
>>> from collections.abc import AsyncIterator
>>> from collections.abc import AsyncGenerator


References
----------
.. [#Langa2020] Langa, Ł. import asyncio: Learn Python's AsyncIO. Year: 2020. Retrieved: 2022-03-10. URL: https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB
