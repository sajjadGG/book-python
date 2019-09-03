class Astronaut:
    def __init__(self, name, locations=()):
        self.name = name
        self.locations = list(locations)

    def __str__(self):
        return f'{self.name}, {self.locations}'

    def __iadd__(self, other):
        self.locations.append(other)
        return self

    def __contains__(self, item):
        for address in self.locations:
            if address == item:
                return True
        return False


class Location:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\n\t{self.name}'

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


astro = Astronaut('Jan Twardowski', locations=(
    Location('Armstrong Flight Research Center'),
    Location('Kennedy Space Center'),
))

astro += Location('Jet Propulsion Laboratory')
astro += Location('Johnson Space Center')

print(astro)
# Jan Twardowski, [
#     Armstrong Flight Research Center,
#     Kennedy Space Center,
#     Jet Propulsion Laboratory,
#     Johnson Space Center]

if Location('Johnson Space Center') in astro:
    print(True)
else:
    print(False)
# True
