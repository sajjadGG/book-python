def print_iris(species, **pomiary):
    print(locals())


with open(r'../data/iris.csv') as file:
    header = file.readline()
    *header, _ = header.split(',')

    for line in file.readlines():
        *features, label = line.strip().split(',')
        features = map(float, features)
        pomiary = zip(header, features)
        print_iris(label, **dict(pomiary))
