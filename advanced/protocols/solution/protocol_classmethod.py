from dataclasses import dataclass
from pprint import pprint


class CSVMixin:
    def to_csv(self):
        return ','.join(self.__dict__.values())

    @classmethod
    def from_csv(cls, data):
        return cls(*data.split(','))


@dataclass
class Person:
    firstname: str
    lastname: str


class Astronaut(Person, CSVMixin):
    pass


class Cosmonaut(Person, CSVMixin):
    pass




FILE = r'/tmp/protocol-classmethod.csv'

watney = Astronaut('Mark', 'Watney')
twardowski = Cosmonaut('Jan', 'Twardowski')

with open(FILE, mode='wt') as file:
    file.write(watney.to_csv() + '\n')
    file.write(twardowski.to_csv() + '\n')

del watney
del twardowski

result = []

with open(FILE, mode='rt') as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip()

    result.append(Astronaut.from_csv(line1))
    result.append(Cosmonaut.from_csv(line2))


pprint(result)
# [Astronaut(firstname='Mark', lastname='Watney'),
#  Cosmonaut(firstname='Jan', lastname='Twardowski')]
