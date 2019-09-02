# https://raw.githubusercontent.com/AstroMatt/book-python/master/functions/data/iris-clean.csv


def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


with open(r'../data/iris-clean.csv') as file:

    # skip first line in file
    file.readline()

    for line in file:
        *features, labels = line.strip().split(',')

        d = {'species': labels}
        print_iris(*features, **d)
