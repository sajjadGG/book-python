class Astronaut:
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'My name is {self.name}')


class MaleAstronaut(Astronaut):
    gender = 'male'


class Gieroj(MaleAstronaut):
    status = 'hero'


ivan = Gieroj(name='Ivan')
ivan.say_hallo()
# My name is Ivan
ivan.status
# hero
ivan.gender
# male
