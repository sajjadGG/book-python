from random import sample

output = sample(range(1, 49), 6)
print(output)


# Alternative solution
from random import randint

MAX_VALUE = 49
MIN_VALUE = 1
REPETITIONS = 6

output = set()

while len(output) < REPETITIONS:
    number = randint(MIN_VALUE, MAX_VALUE)
    output.add(number)

print(sorted(output))

