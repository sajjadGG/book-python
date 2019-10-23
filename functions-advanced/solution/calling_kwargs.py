FILE = r'../data/iris.csv'

data = []

with open(FILE) as file:
    header = file.readline()
    *column_names, _ = header.strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(column_names, measurements)
        data.append(dict(pairs))


def mean(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


for row in data:
    avg = mean(**row)
    print(avg)
