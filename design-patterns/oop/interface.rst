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

The following code is not a valid Python syntax. It is only to demonstrate how interfaces generally works.

.. code-block:: python
    :force:

    interface Cache:
        def set(self, key: str, value: str) -> None
        def get(self, key: str) -> str
        def is_valid(self, key: str) -> bool


Example
-------
.. code-block:: python

    class CacheInterface:
        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def get(self, key: str) -> str:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError

.. code-block:: python

    class CacheInterface:
        def set(self, key: str, value: str) -> None: raise NotImplementedError
        def get(self, key: str) -> str: raise NotImplementedError
        def is_valid(self, key: str) -> bool: raise NotImplementedError

Sometimes you may get a shorter code, but it will not raise an error.

.. code-block:: python

    class CacheInterface:
        def set(self, key: str, value: str) -> None: pass
        def get(self, key: str) -> str: pass
        def is_valid(self, key: str) -> bool: pass

The following code is not a valid Python syntax... How nice it would be to write:

    .. code-block:: python

        @interface
        class Cache:
            def set(self, key: str, value: str) -> None: pass
            def get(self, key: str) -> str: pass
            def is_valid(self, key: str) -> bool: pass

    .. code-block:: python
        :force:

        interface Cache:
            def set(self, key: str, value: str) -> None
            def get(self, key: str) -> str
            def is_valid(self, key: str) -> bool


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
.. literalinclude:: ../_assignments/oop_interface_a.py
    :caption: :download:`Solution <../_assignments/oop_interface_a.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_interface_b.py
    :caption: :download:`Solution <../_assignments/oop_interface_b.py>`
    :end-before: # Solution
