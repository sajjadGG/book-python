INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
         0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
         1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
         4, 8, 1, 9, 6, 3]

OUTPUT = {}

for digit in INPUT:

    if digit not in OUTPUT:
        OUTPUT[digit] = 1
    else:
        OUTPUT[digit] += 1

print(OUTPUT)
