def increment_population():
    Astronaut.population += 1


class Astronaut:
    population = 0

    def __init__(self, name):
        self.name = name
        increment_population()


jose = Astronaut('José Jiménez')
ivan = Astronaut('Иван Иванович')
print(Astronaut.population)  # 2

# ----------------

class Astronaut:
    population = 0

    def __init__(self, name):
        self.name = name
        Astronaut.increment_population()

    @staticmethod
    def increment_population():
        Astronaut.population += 1


jose = Astronaut('José Jiménez')
ivan = Astronaut('Иван Иванович')
print(Astronaut.population)  # 2