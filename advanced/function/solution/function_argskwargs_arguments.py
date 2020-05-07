FILE = r'../data/iris.csv'
result = []

with open(FILE) as file:
    *header, _ = file.readline().strip().split(',')
    # header = file.readline().strip().split(',')[0:4]

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(header, measurements)
        result.append(dict(pairs))


def mean(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


for row in result:
    avg = mean(**row)
    print(avg)


## Alternative
list(map(lambda row: mean(**row), result))
