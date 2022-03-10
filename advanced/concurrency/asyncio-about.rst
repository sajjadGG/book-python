AsyncIO About
=============


.. glossary::

    promise
    future
    coroutine
    queue
    awaitable

    aws
        awaitables


Rationale
---------
* ``asyncio`` in stdlib
* ``async`` and ``await`` keyword
* Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
* Async is the future of programming

* Objective: Maximize the usage of a single thread
* Objective: handling I/O asynchronously
* Objective: enabling concurrent code using coroutines

* Advantage: Async will fill the gaps, otherwise wasted on waiting for I/O
* Advantage: You control when tasks switches occur, so locks and other synchronization are no longer needed
* Advantage: Cost task switches is incredibly low. Calling a pure Python function has more overhead than restarting a generator or awaitable
* Advantage: Function builds stack each time it's called, whereas async uses generators underneath, which already has stack created
* Advantage: Async is the cheapest way to task switch
* Advantage: In terms of speed async servers blows threaded servers in means of thousands
* Advantage: Async is very cheap in means of resources
* Advantage: Async world has a huge ecosystem of support tools
* Advantage: Coding is easier to get right, than threads

* Disadvantage: Async switches cooperatively, so you do need to add explicit code ``yield`` or ``await`` to cause a task to switch
* Disadvantage: Everything you do need a non-blocking version (for example ``open()``)
* Disadvantage: Increased learning curve
* Disadvantage: Create event loop, acquire, crate non-blocking versions of your code
* Disadvantage: You think you know Python, there is a second half to learn (async)


Sync vs Async
-------------
.. figure:: img/asyncio-sequence-sync.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-sequence-async.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/concurrency-sync-vs-async-1.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_

.. figure:: img/concurrency-sync-vs-async-2.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


Execution
---------
.. figure:: img/asyncio-execution-sync.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-execution-async.png

    Source: Michael Kennedy [#Kennedy2019]_


Awaitables
----------
* Object is an awaitable if it can be used in an ``await`` expression
* Awaitable objects: Coroutines, Tasks, Futures
* ``__await__`` and ``await`` keyword

There are three main types of awaitable objects:

    * Coroutines,
    * Tasks,
    * Futures.

.. figure:: img/asyncio-async-anatomy.png

    Coroutine (async function) anatomy. Source: Michael Kennedy [#Kennedy2019]_


Example
-------
.. code-block:: python

    import asyncio


    async def a():
        print('A: started')
        await asyncio.sleep(2)
        print('A: finished')
        return 'a'

    async def b():
        print('B: started')
        await asyncio.sleep(1)
        print('B: finished')
        return 'b'

    async def c():
        print('C: started')
        await asyncio.sleep(3)
        print('C: finished')
        return 'c'


    async def main():
        result = await asyncio.gather(
            a(),
            b(),
            c(),
        )
        print(f'Result: {result}')


    if __name__ ==  '__main__':
        asyncio.run(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished
    # Result: ['a', 'b', 'c']


Further Reading
---------------
* Kennedy, M. Async Techniques and Examples in Python [#Kennedy2022]_
* Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_
* Abdalla, A. Creating a Bittorrent Client using Asyncio [#Abdalla2017]_


References
----------
.. [#Kennedy2019] Kennedy, M. Demystifying Python's Async and Await Keywords. Publisher: JetBrainsTV. Year: 2019. Retrieved: 2022-03-10. URL: https://www.youtube.com/watch?v=F19R_M4Nay4

.. [#Kennedy2022] Kennedy, M. Async Techniques and Examples in Python Course. Publisher: TalkPython. Year: 2022. Retrieved: 2022-03-10. URL: https://talkpython.fm/async

.. [#Abdalla2017] Abdalla, A. Creating a Bittorrent Client using Asyncio. Year: 2017. Retrieved: 2022-03-10. URL: https://www.youtube.com/watch?v=Pe3b9bdRtiE

.. [#Langa2020] Langa, Ł. import asyncio: Learn Python's AsyncIO. Year: 2020. Retrieved: 2022-03-10. URL: https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB

.. [#AsyncioTask] https://docs.python.org/3/library/asyncio-task.html
.. [#cheat] https://cheat.readthedocs.io/en/latest/python/asyncio.html
.. [#pydocmultithreading] https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading
