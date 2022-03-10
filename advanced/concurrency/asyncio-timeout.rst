AsyncIO Timeout
===============


Rationale
---------
* coroutine ``asyncio.wait_for(aw, timeout)``
* Wait for the aw awaitable to complete with a timeout.
* Timeout can either be ``None`` or a ``float`` or int number of seconds to wait for.
* If timeout is ``None``, block until the future completes.
* If a timeout occurs, it cancels the task and raises ``asyncio.TimeoutError``
* If the wait is cancelled, the future ``aw`` is also cancelled.


Example
-------
.. code-block:: python

    import asyncio

    HOUR = 3600


    async def work():
        await asyncio.sleep(HOUR)
        return 'done'


    async def main():
        try:
            await asyncio.wait_for(work(), timeout=1.0)
        except asyncio.TimeoutError:
            print('timeout!')

    asyncio.run(main())
    # timeout!
