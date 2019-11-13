FILE = r'../data/iris.csv'

OUTPUT = []

with open(FILE) as file:
    header = file.readline()
    *column_names, _ = header.strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(column_names, measurements)
        OUTPUT.append(dict(pairs))


def mean(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


for row in OUTPUT:
    avg = mean(**row)
    print(avg)
