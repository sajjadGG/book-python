class Astronaut:
    def say_hello(self):
        print('Hello')


class Jose(Astronaut):
    def say_hello(self):
        print('¡Hola!')
        super().say_hello()
