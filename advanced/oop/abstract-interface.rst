OOP Abstract Interface
======================
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
* Names: ``Cache``, ``CacheInterface``, ``ICache``, ``CacheIface``

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
>>> class ICache:
...     def set(self, key: str, value: str) -> None: ...
...     def get(self, key: str) -> str: ...
...     def is_valid(self, key: str) -> bool: ...
>>>
>>>
>>> class DatabaseCache(ICache):
...      ...
>>>
>>> class InMemoryCache(ICache):
...      ...
>>>
>>> class FilesystemCache(ICache):
...      ...
>>>
>>>
>>> c: ICache = DatabaseCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')
>>>
>>> c: ICache = InMemoryCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')
>>>
>>> c: ICache = FilesystemCache()
>>> c.set('firstname', 'Mark')
>>> c.is_valid('firstname')
>>> c.is_valid('lastname')
>>> c.get('firstname')


Use Case - 0x01
---------------
* Cache

File ``cache_interface.py``:

>>> class ICache:
...     def get(self, key: str) -> str: raise NotImplementedError
...     def set(self, key: str, value: str) -> None: raise NotImplementedError
...     def is_valid(self, key: str) -> bool: raise NotImplementedError

File ``cache_impl.py``:

>>> class CacheDatabase(ICache):
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
>>> class CacheRAM(ICache):
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
>>> class CacheFilesystem(ICache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...

File ``settings.py``

>>> from myapp.cache_interface import ICache  # doctest: +SKIP
>>> from myapp.cache_imp import DatabaseCache  # doctest: +SKIP
>>> from myapp.cache_imp import InMemoryCache  # doctest: +SKIP
>>> from myapp.cache_imp import FilesystemCache  # doctest: +SKIP
>>>
>>>
>>> DefaultCache = InMemoryCache

File ``myapp.py``:

>>> from myapp.settings import DefaultCache, ICache  # doctest: +SKIP

>>> cache: ICache = DefaultCache()
>>> cache.set('name', 'Mark Watney')
>>> cache.is_valid('name')
>>> cache.get('name')


Use Case - 0x02
---------------
>>> class Tool:
...     def on_mouse_over(self): raise NotImplementedError
...     def on_mouse_out(self): raise NotImplementedError
...     def on_mouse_click_leftbutton(self): raise NotImplementedError
...     def on_mouse_unclick_leftbutton(self): raise NotImplementedError
...     def on_mouse_click_rightbutton(self): raise NotImplementedError
...     def on_mouse_unclick_rightbutton(self): raise NotImplementedError
...     def on_key_press(self): raise NotImplementedError
...     def on_key_unpress(self): raise NotImplementedError
>>>
>>>
>>> class Pencil(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...
>>>
>>>
>>> class Pen(Tool):
...     def on_mouse_over(self):
...         ...
...
...     def on_mouse_out(self):
...         ...
...
...     def on_mouse_click_leftbutton(self):
...         ...
...
...     def on_mouse_unclick_leftbutton(self):
...         ...
...
...     def on_mouse_click_rightbutton(self):
...         ...
...
...     def on_mouse_unclick_rightbutton(self):
...         ...
...
...     def on_key_press(self):
...         ...
...
...     def on_key_unpress(self):
...         ...


Assignments
-----------
.. literalinclude:: assignments/oop_abstract_interface_a.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_interface_b.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_abstract_interface_c.py
    :caption: :download:`Solution <assignments/oop_abstract_interface_c.py>`
    :end-before: # Solution
