AsyncIO Awaitable
=================


Rationale
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

.. figure:: img/asyncio-awaitables.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


Objects
-------
>>> from collections.abc import Awaitable
>>> from collections.abc import Coroutine
>>> from asyncio import Future
>>> from asyncio import Task
