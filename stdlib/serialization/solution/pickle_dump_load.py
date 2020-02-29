import pickle
from dataclasses import dataclass
from pprint import pprint
from typing import List


@dataclass
class Mission:
    year: int
    name: str


@dataclass
class Astronaut:
    name: str
    missions: List[Mission] = ()


INPUT = [
    Astronaut('Jan Twardowski', missions=[
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3')]),

    Astronaut('Mark Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa Lewis', missions=[]),
]

with open(r'/tmp/astronauts.pkl', mode='wb') as file:
    pickle.dump(INPUT, file)


with open(r'/tmp/astronauts.pkl', mode='rb') as file:
    output = pickle.load(file)


pprint(output)
# [
#   Astronaut(name='Jan Twardowski', missions=[
#       Mission(year=1969, name='Apollo 11'),
#       Mission(year=2024, name='Artemis 3')]),
#
#   Astronaut(name='Mark Watney', missions=[
#       Mission(year=2035, name='Ares 3')]),
#
#   Astronaut(name='Melissa Lewis', missions=[])
# ]
