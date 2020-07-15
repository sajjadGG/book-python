import sys

FILE = r'../data/iris.csv'


def function(species):
    result = []
    with open(FILE) as file:
        header = file.readline()

        for line in file:
            *features, label = line.strip().split(',')
            if label == species:
                result.append(features)
        return result


def generator(species):
    with open(FILE) as file:
        header = file.readline()

        for line in file:
            *features, label = line.strip().split(',')
            if label == species:
                yield features


fun = function('setosa')
gen = generator('setosa')

print('Function', sys.getsizeof(fun))
# Function 520

print('Generator', sys.getsizeof(gen))
# Generator 112
