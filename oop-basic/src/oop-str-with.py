class Astronaut:
    name = 'José Jiménez'

    def __str__(self):
        return f'My name {self.name}'


jose = Astronaut()
print(jose)
# My name José Jiménez
