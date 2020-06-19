class Crew:
    def __init__(self, members=()):
        self.members = list(members)

    def __str__(self):
        return '\n'.join(str(astro) for astro in self.members)


class Astronaut:
    def __init__(self, name, experience=()):
        self.name = name
        self.experience = list(experience)

    def __str__(self):
        if self.experience:
            return f'{self.name} veteran of {self.experience}'
        else:
            return f'{self.name}'


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\t{self.year}: {self.name}'


melissa = Astronaut('Melissa Lewis')
print(f'Commander: \n{melissa}\n')
# Commander:
# Melissa Lewis


mark = Astronaut('Mark Watney', experience=[
    Mission(2035, 'Ares 3'),
])
print(f'Space Pirate: \n{mark}\n')
# Space Pirate:
# Mark Watney veteran of [
# 	2035: Ares 3]


crew = Crew([
    Astronaut('Jan Twardowski', experience=[
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3'),
    ]),
    Astronaut('José Jiménez'),
    Astronaut('Mark Watney', experience=[
        Mission(2035, 'Ares 3'),
    ]),
])

print(f'Crew: \n{crew}')
# Crew:
# Jan Twardowski veteran of [
# 	1969: Apollo 11,
# 	2024: Artemis 3]
# José Jiménez
# Mark Watney veteran of [
# 	2035: Ares 3]
