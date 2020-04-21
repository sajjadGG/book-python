import sys

FILE = r'../data/iris.csv'


def function_filter(file, selected_species):
    output = []
    for line in file:
        *measurements, species = line.strip().split(',')
        if species == selected_species:
            output.append(measurements)
    return output


def generator_filter(file, selected_species):
    for line in file:
        *measurements, species = line.strip().split(',')
        if species == selected_species:
            yield measurements


with open(FILE) as file:
    data = file.read()

fun = function_filter(data, 'setosa')
gen = generator_filter(data, 'setosa')


print('Function', sys.getsizeof(fun))
# Function 56

print('Generator', sys.getsizeof(gen))
# Generator 112
