DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

result = {}

for color in DATA:
    if color not in result:
        result[color] = 1
    else:
        result[color] += 1

print(result)
# {'red': 3, 'green': 2, 'blue': 2}


## Alternative solution
DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']
result = []

for color in DATA:
    result[color] = DATA.get(color, 0) + 1

print(result)
# {'red': 3, 'green': 2, 'blue': 2}
