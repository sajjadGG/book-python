import logging
from dataclasses import dataclass
from random import randint
from typing import Optional, Dict, Any, NoReturn


def if_alive(method):
    def wrapper(dragon, *args, **kwargs):
        if dragon.is_alive():
            return method(dragon, *args, **kwargs)
    return wrapper

@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self) -> None:
        if self.x < 0:
            raise ValueError('``x`` cannot be negative')

        if self.y < 0:
            raise ValueError('``y`` cannot be negative')


class Movable:
    @if_alive
    def set_position(self, position: Point = Point()) -> None:
        self._position: Point = position

    @if_alive
    def change_position(self, left: int = 0, down: int = 0, up: int = 0, right: int = 0) -> None:
        current_position: Point = self.get_position()
        x: int = current_position.x + right - left
        y: int = current_position.y + down - up
        self.set_position(Point(x, y))

    def get_position(self) -> Point:
        return self._position

    def __str__(self) -> str:
        current_position: Point = self.get_position()
        return f'Movable(x={current_position.x}, y={current_position.y})'


class Status:
    DEAD: str = 'dead'
    ALIVE: str = 'alive'


class Dragon(Movable):
    HEALTH_MIN: int = 50
    HEALTH_MAX: int = 100
    DAMAGE_MIN: int = 5
    DAMAGE_MAX: int = 20
    GOLD_MIN: int = 1
    GOLD_MAX: int = 100
    TEXTURE_ALIVE: str = r'img/dragon/alive.png'
    TEXTURE_DEAD: str = r'img/dragon/dead.png'

    class IsDead(Exception):
        pass

    def __init__(self, name: str, position: Point = Point()):
        self.name: str = name
        self.texture: str = self.TEXTURE_ALIVE
        self.health_current: int = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold: int = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.update_status()
        self.set_position(position)

    def is_dead(self) -> bool:
        if self.status == Status.DEAD:
            return True
        else:
            return False

    def is_alive(self) -> bool:
        return not self.is_dead()

    def update_status(self) -> None:
        if self.health_current > 0:
            self.status: str = Status.ALIVE
        else:
            self.status: str = Status.DEAD

    def get_drop(self) -> Dict[str, Any]:
        return {
            'gold': self.gold,
            'position': self.get_position(),
        }

    @if_alive
    def make_damage(self) -> Optional[int]:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def make_dead(self) -> NoReturn:
        self.texture = self.TEXTURE_DEAD
        raise Dragon.IsDead

    @if_alive
    def take_damage(self, damage: int) -> Optional[NoReturn]:
        self.health_current -= damage
        self.update_status()
        logging.info(f'{self.name} got: {damage}, HP left: {self.health_current}')

        if self.is_dead():
            self.make_dead()


dragon: Dragon = Dragon(name='Wawelski', position=Point(x=50, y=120))

dragon.set_position(Point(x=10, y=20))
dragon.change_position(left=10, down=20)
dragon.change_position(left=10, right=15)
dragon.change_position(right=15, up=5)
dragon.change_position(down=5)

try:
    dragon.take_damage(10)
    dragon.take_damage(5)
    dragon.take_damage(3)
    dragon.take_damage(2)
    dragon.take_damage(15)
    dragon.take_damage(25)
    dragon.take_damage(75)

except Dragon.IsDead:
    drop: Dict[str, Any] = dragon.get_drop()

    print(f'{dragon.name} is dead')
    print(f'Gold dropped: {drop["gold"]}')
    print(f'Movable: {drop["position"]}')
