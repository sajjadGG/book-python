def say_hello():
    print('Hello')

class Astronaut:
    name = 'Josv Jiménez'

jose = Astronaut()
say_hello()
# Hello


class Astronaut:
    name = 'José Jiménez'

    def say_hello(self):
        print('Hello')

jose = Astronaut()
jose.say_hello()
# Hello


class Astronaut:
    name = 'José Jiménez'

    @staticmethod
    def say_hello():
        print('Hello')

jose = Astronaut()
jose.say_hello()
# Hello
Astronaut.say_hello()
# Hello