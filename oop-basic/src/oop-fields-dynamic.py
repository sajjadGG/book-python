class Astronaut:
    def __init__(self, name, age=30, agency='NASA'):
        self.name = name
        self.agency = agency
        self.age = age


jose = Astronaut(name='José Jiménez')
jose.agency     # NASA

ivan = Astronaut(name='Иван Иванович', agency='Roscosmos')
ivan.agency     # Roscosmos
