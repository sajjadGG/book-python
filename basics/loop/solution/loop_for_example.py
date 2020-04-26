DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

output = {}

for color in DATA:
    if color not in output:
        output[color] = 1
    else:
        output[color] += 1

print(output)
# {'red': 3, 'green': 2, 'blue': 2}


## Alternative solution
DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']
output = []

for color in DATA:
    output[color] = DATA.get(color, 0) + 1

print(output)
# {'red': 3, 'green': 2, 'blue': 2}
