class Astronaut:
    name = 'José Jiménez'

astro = Astronaut()
print(astro)
# <__main__.Astronaut object at 0x01E3FDF0>


class Astronaut:
    name = 'José Jiménez'
    def __str__(self):
        return f'My name {self.name}'

astro = Astronaut()
print(astro)  # print converts it's arguments to ``str()`` before printing
# My name José Jiménez
