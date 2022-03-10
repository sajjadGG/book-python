AsyncIO Event Loop
==================


Rationale
---------
* Async code can only run inside an event loop.
* The event loop is the driver code that manages the cooperative multitasking.
* You can create multiple threads and run different event loops in each of them.

For example, Django uses the main thread to wait for incoming requests, so we can't run an asyncio event loop there, but we can start a separate worker thread for our event loop.
[#cheat]_

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task. [#pydocmultithreading]_

.. figure:: img/asyncio-eventloop-sync.png
.. figure:: img/asyncio-eventloop-async.png
.. figure:: img/asyncio-eventloop-uvloop-doc.png
.. figure:: img/asyncio-eventloop-uvloop-using.png

Example
-------
.. code-block:: python

    import asyncio


    async def work(*args, **kwargs):
        # do stuff...
        return result


    result = asyncio.run(work(1, 2, 3))

Since Python 3.7 there is ``asyncio.run()``. Before you had to ``get_event_loop()`` and then ``run_until_complete()``:

.. code-block:: python

    import asyncio


    async def a():
        print(f'A: started')
        await asyncio.sleep(2)
        print(f'A: finished')


    async def b():
        print(f'B: started')
        await asyncio.sleep(1)
        print(f'B: finished')


    async def c():
        print(f'C: started')
        await asyncio.sleep(3)
        print(f'C: finished')


    async def main():
        await asyncio.gather(
            a(),
            b(),
            c(),
        )


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished
