class Astronaut:
    name = 'José Jiménez'

    def say_hello(self, text='Hello'):
        print(f'{text} {self.name}')


jose = Astronaut()

jose.say_hello()
# Hello José Jiménez

jose.say_hello('My name is')
# My name is José Jiménez