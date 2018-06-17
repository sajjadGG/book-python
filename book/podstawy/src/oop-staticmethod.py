def say_hello():
    print('Hello')

class Astronaut:
    name = 'Jose Jimenez'

jose = Astronaut()
say_hello()
# Hello


class Astronaut:
    name = 'Jose Jimenez'

    def say_hello(self):
        print('Hello')

jose = Astronaut()
jose.say_hello()
# Hello


class Astronaut:
    name = 'Jose Jimenez'

    @staticmethod
    def say_hello():
        print('Hello')

jose = Astronaut()
jose.say_hello()
# Hello
Astronaut.say_hello()
# Hello