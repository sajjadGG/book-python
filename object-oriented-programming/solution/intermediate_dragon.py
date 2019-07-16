from enum import Enum
from basic_dragon_advanced import Dragon, Status, Point, Movable


class Status(Status):
    FULL_HEALTH = 'Full Health'
    INJURED = 'Injured'
    BADLY_WOUNDED = 'Badly Wounded'
    NEAR_DEAD = 'Near Death'


class Config:
    BORDER_X_MAX = 1024
    BORDER_X_MIN = 0
    BORDER_Y_MAX = 768
    BORDER_Y_MIN = 0


class Character(Dragon):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_status()

    def update_status(self):
        if not hasattr(self, 'health_full'):
            self.health_full = self.health_current

        procent = self.health_current / self.health_full * 100

        if procent == 100:
            self.status = Status.FULL_HEALTH
        elif 75 <= procent < 100:
            self.status = Status.INJURED
        elif 25 <= procent < 75:
            self.status = Status.BADLY_WOUNDED
        elif 0 < procent < 25:
            self.status = Status.NEAR_DEAD
        else:
            self.status = Status.DEAD

    def set_position(self, position: Point = Point()) -> None:
        """
        >>> dragon = Character(name='Red', position=Point(0, 0))
        >>> dragon.change_position(right=1)
        >>> dragon.get_position()
        Point(x=1, y=0)
        >>> dragon.change_position(down=1)
        >>> dragon.get_position()
        Point(x=1, y=1)
        >>> dragon.change_position(left=2)
        >>> dragon.get_position()
        Point(x=0, y=1)
        >>> dragon.change_position(up=2)
        >>> dragon.get_position()
        Point(x=1, y=1)
        """
        current_position = self.get_position()
        x = current_position.x
        y = current_position.y

        if x > Config.BORDER_X_MAX:
            x = Config.BORDER_X_MAX

        if x < Config.BORDER_X_MIN:
            x = Config.BORDER_X_MIN

        if y > Config.BORDER_Y_MAX:
            y = Config.BORDER_Y_MAX

        if y < Config.BORDER_Y_MIN:
            y = Config.BORDER_Y_MIN

        super().set_position(Point(x, y))


class CharacterClass(Enum):
    WARRIOR = 'Warrior'


class MediumDragon(Character):
    HIT_POINTS_MIN = 100
    HIT_POINTS_MAX = 150


class Hero(Character):
    HIT_POINTS_MIN = 200
    HIT_POINTS_MAX = 250
    DAMAGE_MIN = 1
    DAMAGE_MAX = 15
    GOLD_MIN = 0
    GOLD_MAX = 0
    CHARACTER_CLASS = CharacterClass.WARRIOR


def run():
    dragon = MediumDragon(name='Wawelski')
    hero = Hero(name='Jan Twardowski')

    turn = 1

    while dragon.is_alive() and hero.is_alive():
        print(f'\nTurn: {turn}')

        dmg = dragon.make_damage()
        hero.take_damage(dmg)

        if hero.is_alive():
            dmg = hero.make_damage()
            dragon.take_damage(dmg)

        if dragon.is_dead():
            drop = dragon.get_drop()
            hero.gold += drop['gold']
            print(f'{hero.name} now has: {hero.gold} gold')

        turn += 1


if __name__ == '__main__':
    run()
