class Astronaut:
    name = 'José Jiménez'


jose = Astronaut()
print(jose)
# <__main__.Astronaut object at 0x01E3FDF0>


class Astronaut:
    name = 'José Jiménez'

    def __str__(self):
        return f'My name {self.name}'


jose = Astronaut()
print(jose)
# My name José Jiménez
