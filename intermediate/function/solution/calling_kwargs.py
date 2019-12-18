FILE = r'../data/iris.csv'
OUTPUT = []

with open(FILE) as file:
    *header, _ = file.readline().strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(header, measurements)
        OUTPUT.append(dict(pairs))


def mean(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


for row in OUTPUT:
    avg = mean(**row)
    print(avg)


## Alternative
list(map(lambda row: mean(**row), OUTPUT))
