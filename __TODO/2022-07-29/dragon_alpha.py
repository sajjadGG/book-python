"""
>>> import sys; sys.tracebacklimit = 0
>>> from random import seed; seed(0)
>>> assert sys.version_info >= (3, 9), 'Python 3.9+ required'

Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20
>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20
>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15
>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5
>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5
>>> dragon.position_change(down=5)

Smok zadaje obrażenia (5-20)
>>> dmg = dragon.make_damage()

>>> try:
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi
...     dragon.take_damage(5)   # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)   # Zadaj 3 obrażeń smokowi
...     dragon.take_damage(2)   # Zadaj 2 obrażeń smokowi
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
...     print(f'Position: {drop.position}')
Wawelski is dead
Gold: 98
Position: Point(x=20, y=40)

Smok powinien zginąć na pozycji: x=20, y=40
>>> dragon.position_get()
Point(x=20, y=40)
"""
from abc import ABC, abstractproperty
from dataclasses import dataclass
from enum import Enum
from random import randint
from typing import ClassVar, NamedTuple
from unittest import TestCase


@dataclass(frozen=True, slots=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError


class HasPosition:
    position: Point

    def __init__(self, x: int = 0, y: int = 0):
        self.position_set(x=x, y=y)

    def position_set(self, *, x: int, y: int) -> None:
        self.position = Point(x=x, y=y)

    def position_change(self, *,
                        left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0,
                        ) -> None:
        current = self.position_get()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.position_set(x=new_x, y=new_y)

    def position_get(self) -> Point:
        return self.position


class Status(Enum):
    ALIVE: ClassVar[str] = 'alive'
    DEAD: ClassVar[str] = 'dead'


class Drop(NamedTuple):
    gold: int
    position: Point

class CanDamage(ABC):
    @abstractproperty
    def DAMAGE_MIN(self) -> int: ...

    @abstractproperty
    def DAMAGE_MAX(self) -> int: ...

    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)


# class HasGold
# class HasHealth
# class HasTexture
# class HasStatus

# class Dragon(HasHealth, HasStatus, HasTexture, HasGold, HasPosition, CanDamage)
class Dragon(HasPosition, CanDamage):
    name: str
    texture: str
    health = property()
    _health: int
    DAMAGE_MIN: ClassVar[int] = 5
    DAMAGE_MAX: ClassVar[int] = 20
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    def __init__(self, name: str, /,
                 *, position_x: int = 0, position_y: int = 0,
                 ) -> None:
        self.name = name
        self._health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)

    class IsDead(Exception):
        pass

    class IsAlive(Exception):
        pass

    @health.setter
    def health(self, value) -> None:
        self._health = value
        if self._health > 0:
            self.status = Status.ALIVE
            self.texture = self.TEXTURE_ALIVE
        else:
            self.status = Status.DEAD
            self.texture = self.TEXTURE_DEAD
            raise self.IsDead()

    @health.getter
    def health(self) -> int:
        return self._health

    def take_damage(self, damage, /) -> None:
        self.health -= damage

    def get_drop(self) -> Drop:
        if self.is_alive():
            raise self.IsAlive('Dragon is alive and cannot drop')
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())

    def is_alive(self) -> bool:
        return self.health > 0


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.current = HasPosition(x=10, y=20)

    def test_position_get(self):
        current = self.current.position_get()
        self.assertEqual(current.x, 10)
        self.assertEqual(current.y, 20)

    def test_position_set_positional(self):
        with self.assertRaises(TypeError):
            self.current.position_set(1, 2)  # noqa

    def test_position_set_keyword(self):
        self.current.position_set(x=1, y=2)
        self.assertEqual(self.current.position.x, 1)
        self.assertEqual(self.current.position.y, 2)

    def test_position_move_keyword(self):
        with self.assertRaises(TypeError):
            self.current.position_change(1)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3)  # noqa
        with self.assertRaises(TypeError):
            self.current.position_change(1, 2, 3, 4)  # noqa

    def test_position_move_left(self):
        self.current.position_change(left=1)
        self.assertEqual(self.current.position.x, 9)
        self.assertEqual(self.current.position.y, 20)

    def test_position_move_right(self):
        self.current.position_change(right=1)
        self.assertEqual(self.current.position.x, 11)
        self.assertEqual(self.current.position.y, 20)

    def test_position_move_up(self):
        self.current.position_change(up=1)
        self.assertEqual(self.current.position.x, 10)
        self.assertEqual(self.current.position.y, 19)

    def test_position_move_down(self):
        self.current.position_change(down=1)
        self.assertEqual(self.current.position.x, 10)
        self.assertEqual(self.current.position.y, 21)

    def test_position_move_vertical(self):
        self.current.position_change(up=1, down=2)
        self.assertEqual(self.current.position.x, 10)
        self.assertEqual(self.current.position.y, 21)

    def test_position_move_horizontal(self):
        self.current.position_change(left=1, right=2)
        self.assertEqual(self.current.position.x, 11)
        self.assertEqual(self.current.position.y, 20)

    def test_position_move_omnidirectional(self):
        self.current.position_change(left=1, right=2, up=3, down=4)
        self.assertEqual(self.current.position.x, 11)
        self.assertEqual(self.current.position.y, 21)


class DragonTest(TestCase):

    # Initialization

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon.position.x, 1)
        self.assertEqual(dragon.position.y, 2)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, position_y=2)  # noqa

    # Other methods

    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_status_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_status_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_status_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_texture_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_damage_take_and_health_positive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_and_health_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)
        self.assertEqual(self.dragon.health, 0)

    def test_damage_take_and_health_negative(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(3)
        self.assertEqual(self.dragon.health, -1)

    def test_drop_and_health_positive(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsAlive):
            self.dragon.get_drop()

    def test_drop_and_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        drop = self.dragon.get_drop()
        self.assertIn(drop.gold, range(1,101))
        self.assertEqual(drop.position, self.dragon.position_get())

    def test_drop_and_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        drop = self.dragon.get_drop()
        self.assertIn(drop.gold, range(1,101))
        self.assertEqual(drop.position, self.dragon.position_get())

    def test_isalive_and_health_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_isalive_and_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_isalive_and_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())
