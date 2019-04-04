def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


with open(r'../data/iris.csv') as file:
    header, *data = file.readlines()

    for line in data:
        *features, labels = line.strip().split(',')
        labels = {'species': labels}

        print_iris(*features, **labels)
