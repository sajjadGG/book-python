OOP Abstract Interface
======================


Rationale
---------
* Python don't have interfaces
* Cannot instantiate
* Inheriting class must implement all methods
* Only method declaration
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)

.. glossary::

    interface
        Software entity with public methods and attribute declaration

    implement
        Class implements interface if has all public fields and methods from interface


Syntax
------
>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None:
...         raise NotImplementedError
...
...     def get(self, key: str) -> str:
...         raise NotImplementedError
...
...     def is_valid(self, key: str) -> bool:
...         raise NotImplementedError


Alternative Notation
--------------------
>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def get(self, key: str) -> str: raise NotImplementedError
...     def is_valid(self, key: str) -> bool: raise NotImplementedError

Sometimes you may get a shorter code, but it will not raise an error.

>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: pass
...     def get(self, key: str) -> str: pass
...     def is_valid(self, key: str) -> bool: pass

As of three dots (``...``) is a valid Python object (Ellipsis) you can write that:

>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

The following code is not a valid Python syntax...
How nice it would be to write:

>>> @interface # doctest: +SKIP
... class Cache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

>>> class Cache(interface=True): # doctest: +SKIP
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...

>>> interface Cache: # doctest: +SKIP
...     def set(self, key: str, value: str) -> None
...     def get(self, key: str) -> str
...     def is_valid(self, key: str) -> bool

Example
-------
>>> class Cache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...
>>>
>>>
>>> class DatabaseCache(Cache):
...      ...
>>>
>>> class InMemoryCache(Cache):
...      ...
>>>
>>> class FilesystemCache(Cache):
...      ...
>>>
>>>
>>> c: Cache = DatabaseCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')
>>>
>>> c: Cache = InMemoryCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')
>>>
>>> c: Cache = FilesystemCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')


Use Case - 0x01
---------------
* Cache

>>> class Cache:
...     def get(self, key: str) -> str: raise NotImplementedError
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def is_valid(self, key: str) -> bool: raise NotImplementedError
>>>
>>>
>>> class CacheDatabase(Cache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
>>>
>>>
>>> class CacheRAM(Cache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
>>>
>>>
>>> class CacheFilesystem(Cache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...
>>>
>>>
>>> fs: Cache = CacheFilesystem()
>>> fs.set('name', 'Mark Watney')
>>> fs.is_valid('name')
>>> fs.get('name')


Use Case - 0x02
---------------
* Settings

>>> # myapp/cache.py
>>> class CacheInterface:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...
>>>
>>>
>>> class DatabaseCache(CacheInterface):
...      pass
>>>
>>> class InMemoryCache(CacheInterface):
...      pass
>>>
>>> class FilesystemCache(CacheInterface):
...      pass

>>> # myapp/settings.py
>>> from myapp.cache import CacheInterface  # doctest: +SKIP
>>>
>>> cache = DatabaseCache

>>> # myapp/usage.py
>>> from myapp.settings import cache  # doctest: +SKIP
>>>
>>> c: CacheInterface = cache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')


Assignments
-----------
.. literalinclude:: assignments/oop_interface_a.py
    :caption: :download:`Solution <assignments/oop_interface_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_interface_b.py
    :caption: :download:`Solution <assignments/oop_interface_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_interface_c.py
    :caption: :download:`Solution <assignments/oop_interface_c.py>`
    :end-before: # Solution
