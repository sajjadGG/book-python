AsyncIO Iterator
================


Rationale
---------
* ``__aiter__``
* ``__anext__``


Example
-------
>>> class Reader:
...     async def readline(self):
...         ...
...
...     def __aiter__(self):
...         return self
...
...     async def __anext__(self):
...         val = await self.readline()
...         if val == b'':
...             raise StopAsyncIteration
...         return val


Type Annotation
---------------
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``
