Interface
=========


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

.. code-block:: python
    :force:

    interface Cache:
        def get(self, key: str) -> str
        def set(self, key: str, value: str) -> None
        def is_valid(self, key: str) -> bool


Example
-------
.. code-block:: python

    from datetime import timedelta


    class CacheInterface:
        timeout: timedelta

        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


Use Cases
---------
.. code-block:: python

    from datetime import timedelta


    class Cache:
        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    class CacheDatabase(Cache):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheRAM(Cache):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheFilesystem(Cache):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    cache: Cache = CacheFilesystem()
    cache.set('name', 'Jan Twardowski')
    cache.is_valid('name')
    cache.get('name')

    cache: Cache = CacheRAM()
    cache.set('name', 'Jan Twardowski')
    cache.is_valid('name')
    cache.get('name')

    cache: Cache = CacheDatabase()
    cache.set('name', 'Jan Twardowski')
    cache.is_valid('name')
    cache.get('name')


Assignments
-----------
.. literalinclude:: ../_assignments/oop_interface_define.py
    :caption: :download:`Solution <../_assignments/oop_interface_define.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_interface_implement.py
    :caption: :download:`Solution <../_assignments/oop_interface_implement.py>`
    :end-before: # Solution
