class Astronaut:
    def say_hello(self):
        print('I am an astronaut')


class Jose(Astronaut):
    def say_hello(self):
        print('My name José Jiménez')
        super().say_hello()


jose = Astronaut()
jose.say_hello()
# My name José Jiménez
# I am an astronaut
