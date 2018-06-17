class Astronaut:
    agency = 'NASA'


# Objects - Instances
ivan = Astronaut()
jose = Astronaut()
max = Astronaut()

ivan.agency  # NASA
jose.agency  # NASA
max.agency  # NASA
Astronaut.agency  # NASA

ivan.agency = 'Roscosmos'

ivan.agency  # Roscosmos
jose.agency  # NASA
max.agency  # NASA
Astronaut.agency  # NASA

Astronaut.agency = 'ESA'

ivan.agency  # Roscosmos
jose.agency  # ESA
max.agency  # ESA
Astronaut.agency  # ESA