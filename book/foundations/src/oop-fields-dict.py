class Astronaut:
    def __init__(self, name, agency='NASA'):
        self.name = name
        self.agency = agency


jose = Astronaut(name='José Jiménez')
print(jose.agency.__dict__)
# {'name': 'José Jiménez', 'agency': 'NASA'}

ivan = Astronaut(name='Иван Иванович', agency='Roscosmos')
print(ivan.agency.__dict__)
# {'name': 'Иван Иванович', 'agency': 'Roscosmos'}