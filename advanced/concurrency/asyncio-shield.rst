AsyncIO Shield
==============


Rationale
---------
* Shielding from Cancellation
* Awaitable ``asyncio.shield(aw)``
* Protect an awaitable object from being cancelled.


Example
-------
.. code-block:: python

    import asyncio

    async def work():
        return 'done'


    async def main():
        try:
            res = await shield(work())
        except CancelledError:
            res = None


    asyncio.run(main())
