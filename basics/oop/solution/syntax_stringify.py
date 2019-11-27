class Crew:
    def __init__(self, members=()):
        self.members = list(members)

    def __str__(self):
        output = []
        for astro in self.members:
            output.append(f'{astro.first_name} {astro.last_name} {astro.locations}')
        return '\n'.join(output)

    def __repr__(self):
        return str(self.members)


class Astronaut:
    def __init__(self, first_name, last_name, locations=()):
        self.first_name = first_name
        self.last_name = last_name
        self.locations = list(locations)

    def __str__(self):
        if self.locations:
            return f'{self.first_name} {self.last_name} {self.locations}'
        else:
            return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return str(self)


class Location:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\n\t{self.name}'


melissa = Astronaut(first_name='Melissa', last_name='Lewis')
print(f'Commander: \n{melissa}\n')
# Commander:
# Melissa Lewis

mark = Astronaut(first_name='Mark', last_name='Watney', locations=[Location('Johnson Space Center'), Location('Kennedy Space Center')])
print(f'Space Pirate: \n{mark}\n')
# Space Pirate:
# Mark Watney [Johnson Space Center, Kennedy Space Center]

crew = Crew([
    Astronaut(first_name='Jan', last_name='Twardowski', locations=[
        Location('Johnson Space Center'),
        Location('Kennedy Space Center'),
        Location('Jet Propulsion Laboratory'),
        Location('Armstrong Flight Research Center'),
    ]),
    Astronaut(first_name='José', last_name='Jiménez'),
    Astronaut(first_name='Иван', last_name='Иванович', locations=[]),
])

print(f'Crew: {crew}')
# Crew: [Jan Twardowski [Johnson Space Center, Kennedy Space Center, Jet Propulsion Laboratory, Armstrong Flight Research Center], José Jiménez, Иван Иванович]

