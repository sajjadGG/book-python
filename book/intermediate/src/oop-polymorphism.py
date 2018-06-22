class Astronaut:
    agency = None

    def say_hello(self):
        raise NotImplementedError


class NASAAstronaut(Astronaut):
    agency = 'NASA'

    def say_hello(self):
        print(f'Howdy from {self.agency}')


class ESAAstronaut(Astronaut):
    agency = 'ESA'

    def say_hello(self):
        print(f'Guten Tag aus {self.agency}')


class RoscosmosAstronaut(Astronaut):
    agency = 'Roscosmos'

    def say_hello(self):
        print(f'Privyet z {self.agency}')


astronaut = NASAAstronaut()
astronaut.say_hello()  # Howdy from NASA

astronaut = RoscosmosAstronaut()
astronaut.say_hello()  # Privyet z Roscosmos


# Instead of...
agency = 'NASA'

if agency == 'NASA':
    print('Howdy from NASA')
elif agency == 'Roscosmos':
    print('Privyet z Roscosmos')
elif agency == 'ESA':
    print('Guten Tag aus ESA')
else:
    raise NotImplementedError
