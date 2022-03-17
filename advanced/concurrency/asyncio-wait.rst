AsyncIO Wait
============


Rationale
---------
* ``asyncio.wait(aws, timeout)``
* ``asyncio.wait_for(aw, timeout)``
* ``wait()`` - when a timeout occurs: does not cancel the futures
* ``wait_for()`` - when a timeout occurs: cancels the task and raises ``asyncio.TimeoutError``
* If aw is a coroutine it is automatically scheduled as a Task
* ``wait()`` schedules coroutines as Tasks automatically and later returns those implicitly created Task objects in (done, pending) sets.


SetUp
-----
>>> import asyncio


Wait
----
* Coroutine ``asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)``
* ``aws`` must be iterable (list, tuple, set)
* ``aws`` iterable must not be empty
* Run awaitable objects in the ``aws`` concurrently and block until the condition specified by ``return_when``
* ``timeout: float|int`` if specified, maximum number of seconds to wait before returning
* ``wait()`` does not cancel the futures when a timeout occurs
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
* ``return_when`` indicates when this function should return
* ``return_when`` must be one of ``FIRST_COMPLETED``, ``FIRST_EXCEPTION``, ``ALL_COMPLETED``
* ``return_when=FIRST_COMPLETED`` - The function will return when any future finishes or is cancelled;
* ``return_when=FIRST_EXCEPTION`` - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED;
* ``return_when=ALL_COMPLETED`` - The function will return when all futures finish or are cancelled
* Does not raise ``asyncio.TimeoutError``
* ``Futures`` or ``Tasks`` that aren't done when the timeout occurs are simply returned in the second set (``pending``).

.. code-block:: python

    done, pending = await asyncio.wait(aws)


>>> async def work():
...     return 'done'
>>>
>>>
>>> async def main():
...     task = asyncio.create_task(work())
...     done, pending = await asyncio.wait({task})
...
...     if task in done:
...         print('work is done')
>>>
>>> asyncio.run(main())
work is done


Wait For
--------
* The function will wait until the future is actually cancelled
* Therefore the total wait time may exceed the timeout
* If an exception happens during cancellation, it is propagated
* If coroutine does not finish by then, rises ``TimeoutError``

>>> async def hello():
...     while True:
...         print('hello')
...         await asyncio.sleep(0.1)
>>>
>>>
>>> async def main():
...     await asyncio.wait_for(hello(), 0.3)
>>>
>>>
>>> asyncio.run(main())
waiting
waiting
waiting
asyncio.exceptions.CancelledError
<BLANKLINE>
During handling of the above exception, another exception occurred:
<BLANKLINE>
asyncio.exceptions.CancelledError
<BLANKLINE>
The above exception was the direct cause of the following exception:
<BLANKLINE>
asyncio.exceptions.TimeoutError


Handling Timeouts
-----------------
>>> async def hello():
...     while True:
...         print('hello')
...         await asyncio.sleep(0.1)
>>>
>>>
>>> async def main():
...     try:
...         await asyncio.wait_for(hello(), 0.3)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
hello
hello
hello
Timeout


Handling Timeouts Concurrently
------------------------------
>>> async def hello():
...     print('hello')
...     await asyncio.sleep(0.2)
>>>
>>>
>>> async def main():
...     todo = asyncio.gather(hello(), hello(), hello())
...     try:
...         await asyncio.wait_for(todo, timeout=0.1)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>> asyncio.run(main())
hello
hello
hello
Timeout


Handling Cancellation
---------------------
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled

>>> async def hello():
...     print('hello')
...     try:
...         await asyncio.sleep(2)
...     except asyncio.CancelledError:
...         print('Cancelled')
>>>
>>>
>>> async def main():
...     todo = asyncio.gather(hello(), hello(), hello())
...     try:
...         await asyncio.wait_for(todo, timeout=1)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>> asyncio.run(main())
hello
hello
hello
Cancelled
Cancelled
Cancelled
Timeout
