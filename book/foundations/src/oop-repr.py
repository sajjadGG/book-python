class Astronaut:
    def __init__(self, name, agency='NASA'):
        self.name = name
        self.agency = agency

    def __str__(self):
        return f'My name {self.name}'

    def __repr__(self):
        return f'Astronaut(name="{self.name}", agency="{self.agency}")'


jose = Astronaut(name='Jose Jimenez', agency='NASA')
print(jose)
# My name Jose Jimenez

crew = [
    Astronaut(name='Jose Jimenez', agency='NASA'),
    Astronaut(name='Max Peck', agency='NASA'),
    Astronaut(name='Ivan Ivanovic', agency='Roscosmos'),
]

print(crew)
# Astronaut(name='Jose Jimenez', agency='NASA'),
# Astronaut(name='Max Peck', agency='NASA'),
# Astronaut(name='Ivan Ivanovic', agency='Roscosmos'),
