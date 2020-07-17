import pickle
from dataclasses import dataclass


class PickleSerializable:
    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, data):
        return pickle.loads(data)


@dataclass
class Person:
    firstname: str
    lastname: str


class Astronaut(Person, PickleSerializable):
    pass


class Cosmonaut(Person, PickleSerializable):
    pass


watney = Astronaut('Mark', 'Watney')
lewis = Astronaut('Melissa', 'Lewis')
twardowski = Astronaut('Jan', 'Twardowski')
ivanovic = Astronaut('Ivan', 'Ivanovic')

print(watney.to_pickle())
# b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x04\x00\x00\x00Markq\x04X\t\x00\x00\x00lastnameq\x05X\x06\x00\x00\x00Watneyq\x06ub.'

watney = Astronaut.from_pickle(b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x04\x00\x00\x00Markq\x04X\t\x00\x00\x00lastnameq\x05X\x06\x00\x00\x00Watneyq\x06ub.')
print(watney)
