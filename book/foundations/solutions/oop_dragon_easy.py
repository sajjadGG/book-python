import random


class Dragon:
    def __init__(self, name, hp=100, pos_x=0, pos_y=0, texture='dragon.png'):
        self.name = name
        self.hp = random.randint(50, 100)
        self.position_x = pos_x
        self.position_y = pos_y
        self.texture = texture

    def move(self, left=0, down=0, up=0, right=0):
        self.position_x += right
        self.position_x -= left
        self.position_y -= up
        self.position_y += down

    def set_position(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def get_position(self):
        return self.position_x, self.position_y

    def dead(self):
        print('Dead')
        self.texture = 'dragon-dead.png'
        gold = random.randint(1, 100)
        print(f'Dropped {gold} gold at position {self.get_position()}')

    def hit(self, damage=0):
        self.hp -= damage
        print(f'Damage taken: {damage}, Dragon HP: {self.hp}')

        if self.hp <= 0:
            self.dead()


wawelski = Dragon(name='Wawelski', pos_x=0, pos_y=0)

wawelski.move(left=10, down=20)
wawelski.move(right=15, up=5)

wawelski.hit(10)
wawelski.hit(50)
wawelski.hit(35)
wawelski.hit(20)
