class Crew:
    def __init__(self):
        self.mission = 'Ares 3'


class Astronaut(Crew):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name} ({self.mission})'


mark = Astronaut('Mark Watney')
melissa = Astronaut('Melissa Lewis')
alex = Astronaut('Alex Vogel')

result = f"""
Astronaut crew:
- {mark}
- {melissa}
- {alex}
"""

print(result)
# Watney family:
# - Mark Watney
# - Melissa Watney
# - Alex Watney
