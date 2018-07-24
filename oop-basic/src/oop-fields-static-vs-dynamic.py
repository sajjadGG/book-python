class Astronaut:
    agency = 'NASA'

    def __init__(self, name):
        self.name = name


# Objects - Instances
ivan = Astronaut(name='Иван Иванович')
jose = Astronaut(name='José Jiménez')
max = Astronaut(name='Max Peck')

ivan.agency         # NASA
jose.agency         # NASA
max.agency          # NASA
Astronaut.agency    # NASA

ivan.agency = 'Roscosmos'

ivan.agency         # Roscosmos
jose.agency         # NASA
max.agency          # NASA
Astronaut.agency    # NASA

Astronaut.agency = 'ESA'

ivan.agency         # Roscosmos
jose.agency         # ESA
max.agency          # ESA
Astronaut.agency    # ESA
