def print_iris(species, **pomiary):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()
    *columns, _ = header.split(',')

    for line in data:
        *measurements, species = line.strip().split(',')
        pomiary = {}

        for i, _ in enumerate(columns):
            key = columns[i]
            value = float(measurements[i])
            pomiary[key] = value

        print_iris(species, **pomiary)
