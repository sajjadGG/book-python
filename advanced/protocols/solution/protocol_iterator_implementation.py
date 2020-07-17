from dataclasses import dataclass


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.missions):
            raise StopIteration

        result = self.missions[self._iter_index]
        self._iter_index += 1
        return result


@dataclass
class Mission:
    year: int
    name: str


twardowski = Astronaut('Jan', 'Twardowski', missions=(
    Mission(1969, 'Apollo 11'),
    Mission(2024, 'Artemis 3'),
    Mission(2035, 'Ares 3'),
))

for mission in twardowski:
    print(mission)

# Mission(year=1969, name='Apollo 11')
# Mission(year=2024, name='Artemis 3')
# Mission(year=2035, name='Ares 3')
