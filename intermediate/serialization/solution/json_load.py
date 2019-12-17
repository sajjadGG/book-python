import json
from pprint import pprint

FILE = r'../data/iris.json'
output = list()


with open(FILE) as file:
    DATA = json.load(file)


## Naive Solution
header = tuple(DATA[0].keys())
output.append(header)

for row in DATA:
    measurements = row.values()
    output.append(tuple(measurements))

pprint(output)


## Proper solution
header = set()
OUTPUT = list()

for row in DATA:
    header.update(row.keys())


OUTPUT.append(header)

for row in DATA:
    OUTPUT.append(tuple(
        row.get(head, None)
            for head in header
    ))

print(OUTPUT)
