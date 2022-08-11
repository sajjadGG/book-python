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

>>> mycache: ICache = DatabaseCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')

>>> mycache: ICache = InMemoryCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')

>>> mycache: ICache = FilesystemCache()
>>> mycache.set('firstname', 'Mark')
>>> mycache.is_valid('firstname')
>>> mycache.is_valid('lastname')
>>> mycache.get('firstname')


Use Case - 0x01
---------------
* Cache

File ``cache_iface.py``:

>>> class ICache:
...     def get(self, key: str) -> str:
...         raise NotImplementedError
...
...     def set(self, key: str, value: str) -> None:
...         raise NotImplementedError
...
...     def is_valid(self, key: str) -> bool:
...         raise NotImplementedError

File ``cache_impl.py``:

>>> class DatabaseCache(ICache):
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
>>> class InMemoryCache(ICache):
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
>>> class FilesystemCache(ICache):
...     def is_valid(self, key: str) -> bool:
...         ...
...
...     def get(self, key: str) -> str:
...         ...
...
...     def set(self, key: str, value: str) -> None:
...         ...

File ``settings.py``

>>> from myapp.cache_iface import ICache  # doctest: +SKIP
>>> from myapp.cache_impl import DatabaseCache  # doctest: +SKIP
>>> from myapp.cache_impl import InMemoryCache  # doctest: +SKIP
>>> from myapp.cache_impl import FilesystemCache  # doctest: +SKIP
>>>
>>>
>>> DefaultCache = InMemoryCache

File ``myapp.py``:

>>> from myapp.settings import DefaultCache, ICache  # doctest: +SKIP
>>>
>>>
>>> cache: ICache = DefaultCache()
>>> cache.set('name', 'Mark Watney')
>>> cache.is_valid('name')
>>> cache.get('name')

Note, that myapp doesn't know which cache is being used. It only depends
on configuration in settings file.


Use Case - 0x02
---------------
.. figure:: img/oop-interface-gimp.jpg

    GIMP (GNU Image Manipulation Project) window with tools and canvas [#GIMP]_

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


References
----------
.. [#GIMP] Download GIMP. Year: 2022. Retrieved: 2022-08-11. URL: https://anderbot.com/wp-content/uploads/2020/10/GIMP5.jpg


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
