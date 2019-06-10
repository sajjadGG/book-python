def print_iris(species, **pomiary):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()
    *header, _ = header.split(',')

    for line in data:
        *features, label = line.strip().split(',')
        features = map(float, features)
        pomiary = zip(header, features)
        print_iris(label, **dict(pomiary))
