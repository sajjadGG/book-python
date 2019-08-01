import json
from pprint import pprint

FILE = r'../data/iris.json'
out = list()


with open(FILE) as file:
    DATA = json.load(file)


header = tuple(DATA[0].keys())
out.append(header)

for row in DATA:
    measurements = row.values()
    out.append(tuple(measurements))

pprint(out)
