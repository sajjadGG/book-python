FILE = r'../data/iris-clean.csv'

data = []

with open(FILE) as file:
    header = file.readline()
    *features, _ = header.strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = [float(x) for x in measurements]
        row = dict(zip(features, measurements))
        data.append(row)


def average(**kwargs):
    val = kwargs.values()
    return sum(val) / len(val)


for row in data:
    avg = average(**row)
    print(avg)
