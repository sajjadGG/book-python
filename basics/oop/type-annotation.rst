OOP Type Annotation
===================


Rationale
---------
* All classes are types
* Always depend upon abstraction not an implementation (SOLID Dependency Inversion Principle). More information in :ref:`OOP SOLID`

>>> class Astronaut:
...     pass
>>>
>>>
>>> mark: Astronaut = Astronaut()

>>> class Cache:
...     pass
>>>
>>> class DatabaseCache(Cache):
...     pass
>>>
>>> class MemoryCache(Cache):
...     pass
>>>
>>> class FilesystemCache(Cache):
...     pass
>>>
>>>
>>> db: Cache = DatabaseCache()
>>> mem: Cache = MemoryCache()
>>> fs: Cache = FilesystemCache()


Attributes
----------
>>> class Point:
...     x: int
...     y: int
...
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y

>>> class Point:
...     def __init__(self, x, y):
...         self.x: int = x
...         self.y: int = y


Method Return Types
-------------------
>>> class Astronaut:
...     def say_hello(self) -> str:
...         return 'My name... José Jiménez'
>>>
>>>
>>> mark: Astronaut = Astronaut()
>>> mark.say_hello()
'My name... José Jiménez'

>>> class Point:
...     def get_coordinates(self) -> tuple[int, int]:
...         return 1, 2
>>>
>>>
>>> pt: Point = Point()
>>> pt.get_coordinates()
(1, 2)


Required Method Arguments
-------------------------
>>> class Point:
...     def __init__(self, x: int, y: int) -> None:
...         self.x = x
...         self.y = y
>>>
>>> class Astronaut:
...     def __init__(self, firstname: str, lastname: str) -> None:
...         self.firstname: str = firstname
...         self.lastname: str = lastname


Optional Method Arguments
-------------------------
>>> class Point:
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
...
...     def set_coordinates(self, x: int, y: int) -> None:
...         self.x = x
...         self.y = y
...
...     def get_coordinates(self) -> tuple[int, int]:
...         return self.x, self.y
>>>
>>>
>>> pt: Point = Point()
>>> pt.set_coordinates(1, 2)
>>> pt.get_coordinates()
(1, 2)


Classes
-------
>>> class Point:
...     def __init__(self, x: int = 0, y: int = 0) -> None:
...         self.x = x
...         self.y = y
...
...     def __str__(self) -> str:
...         return f'Point(x={self.x}, y={self.y})'
>>>
>>>
>>> class Position:
...      def __init__(self, initial_position: Point = Point()) -> None:
...          self.position = initial_position
...
...      def get_coordinates(self) -> Point:
...          return self.position
>>>
>>>
>>> pos: Position = Position()
>>>
>>> pos.get_coordinates()  # doctest: +ELLIPSIS
<Point object at 0x...>
>>>
>>> print(pos.get_coordinates())
Point(x=0, y=0)


Nested
------
>>> class Iris:
...     def __init__(self, features: list[float], label: str) -> None:
...         self.features: list[float] = features
...         self.label: str = label
>>>
>>> data: list[Iris] = [
...     Iris([4.7, 3.2, 1.3, 0.2], 'setosa'),
...     Iris([7.0, 3.2, 4.7, 1.4], 'versicolor'),
...     Iris([7.6, 3.0, 6.6, 2.1], 'virginica')]


Final Class
-----------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

>>> from typing import final
>>>
>>>
>>> @final
... class Astronaut:
...     pass

Error: Cannot inherit from final class "Base":

>>> from typing import final
>>>
>>>
>>> @final
... class Astronaut:
...     pass
>>>
>>> class Pilot(Astronaut):
...     pass


Final Method
------------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing

>>> from typing import final
>>>
>>>
>>> class Astronaut:
...     @final
...     def say_hello(self) -> None:
...         pass


Error: Cannot override final attribute "foo" (previously declared in base class "Base"):

>>> from typing import final
>>>
>>>
>>> class Astronaut:
...     @final
...     def say_hello(self) -> None:
...         pass
>>>
>>> class Pilot(Astronaut):
...     def say_hello(self) -> None:    # Error: Cannot override final attribute
...         pass


Final Attribute
---------------
>>> from typing import Final
>>>
>>>
>>> class Position:
...     x: Final[int]
...     y: Final[int]
...
...     def __init__(self) -> None:
...         self.x = 1
...         self.y = 2

Error: final attribute (``y``) without an initializer:

>>> from typing import Final
>>>
>>>
>>> class Position:
...     x: Final[int]
...     y: Final[int]       # Error: final attribute 'y' without an initializer
...
...     def __init__(self) -> None:
...         self.x = 1

Error: can't override a final attribute:

>>> from typing import Final
>>>
>>>
>>> class Settings:
...     RESOLUTION_X_MIN: Final[int] = 0
...     RESOLUTION_X_MAX: Final[int] = 1024
...     RESOLUTION_Y_MIN: Final[int] = 0
...     RESOLUTION_Y_MAX: Final[int] = 768
>>>
>>>
>>> class Game(Settings):
...     RESOLUTION_X_MIN = 3        # Error: can't override a final attribute

Error: can't override a final attribute:

>>> from typing import Final
>>>
>>>
>>> class Hero:
...     DAMAGE_MIN: Final[int] = 10
...     DAMAGE_MAX: Final[int] = 20
>>>
>>>
>>> Hero.DAMAGE_MIN = 1             # Error: can't override a final attribute


More Information
----------------
* More information in :ref:`Type Annotations` and :ref:`CI/CD Type Checking`
