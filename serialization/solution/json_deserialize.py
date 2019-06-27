import json
from pprint import pprint

FILE = r'../data/iris.json'
out = list()


with open(FILE) as file:
    DATA = json.load(file)


header, *data = DATA
out.append(tuple(header))

for row in DATA:
    measurements = row.values()
    out.append(tuple(measurements))

pprint(out)
