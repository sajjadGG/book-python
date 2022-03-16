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
...         line = await self.readline()
...         if line == b'':
...             raise StopAsyncIteration
...         return line


Type Annotation
---------------
* ``collections.abc.AsyncIterable``
* ``collections.abc.AsyncIterator``
* ``collections.abc.AsyncGenerator``
