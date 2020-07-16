**********
Interfaces
**********



What it is?
===========
* Python don't have interfaces
* Cannot instantiate
* Inheriting class must implement all methods
* Only method declaration

.. glossary::
    interface
    implement

.. code-block:: python
    :caption: Interfaces

    class CacheInterface:
        def get(self, key: str) -> str:
            raise NotImplementedError

        def set(self, key: str, value: str) -> None:
            raise NotImplementedError

        def is_valid(self, key: str) -> bool:
            raise NotImplementedError


When use it?
============


Examples
========
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


Assignments
===========

OOP Interface Iris
------------------
* Complexity level: easy
* Lines of code to write: 21 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_interface_iris.py`

:English:
    #. Use code from "Input" section (see below)
    #. Create interface ``IrisInterface``
    #. Create methods ``sum()``, ``avg()``, ``len()`` in ``IrisInterface``
    #. Method ``avg()`` returns ``self.sum()`` divided by ``self.len()``
    #. Methods must raise exception ``NotImplementedError``
    #. Create class ``Setosa`` inheriting from ``IrisInterface``
    #. Create instance of a class ``Setosa`` and call ``avg()`` method
    #. Create instance of a class ``IrisInterface`` and call ``avg()`` method

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Stwórz interfejs ``IrisInterface``
    #. Stwórz metody ``sum()``, ``avg()``, ``len()`` w ``IrisInterface``
    #. Metoda ``avg()`` zwraca ``self.sum()`` dzielony przez ``self.len()``
    #. Metody muszą podnosić wyjątek ``NotImplementedError``
    #. Stwórz klasę ``Setosa`` dziedziczące po ``IrisInterface``
    #. Stwórz instancje klasy ``Setosa`` i wywołaj metodę ``avg()``
    #. Stwórz instancje klasy ``IrisInterface`` i wywołaj metodę ``avg()``

:Input:
    .. code-block:: python

        def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width

    .. code-block:: python

        iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
        setosa = Setosa(5.1, 3.5, 1.4, 0.2)

:Output:
    .. code-block:: python

        setosa.avg()
        # Setosa 2.55

    .. code-block:: python

        iris.avg()
        # Traceback (most recent call last):
        #    ...
        # NotImplementedError
