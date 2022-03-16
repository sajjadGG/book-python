AsyncIO Wait
============


Rationale
---------
* coroutine ``asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)``
* Run awaitable objects in the ``aws`` iterable concurrently and block until the condition specified by return_when.
* The ``aws`` iterable must not be empty.
* ``timeout: float|int`` if specified, maximum number of seconds to wait before returning.
* ``wait()`` does not cancel the futures when a timeout occurs.
* ``return_when`` indicates when this function should return. It must be one of the following constants:

    * ``FIRST_COMPLETED`` - The function will return when any future finishes or is cancelled.
    * ``FIRST_EXCEPTION`` - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.
    * ``ALL_COMPLETED`` - The function will return when all futures finish or are cancelled.

.. code-block:: python

    done, pending = await asyncio.wait(aws)

* Does not raise ``asyncio.TimeoutError``
* ``Futures`` or ``Tasks`` that aren't done when the timeout occurs are simply returned in the second set (``pending``).


Example
-------
>>> import asyncio
>>>
>>>
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


Waiting For
-----------
* This will try to run function for 5.0 seconds
* If function does not finish by then, rises ``TimeoutError``

>>> import asyncio
>>>
>>>
>>> async def myfunc():
...     while True:
...         print('waiting')
...         await asyncio.sleep(1.0)
>>>
>>>
>>> asyncio.run(asyncio.wait_for(myfunc(), 5.0))
waiting
waiting
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

>>> import asyncio
>>>
>>>
>>> async def myfunc():
...     while True:
...         print('waiting')
...         await asyncio.sleep(1.0)
>>>
>>>
>>> async def main():
...     try:
...         await asyncio.wait_for(myfunc(), 3.0)
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
waiting
waiting
waiting
Timeout

>>> import asyncio
>>>
>>>
>>> async def myfunc():
...     while True:
...         print('waiting')
...         await asyncio.sleep(1.0)
>>>
>>>
>>> async def main():
...     mycoro = myfunc()
...     waiter = asyncio.wait_for(mycoro, 3.0)
...     try:
...         await waiter
...     except asyncio.TimeoutError:
...         print('Timeout')
>>>
>>>
>>> asyncio.run(main())
waiting
waiting
waiting
Timeout

Created but not awaited objects will raise an exception. This prevents
from creating coroutines and forgetting to "await" on it.

More verbose message you can achieve by using ``PYTHONASYNCIODEBUG=1`` and
``PYTHONTRACEMALLOC=1`` environment variables.
