from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = '#00FF00'
    BLUE = 'blue'


print(Color.RED)
# Color.RED

print(Color.RED.name)
# RED

print(Color.RED.value)
# 1

for color in Color:
    print(color)

# Color.RED
# Color.GREEN
# Color.BLUE

Color(1)
# <Color.RED: 1>

Color.RED is Color.RED
# True
