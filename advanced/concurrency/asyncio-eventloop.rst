AsyncIO Event Loop
==================


Rationale
---------
* Async code can only run inside an event loop.
* The event loop is the driver code that manages the cooperative multitasking.
* You can create multiple threads and run different event loops in each of them.
* Python will create a default event loop only in Main Thread
* Python will not create an event loop automatically for you on any other than main thread by default, this is to prevent from having multiple event lops created explicitly
* Event loop can execute only one callback (coroutine) at a time
* Some callbacks (coroutines) can schedule themselves once again (trampoline)
* Reactors
* Proactors

For example, Django uses the main thread to wait for incoming requests, so we can't run an asyncio event loop there, but we can start a separate worker thread for our event loop.
[#cheat]_

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task. [#pydocmultithreading]_

.. figure:: img/asyncio-eventloop-sync.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-eventloop-async.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-eventloop-uvloop-doc.png

    Source: Michael Kennedy [#Kennedy2019]_

.. figure:: img/asyncio-eventloop-uvloop-using.png

    Source: Michael Kennedy [#Kennedy2019]_


Run
---
>>> import asyncio
>>>
>>>
>>> async def myfunc(*args, **kwargs):
...     # do stuff...
...     return result
>>>
>>>
>>> result = asyncio.run(myfunc())


Gather
------
* Run multiple coroutines and gather results

>>> import asyncio
>>>
>>>
>>> async def a():
...     print('a: started')
...     await asyncio.sleep(2)
...     print('a: finished')
...     return 'a'
>>>
>>> async def b():
...     print('b: started')
...     await asyncio.sleep(1)
...     print('b: finished')
...     return 'b'
>>>
>>> async def c():
...     print('c: started')
...     await asyncio.sleep(3)
...     print('c: finished')
...     return 'c'
>>>
>>> async def main():
...     result = await asyncio.gather(
...         a(),
...         b(),
...         c(),
...     )
...     print(f'Result: {result}')
>>>
>>> if __name__ == '__main__':
...     asyncio.run(main())
...
a: started
b: started
c: started
b: finished
a: finished
c: finished
Result: ['a', 'b', 'c']


Selectors
---------
.. figure:: img/asyncio-eventloop-selectors.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_

.. figure:: img/asyncio-eventloop-selectors-unix.png

    Source: Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


UVLoop
------
* The ultimate loop implementation for UNIXes (run this on production)

.. code-block:: console

    $ pip install uvloop

>>> # doctest: +SKIP
... import uvloop
...
... uvloop.install()
...
... loop = asyncio.new_event_loop()
... loop
<uvloop.Loop running=False closed=False debug=False>


References
----------
.. [#Kennedy2019] Kennedy, M. Demystifying Python's Async and Await Keywords. Publisher: JetBrainsTV. Year: 2019. Retrieved: 2022-03-10. URL: https://www.youtube.com/watch?v=F19R_M4Nay4

.. [#Langa2020] Langa, Ł. import asyncio: Learn Python's AsyncIO. Year: 2020. Retrieved: 2022-03-10. URL: https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB
