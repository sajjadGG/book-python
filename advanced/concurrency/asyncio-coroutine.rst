AsyncIO Coroutine
=================



Rationale
---------
* Python coroutines are awaitables
* Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. [#AsyncioTask]_
* Term 'coroutine' can be used for two closely related concepts [#AsyncioTask]_:

    * a coroutine function: an ``async def`` function;
    * a coroutine object: an object returned by calling a coroutine function.

* Python distinguishes between a coroutine function and a coroutine object
* Write a coroutine function by putting ``async`` in front of the ``def``
* Only a coroutine function can use ``await``, non-coroutine functions cannot.
* Calling a coroutine function does not execute it, but rather returns a coroutine object. (This is analogous to generator functions - calling them doesn't execute the function, it returns a generator object, which we then use later.)
* To execute a coroutine object, either:

    * use it in an expression with await in front of it, or
    * use asyncio.run(coroutine_object()), or
    * schedule it with ensure_future() or create_task().


Example
-------
.. code-block:: python

    import asyncio


    async def work():
        return 'done'


    async def main():
        result = await work()
        print(result)


    asyncio.run(main())
    # done
