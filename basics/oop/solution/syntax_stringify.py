class Crew:
    def __init__(self, members=()):
        self.members = list(members)

    def __str__(self):
        return '\n'.join(str(astro) for astro in self.members)


class Astronaut:
    def __init__(self, name, locations=()):
        self.name = name
        self.locations = list(locations)

    def __str__(self):
        if self.locations:
            return f'{self.name} {self.locations}'
        else:
            return f'{self.name}'


class Location:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\n\t{self.name}'


melissa = Astronaut('Melissa Lewis')
print(f'Commander: \n{melissa}\n')
# Commander:
# Melissa Lewis


mark = Astronaut('Mark Watney', locations=[
    Location('Johnson Space Center'),
    Location('Kennedy Space Center')
])
print(f'Space Pirate: \n{mark}\n')
# Space Pirate:
# Mark Watney [
# 	Johnson Space Center,
# 	Kennedy Space Center]


crew = Crew([
    Astronaut('Jan Twardowski', locations=[
        Location('Johnson Space Center'),
        Location('Kennedy Space Center'),
        Location('Jet Propulsion Laboratory'),
        Location('Armstrong Flight Research Center'),
    ]),
    Astronaut('José Jiménez'),
    Astronaut('Иван Иванович', locations=[]),
])
print(f'Crew: \n{crew}')
# Crew:
# Jan Twardowski [
# 	Johnson Space Center,
# 	Kennedy Space Center,
# 	Jet Propulsion Laboratory,
# 	Armstrong Flight Research Center]
# José Jiménez
# Иван Иванович
