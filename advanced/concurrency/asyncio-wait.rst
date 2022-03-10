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
.. code-block:: python

    import asyncio


    async def work():
        return 'done'


    async def main():
        task = asyncio.create_task(work())
        done, pending = await asyncio.wait({task})

        if task in done:
            print('work is done')

    asyncio.run(main())
    # work is done
