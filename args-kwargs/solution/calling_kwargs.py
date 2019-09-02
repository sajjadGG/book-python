def print_iris(species, **measurements):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()
    *columns, _ = header.split(',')

    for line in data:
        *measurements, species = line.strip().split(',')
        data = {}

        for i, name in enumerate(columns):
            data[name] = float(measurements[i])

        print_iris(species, **data)
