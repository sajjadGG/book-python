AsyncIO Coroutine
=================


Rationale
---------
* Coroutine function and coroutine object are two different things
* Coroutine function is the definition (``async def``)
* Coroutine function will create coroutine when called
* This is similar to generator object and generator function
* Coroutine functions are not awaitables
* Coroutine objects are awaitables
* Coroutines declared with the ``async``/``await`` syntax is the preferred way of writing asyncio applications. [#AsyncioTask]_

>>> async def hello():
...     return 'hello'
>>>
>>>
>>> type(hello)
<class 'function'>
>>>
>>> type(hello())
<class 'coroutine'>


SetUp
-----
>>> import asyncio


Coroutine Function
------------------
* Coroutine function is the definition (``async def``)
* Also known as async functions
* Defined by putting ``async`` in front of the ``def``
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``
* Coroutine functions are not awaitables

Calling a coroutine function does not execute it, but rather returns a
coroutine object. This is analogous to generator functions - calling them
doesn't execute the function, it returns a generator object, which we then
use later.

>>> async def hello():
...     return 'hello'


Coroutine Object
----------------
* Coroutine function will create coroutine when called
* Coroutine objects are awaitables
* To execute coroutine object you can ``await`` it
* To execute coroutine object you can ``asyncio.run(...)``
* To schedule coroutine object: ``ensure_future()`` or ``create_task()``

To execute a coroutine object, either:

* use it in an expression with ``await`` in front of it, or
* use ``asyncio.run(coroutine_object())``, or
* schedule it with ``ensure_future()`` or ``create_task()``.

>>> async def hello():
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello())
'hello'


Error: Running Coroutine Functions
----------------------------------
* Only coroutine objects can be run
* It is not possible to run coroutine function

>>> def hello():
...     return 'hello'
>>>
>>>
>>> asyncio.run(hello)
Traceback (most recent call last):
ValueError: a coroutine was expected, got <function hello at 0x117a363b0>


Error: Multiple Awaiting
------------------------
* Coroutine object can only be awaited once

>>> async def hello():
...     return 'hello'
>>>
>>>
>>> coro = hello()
>>>
>>> asyncio.run(coro)
'hello'
>>>
>>> asyncio.run(coro)
Traceback (most recent call last):
RuntimeError: cannot reuse already awaited coroutine


Error: Await Outside Coroutine Function
---------------------------------------
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``

Only a coroutine function (``async def``) can use ``await``. Non-coroutine
functions (``def``) cannot use ``await``:

>>> def hello():
...     await asyncio.sleep(0.1)
...     return 'hello'
...
Traceback (most recent call last):
SyntaxError: 'await' outside async function


Getting Results
---------------
>>> import asyncio
>>>
>>>
>>> async def hello():
...     return 'hello'
>>>
>>>
>>> async def main():
...     result = await hello()
...     print(result)
>>>
>>>
>>> asyncio.run(main())
done


Inspect
-------
>>> from inspect import isawaitable
>>>
>>>
>>> async def hello():
...     return 'hello'
>>>
>>>
>>> isawaitable(hello)
False
>>>
>>> isawaitable(hello())
True
>>>
>>>
>>> type(hello)
<class 'function'>
>>>
>>> type(hello())
<class 'coroutine'>
