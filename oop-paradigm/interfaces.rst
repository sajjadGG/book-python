**********
Interfaces
**********



What it is?
===========
* Nie można tworzyć instancji
* Wszystkie metody muszą być zaimplementowane przez potomków
* Tylko deklaracje metod
* Metody nie mogą mieć implementacji


When use it?
============


Example
=======
.. code-block:: python
    :caption: Interfaces

    class CacheInterface:
        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


    class CacheDatabase(CacheInterface):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheRAM(CacheInterface):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    class CacheFilesystem(CacheInterface):
        def is_valid(self, key: str) -> bool:
            ...

        def get(self, key: str) -> str:
            ...

        def set(self, key: str, value: str) -> None:
            ...


    fs = CacheFilesystem()
    fs.set('name', 'Jan Twardowski')
    fs.is_valid('name')
    fs.get('name')

    ram = CacheRAM()
    ram.set('name', 'Jan Twardowski')
    ram.is_valid('name')
    ram.get('name')

    db = CacheDatabase()
    db.set('name', 'Jan Twardowski')
    db.is_valid('name')
    db.get('name')

