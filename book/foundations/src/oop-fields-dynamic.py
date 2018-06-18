class Astronaut:
    def __init__(self, name, agency='NASA'):
        self.name = name
        self.agency = agency
        self.age = 30  # better is to use parameter to be customized by user


jose = Astronaut(name='José Jiménez')
jose.agency
# NASA

ivan = Astronaut(name='Иван Иванович', agency='Roscosmos')
ivan.agency
# Roscosmos