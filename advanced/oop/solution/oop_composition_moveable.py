"""
>>> class Astronaut(Moveable):
...     pass

>>> astro = Astronaut()
>>> astro.get_position()
Point(x=0, y=0)

>>> astro.change_position(right=10)
>>> astro.get_position()
Point(x=10, y=0)

>>> astro.change_position(left=5)
>>> astro.get_position()
Point(x=5, y=0)

>>> astro.change_position(down=10)
>>> astro.get_position()
Point(x=5, y=10)

>>> astro.change_position(up=5)
>>> astro.get_position()
Point(x=5, y=5)

>>> astro.set_position(x=0, y=0)
>>> astro.get_position()
Point(x=0, y=0)
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Moveable:
    _position: Point = Point()

    def get_position(self):
        return self._position

    def set_position(self, x, y):
        self._position = Point(x, y)

    def change_position(self, left=0, right=0, up=0, down=0):
        current = self._position
        x = current.x + right - left
        y = current.y + down - up
        self.set_position(x, y)
