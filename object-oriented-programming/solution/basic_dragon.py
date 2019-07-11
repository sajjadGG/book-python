from dataclasses import dataclass
from random import randint
from typing import Optional, Dict, Any


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0:
            raise ValueError('``x`` cannot be negative')

        if self.y < 0:
            raise ValueError('``y`` cannot be negative')


class Movable:
    def position_set(self, point: Point) -> None:
        self._position: Point = point

    def position_change(self, left: int = 0, down: int = 0, right: int = 0, up: int = 0):
        current_position: Point = self.position_get()
        x: int = current_position.x + right - left
        y: int = current_position.y + down - up
        self.position_set(Point(x, y))

    def position_get(self) -> Point:
        return self._position


class Status:
    DEAD: str = 'dead'
    ALIVE: str = 'alive'


class Dragon(Movable):
    TEXTURE_ALIVE: str = 'img/dragon/alive.png'
    TEXTURE_DEAD: str = 'img/dragon/dead.png'
    HEALTH_MIN: int = 50
    HEALTH_MAX: int = 100
    DAMAGE_MIN: int = 5
    DAMAGE_MAX: int = 20
    GOLD_MIN: int = 1
    GOLD_MAX: int = 100

    def __init__(self, name: str, position: Point = Point()) -> None:
        self.name: str = name
        self.texture: str = self.TEXTURE_ALIVE
        self.health: int = self._get_initial_health()
        self.gold: int = randint(self.GOLD_MIN, self.GOLD_MAX)
        self._position: Point = position
        self.position_set(position)
        self.update_status()

    def _get_initial_health(self) -> int:
        return randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def update_status(self) -> None:
        if self.health > 0:
            self.status = Status.ALIVE
        else:
            self.status = Status.DEAD

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        if self.status == Status.DEAD:
            return True
        else:
            return False

    def attack(self) -> Optional[int]:
        if self.is_alive():
            return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def _get_drop(self) -> Dict[str, Any]:
        gold: int = self.gold
        self.gold: int = 0

        return {
            'gold': gold,
        }

    def _die(self) -> Dict[str, Any]:
        self.texture: str = self.TEXTURE_DEAD
        drop: Dict[str, Any] = self._get_drop()

        print(f'{self.name} is dead')
        print(f'Gold {drop["gold"]}')
        print(f'Position {self.position_get()}')

        return drop

    def take_damage(self, damage: int) -> Optional[Dict[str, Any]]:
        if self.is_dead():
            return

        self.health -= damage
        self.update_status()

        print(f'{self.name}, DMG: {damage}, now HP: {self.health}')

        if self.is_dead():
            return self._die()


# wawelski = Dragon(name='Wawelski', x=50, y=120)
# wawelski = Dragon(name='Wawelski', pos_x=50, pos_y=120)
# wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)

# wawelski = Dragon(name='Wawelski', pos=(50, 120))
# wawelski = Dragon(name='Wawelski', position=(50, 120))
# wawelski = Dragon(name='Wawelski', position={'x': 50, 'y': 120})


# wawelski = Dragon(name='Wawelski', position=Movable(50, 120))


wawelski = Dragon(name='Wawelski', position=Point(x=50, y=120))

wawelski.position_set(Point(x=10, y=20))

# wawelski.move_left()
# wawelski.move_right()
# wawelski.move_up()
# wawelski.move_down()

wawelski.position_change(left=10, down=20)
wawelski.position_change(left=10, right=15)
wawelski.position_change(up=5, right=15)
wawelski.position_change(down=5)

# wawelski.move([{'left': ..., 'right': ...}])
# wawelski.move(dx=..., dy=...)

# wawelski.position.move(left, down, up, right)

wawelski.take_damage(10)
wawelski.take_damage(5)
wawelski.take_damage(3)
wawelski.take_damage(2)
wawelski.take_damage(15)
wawelski.take_damage(25)
wawelski.take_damage(75)
