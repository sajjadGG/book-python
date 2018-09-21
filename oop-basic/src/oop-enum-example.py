from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = '#00FF00'
    BLUE = 'blue'


class Moon:
    def __init__(self, first_explorer):
        if first_explorer == 'NASA':
            self.color = Color.BLUE
        elif first_explorer == 'Roscosmos':
            self.color = Color.RED


moon = Moon(first_explorer='NASA')


if moon.color is Color.RED:
    print(True)
else:
    print(False)
