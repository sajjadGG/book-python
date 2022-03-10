AsyncIO Sleep
=============


Rationale
---------
* Coroutine ``asyncio.sleep(delay, result=None)``
* Block for delay seconds.
* If result is provided, it is returned to the caller when the coroutine completes


Example
-------
.. code-block:: python

    import asyncio


    async def main():
        result = await asyncio.sleep(1, 'done')
        print(result)


    asyncio.run(main())
    # done
