from random import seed, randint
from pprint import pprint


seed(0)
result = []
total = 0


X_MAX = 16
Y_MAX = 16
X_INNER = 4
Y_INNER = 4


x_offset = (X_MAX - X_INNER) / 2
y_offset = (Y_MAX - Y_INNER) / 2


for x in range(X_MAX):
    result.append([])

    for y in range(Y_MAX):
        result[x].append(randint(0, 9))

        x_offset_left = x_offset
        x_offset_right = X_MAX - x_offset

        y_offset_left = y_offset
        y_offset_right = Y_MAX - y_offset

        if x_offset_left <= x < x_offset_right and y_offset_left <= y < y_offset_right:
            total += result[x][y]


pprint(result)
pprint(total)
