FILE = r'../data/iris.csv'
output = []

with open(FILE) as file:
    *header, _ = file.readline().strip().split(',')

    for line in file:
        *measurements, _ = line.strip().split(',')
        measurements = map(float, measurements)
        pairs = zip(header, measurements)
        output.append(dict(pairs))


def mean(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


for row in output:
    avg = mean(**row)
    print(avg)


## Alternative
list(map(lambda row: mean(**row), output))
