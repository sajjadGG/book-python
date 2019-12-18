import sys

FILE = r'../data/iris.csv'


def function_filter(selected_species):
    output = []
    with open(FILE) as file:
        for line in file:
            *measurements, species = line.strip().split(',')
            if species == selected_species:
                output.append(measurements)
    return output


def generator_filter(selected_species):
    with open(FILE) as file:
        for line in file:
            *measurements, species = line.strip().split(',')
            if species == selected_species:
                yield measurements


fun = function_filter('setosa')
gen = generator_filter('setosa')


print('Function', sys.getsizeof(fun))
# Function 536

print('Generator', sys.getsizeof(gen))
# Generator 128

