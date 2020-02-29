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
output = list()

for row in DATA:
    header.update(row.keys())


output.append(header)

for row in DATA:
    output.append(tuple(
        row.get(head, None)
            for head in header
    ))

print(output)
