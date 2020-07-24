from dataclasses import dataclass


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


watney = Astronaut('Mark', 'Watney')
lewis = Astronaut('Melissa', 'Lewis')
twardowski = Astronaut('Jan', 'Twardowski')
ivanovic = Astronaut('Ivan', 'Ivanovic')


csv = watney.to_csv()
print(csv)

watney = Astronaut.from_csv(csv)
print(watney)
