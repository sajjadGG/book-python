from random import seed, randint
from pprint import pprint


seed(0)
result = []
total = 0

SIZE_X = 16
SIZE_Y = 16


for x in range(SIZE_X):
    result.append([])

    for y in range(SIZE_Y):
        result[x].append(randint(0, 9))

        if 6 <= x < 10 and 6 <= y < 10:
            total += result[x][y]


pprint(result)
pprint(total)
