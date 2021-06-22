Async Programming
=================


.. glossary::

    promises
    futures
    coroutines
    awaitable
    queue


Rationale
---------
* ``asyncio`` in stdlib
* ``async`` keyword
* ``await`` keyword
* CPU-bound Concurrency:

    * Using Queues and Multiprocessing
    * Using Futures and Multiprocessing

* I/O-bound Concurrency:

    * Using Queues and Threading
    * Using Futures and Threading


Type Annotations
----------------
* ``collections.abc.Awaitable``
* ``collections.abc.Coroutine``
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``


Async Programming
-----------------
* Source: https://www.youtube.com/watch?v=F19R_M4Nay4
* Source: https://talkpython.fm/async
* By Michael Kennedy

.. figure:: img/sync-execution-sequence.png

.. figure:: img/sync-execution-timeline.png

.. figure:: img/async-execution-sequence.png

.. figure:: img/async-execution-timeline.png

.. figure:: img/eventloop-sync.png

.. figure:: img/eventloop-async.png

.. figure:: img/async-python.png

.. figure:: img/async-threads.png

.. figure:: img/async-gil.png

.. figure:: img/async-anatomy.png

.. figure:: img/uvloop-doc.png

.. figure:: img/uvloop-using.png


Awaitable
---------
* Coroutine
* ``__await__``


Iterator
--------
* ``__aiter__``
* ``__anext__``

.. code-block:: python

    class Reader:
        async def readline(self):
            ...

        def __aiter__(self):
            return self

        async def __anext__(self):
            val = await self.readline()
            if val == b'':
                raise StopAsyncIteration
            return val


Context Manager
---------------
* ``__aenter__``
* ``__aexit__``

.. code-block:: python

    class AsyncContextManager:
        async def __aenter__(self):
            await print('entering context')

        async def __aexit__(self, exc_type, exc, tb):
            await print('exiting context')


3rd Party Library - Trio
------------------------
* https://trio.readthedocs.io/en/latest/tutorial.html

.. code-block:: console

    $ pip install trio

.. code-block:: python

    import trio

    async def child1():
        print("  child1: started! sleeping now...")
        await trio.sleep(1)
        print("  child1: exiting!")

    async def child2():
        print("  child2: started! sleeping now...")
        await trio.sleep(1)
        print("  child2: exiting!")

    async def parent():
        print("parent: started!")
        async with trio.open_nursery() as nursery:
            print("parent: spawning child1...")
            nursery.start_soon(child1)

            print("parent: spawning child2...")
            nursery.start_soon(child2)

            print("parent: waiting for children to finish...")
            # -- we exit the nursery block here --
        print("parent: all done!")

    trio.run(parent)

Client:

.. code-block:: python

    import sys
    import trio

    # arbitrary, but:
    # - must be in between 1024 and 65535
    # - can't be in use by some other program on your computer
    # - must match what we set in our echo server
    PORT = 12345
    # How much memory to spend (at most) on each call to recv. Pretty arbitrary,
    # but shouldn't be too big or too small.
    BUFSIZE = 16384

    async def sender(client_stream):
        print("sender: started!")
        while True:
            data = b"async can sometimes be confusing, but I believe in you!"
            print(f"sender: sending {data!r}")
            await client_stream.send_all(data)
            await trio.sleep(1)

    async def receiver(client_stream):
        print("receiver: started!")
        while True:
            data = await client_stream.receive_some(BUFSIZE)
            print(f"receiver: got data {data!r}")
            if not data:
                print("receiver: connection closed")
                sys.exit()

    async def parent():
        print(f"parent: connecting to 127.0.0.1:{PORT}")
        client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
        async with client_stream:
            async with trio.open_nursery() as nursery:
                print("parent: spawning sender...")
                nursery.start_soon(sender, client_stream)

                print("parent: spawning receiver...")
                nursery.start_soon(receiver, client_stream)

    trio.run(parent)

Server:

.. code-block:: python

    import trio
    from itertools import count

    # Port is arbitrary, but:
    # - must be in between 1024 and 65535
    # - can't be in use by some other program on your computer
    # - must match what we set in our echo client
    PORT = 12345
    # How much memory to spend (at most) on each call to recv. Pretty arbitrary,
    # but shouldn't be too big or too small.
    BUFSIZE = 16384

    CONNECTION_COUNTER = count()

    async def echo_server(server_stream):
        # Assign each connection a unique number to make our debug prints easier
        # to understand when there are multiple simultaneous connections.
        ident = next(CONNECTION_COUNTER)
        print("echo_server {}: started".format(ident))
        try:
            while True:
                data = await server_stream.receive_some(BUFSIZE)
                print(f"echo_server {ident}: received data {data!r}")
                if not data:
                    print(f"echo_server {ident}: connection closed")
                    return
                print(f"echo_server {ident}: sending data {data!r}")
                await server_stream.send_all(data)
        # FIXME: add discussion of MultiErrors to the tutorial, and use
        # MultiError.catch here. (Not important in this case, but important if the
        # server code uses nurseries internally.)
        except Exception as exc:
            # Unhandled exceptions will propagate into our parent and take
            # down the whole program. If the exception is KeyboardInterrupt,
            # that's what we want, but otherwise maybe not...
            print(f"echo_server {ident}: crashed: {exc!r}")

    async def main():
        await trio.serve_tcp(echo_server, PORT)

    # We could also just write 'trio.run(serve_tcp, echo_server, PORT)', but real
    # programs almost always end up doing other stuff too and then we'd have to go
    # back and factor it out into a separate function anyway. So it's simplest to
    # just make it a standalone function from the beginning.
    trio.run(main)


3rd Party Library - Unsync
--------------------------
* Library decides which to run, thread, asyncio or sync

.. code-block:: console

    $ pip install unsync

.. code-block:: python

    @unsync
    def my_function():
        pass


References
----------
* https://www.youtube.com/watch?v=Pe3b9bdRtiE
* https://www.youtube.com/watch?v=Xbl7XjFYsN4
