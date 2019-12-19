class Astronaut:
    def __init__(self, name, experience=()):
        self.name = name
        self.experience = list(experience)

    def __str__(self):
        return f'{self.name}, {self.experience}'

    def __iadd__(self, other):
        self.experience.append(other)
        return self

    def __contains__(self, flight):
        for mission in self.experience:
            if mission == flight:
                return True
        return False


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\t{self.year}: {self.name}'

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False


astro = Astronaut('Jan Twardowski', experience=[
    Mission(1969, 'Apollo 11'),
])

astro += Mission(2024, 'Artemis 3')
astro += Mission(2035, 'Ares 3')

print(astro)
# Jan Twardowski, [
# 	1969: Apollo 11,
# 	2024: Artemis 3,
# 	2035: Ares 3]

if Mission(2024, 'Artemis 3') in astro:
    print(True)
else:
    print(False)
# True
