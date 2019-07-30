import random


MAX_VALUE = 49
MIN_VALUE = 1
REPETITIONS = 6

output = []


while len(output) <= REPETITIONS:
    number = random.randrange(MIN_VALUE, MAX_VALUE)

    if number not in output:
        output.append(number)

print(sorted(output))


# Alternative solution
output = random.sample(
    population=range(MIN_VALUE, MAX_VALUE),
    k=REPETITIONS)

print(output)
