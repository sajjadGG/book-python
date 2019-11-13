import json
from pprint import pprint

FILE = r'../data/iris.json'
output = list()


with open(FILE) as file:
    DATA = json.load(file)


header = tuple(DATA[0].keys())
output.append(header)

for row in DATA:
    measurements = row.values()
    output.append(tuple(measurements))

pprint(output)
