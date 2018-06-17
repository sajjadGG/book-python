class Astronaut:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')
print(ivan.first_name)
# Иван
