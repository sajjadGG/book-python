def print_iris(species, **pomiary):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()
    parameter_names = header.split(',')[:-1]

    for line in data:
        *measurements, species = line.strip().split(',')
        pomiary = {}

        for i, _ in parameter_names:
            key = parameter_names[i]
            value = float(measurements[i])
            pomiary[key] = value

        print_iris(species, **pomiary)
