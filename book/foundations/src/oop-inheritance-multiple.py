class Astronaut:
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'My name is {self.name}')


class MaleAstonaut(Astronaut):
    gender = 'male'


class Gieroj(MaleAstonaut):
    status = 'hero'


ivan = MaleAstonaut(name='Ivan')
ivan.say_hallo()
# My name is Ivan
