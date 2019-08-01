def print_iris(species, **pomiary):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()
    *columns, _ = header.split(',')

    for line in data:
        *measurements, species = line.strip().split(',')
        values = {}

        for i, name in enumerate(columns):
            values[name] = float(measurements[i])

        print_iris(species, **values)
