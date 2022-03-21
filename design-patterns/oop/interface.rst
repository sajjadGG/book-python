OOP Interface
=============


Important
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


Use Cases
---------
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
>>>
>>> ram: Cache = CacheRAM()
>>> ram.set('name', 'Mark Watney')
>>> ram.is_valid('name')
>>> ram.get('name')
>>>
>>> db: Cache = CacheDatabase()
>>> db.set('name', 'Mark Watney')
>>> db.is_valid('name')
>>> db.get('name')


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
