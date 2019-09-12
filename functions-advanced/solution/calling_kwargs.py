FILE = r'../data/iris-clean.csv'


def average(**kwargs):
    values = kwargs.values()
    return sum(values) / len(values)


data = []

with open(FILE) as file:
    header, *records = file.readlines()
    *columns, _ = header.split(',')

    for line in records:
        *measurements, _ = line.strip().split(',')

        tmp = {}

        for i, name in enumerate(columns):
            tmp[name] = float(measurements[i])

        data.append(tmp)


for row in data:
    print(average(**row))

print(data)
