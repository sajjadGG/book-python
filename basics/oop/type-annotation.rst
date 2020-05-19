.. _OOP Type Annotation:

*******************
OOP Type Annotation
*******************


Rationale
=========
.. highlights::
    * All classes are types
    * Always depend upon abstraction not an implementation (SOLID Dependency Inversion Principle). More info :ref:`OOP SOLID`

.. code-block:: python

    class Astronaut:
        pass


    mark: Astronaut = Astronaut()

.. code-block:: python

    class Cache:
        pass

    class DatabaseCache(Cache):
        pass

    class MemoryCache(Cache):
        pass

    class FilesystemCache(Cache):
        pass


    db: Cache = DatabaseCache()
    mem: Cache = MemoryCache()
    fs: Cache = FilesystemCache()


Method Return Types
===================
.. code-block:: python

    class Astronaut:
        def say_hello(self) -> str:
            return 'My name... José Jiménez'


    mark: Astronaut = Astronaut()
    mark.say_hello()
    # 'My name... José Jiménez'

.. code-block:: python

    class Point:
        def get_coordinates(self) -> Tuple[int, int]:
            return 1, 2


    pt: Point = Point()
    pt.get_coordinates()
    # (1, 2)


Required Method Arguments
=========================
.. code-block:: python

    class Point:
        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname: str, lastname: str) -> None:
            self.firstname: str = firstname
            self.lastname: str = lastname


Optional Method Arguments
=========================
.. code-block:: python

    from typing import Tuple


    class Point:
        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x = x
            self.y = y

        def set_coordinates(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

        def get_coordinates(self) -> Tuple[int, int]:
            return self.x, self.y


    pt: Point = Point()
    pt.set_coordinates(1, 2)
    pt.get_coordinates()
    # (1, 2)


Classes
=======
.. code-block:: python

    class Point:
        def __init__(self, x: int = 0, y: int = 0) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f'Point(x={self.x}, y={self.y})'


    class Position:
        def __init__(self, initial_position: Point = Point()) -> None:
            self.position = initial_position

        def get_coordinates(self) -> Point:
            return self.position


    pos: Position = Position()

    pos.get_coordinates()
    # <__main__.Point object at 0x11c5531c0>

    print(pos.get_coordinates())
    # Point(x=0, y=0)


Nested
======
.. code-block:: python

    from typing import List


    class Iris:
        def __init__(self, features: List[float], label: str) -> None:
            self.features: List[float] = features
            self.label: str = label

    data: List[Iris] = [
        Iris([4.7, 3.2, 1.3, 0.2], 'setosa'),
        Iris([7.0, 3.2, 4.7, 1.4], 'versicolor'),
        Iris([7.6, 3.0, 6.6, 2.1], 'virginica'),
    ]


More Information
================
.. note:: More Information in :ref:`Stdlib Type Annotation`
