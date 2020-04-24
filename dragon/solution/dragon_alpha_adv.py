import logging
from dataclasses import dataclass
from functools import wraps
from random import randint
from typing import TypedDict, NoReturn


logging.basicConfig(
    level=logging.INFO,
    format='"%(asctime).19s", "%(levelname)4.4s", "%(message)s"',
    # filename='/tmp/game.csv',
)


def debug(method):
    @wraps(method)
    def wrapper(instance, *args, **kwargs):
        logging.debug(f'{instance} {method.__name__}(args={args}, kwargs={kwargs})')
        return method(instance, *args, **kwargs)
    return wrapper


def if_alive(action):
    @wraps(action)
    def wrapper(creature, *args, **kwargs):
        if creature.is_alive():
            action(creature, *args, **kwargs)
    return wrapper


def if_dead(action):
    @wraps(action)
    def wrapper(creature, *args, **kwargs):
        if creature.is_dead():
            action(creature, *args, **kwargs)
    return wrapper


class Status:
    ALIVE: str = 'alive'
    DEAD: str = 'dead'


@dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        if self.x < 0:
            raise ValueError('``x`` cannot be negative')

        if self.y < 0:
            raise ValueError('``y`` cannot be negative')


class Movable:
    @if_alive
    def position_set(self, position: Position = Position()) -> None:
        self._position = position

    def position_get(self):
        return self._position

    def position_change(self, left: int = 0, right: int = 0, down: int = 0, up: int = 0) -> None:
        current_position = self.position_get()
        new_position = Position(
            x = current_position.x + right - left,
            y = current_position.y + down - up)
        self.position_set(new_position)


class Drop(TypedDict):
    gold: int
    position: Position


class Dragon(Movable):
    DAMAGE_MIN: int = 5
    DAMAGE_MAX: int = 20
    HEALTH_MIN: int = 50
    HEALTH_MAX: int = 100
    GOLD_MIN: int = 1
    GOLD_MAX: int = 100
    TEXTURE_ALIVE: str = 'img/dragon/alive.png'
    TEXTURE_DEAD: str = 'img/dragon/dead.png'

    class IsDead(Exception):
        pass

    def __init__(self, name: str, position: Position = Position()) -> None:
        self._name: str = name
        self._texture: str = self.TEXTURE_ALIVE
        self._gold: int = randint(self.GOLD_MIN, self.GOLD_MAX)
        self._health_current: int = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self._update_status()
        self.position_set(position)

    @if_alive
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def is_dead(self) -> bool:
        if self._status == Status.DEAD:
            return True
        else:
            return False

    def is_alive(self) -> bool:
        return not self.is_dead()

    @debug
    @if_alive
    def take_damage(self, damage: int):
        self._health_current -= damage
        logging.info(f'Damage taken: {damage}, {self:status}')
        self._update_status()

        if self.is_dead():
            self._make_dead()

    @if_dead
    def _make_dead(self) -> NoReturn:
        self._texture = self.TEXTURE_DEAD
        raise self.IsDead

    def get_drop(self) -> Drop:
        gold = self._gold
        self._gold = 0
        return Drop(gold=gold, position=self.position_get())

    def _update_status(self):
        if self._health_current < 0:
            self._status: str = Status.DEAD
        else:
            self._status: str = Status.ALIVE

    def __format__(self, message):
        if message == Status.DEAD:
            return f'{self} is dead'
        elif message == 'status':
            return f'{self._name} (Status: {self._status}, HP: {self._health_current})'
        else:
            return f'{self._name}'


wawelski = Dragon('Wawelski', position=Position(x=50, y=120))
wawelski.position_set(Position(x=10, y=20))

wawelski.position_change(left=10, down=20)
wawelski.position_change(left=10, right=15)
wawelski.position_change(right=15, up=5)
wawelski.position_change(down=5)

try:
    wawelski.take_damage(10)
    wawelski.take_damage(5)
    wawelski.take_damage(3)
    wawelski.take_damage(2)
    wawelski.take_damage(15)
    wawelski.take_damage(25)
    wawelski.take_damage(75)
except wawelski.IsDead:
    drop: Drop = wawelski.get_drop()

    logging.warning(f'{wawelski:dead}')
    logging.info(f'Gold dropped: {drop["gold"]}')
    logging.info(drop["position"])


""" Alternative interface options

#-> wawelski = Dragon('Wawelski', position_x=50, position_y=120)
#-> wawelski = Dragon('Wawelski', position=Position(50, 120))
#-> wawelski = Dragon('Wawelski', position=Position(x=50, y=120))
# wawelski = Dragon('Wawelski', x=50, y=120)
# wawelski = Dragon('Wawelski', pos_x=50, pos_y=120)
# wawelski = Dragon('Wawelski', xy=(50,120))
# wawelski = Dragon('Wawelski', pos=(50,120))
# wawelski = Dragon('Wawelski', position=(50,120))
# wawelski = Dragon('Wawelski', position_xy=(50,120))
# wawelski = Dragon('Wawelski', position={'x':50, 'y':120})
# wawelski = Dragon('Wawelski', position=Position(position_x=50, position_y=120))

#-> wawelski.set_position(x=10, y=20)
# wawelski.set_position(10, 20)
# wawelski.x = 10
# wawelski.y = 20
# wawelski.position_x = 10
# wawelski.position_y = 20
# wawelski._position_x = 10
# wawelski._position_y = 20

#-> wawelski.move(left=10, down=20)
# wawelski.move(0, 10, 0, 20)
# wawelski.move_left(10)
# wawelski.move_right(10)
# wawelski.move([
#     (0, 10, 0, 20),
#     (0, 10, 0, 20)])
# wawelski.move(dx=10, dy=-20)
# wawelski.move(vertical=10, horizontal=-20)
# wawelski.move(x=10, y=-20)
# wawelski.move_to(x=10, y=20)
# wawelski.move_x(10)
# wawelski.move_y(20)
# wawelski.move_xy(10, 20)
# wawelski.move({'x':50, 'y':120})
# wawelski.move({'left':50, 'down':120})
# wawelski.move([
#     {'left':50, 'down':120},
#     {'left':50, 'right':120},
#     {'down':50}])
# wawelski.move([
#     (10, 20),
#     (50, 120),
#     (5)])
# wawelski.move([
#     (10, 20),
#     (10, 15)])
# wawelski.move([
#     {'x':10, 'y':20},
#     {'x':10, 'y':15}])
# wawelski.move([
#     Position(x=10, y=20),
#     Position(x=10, y=15)])
# wawelski.change_position(left=10, down=20)

#-> wawelski.take_damage()
# wawelski.attack()
# wawelski.hit()
"""
