import sys


def function_filter(selected_species):
    output = []

    with open(r'iris.csv') as file:
        for line in file:
            *measurements, species = line.strip().split(',')
            if species == selected_species:
                output.append(measurements)

    return output


def generator_filter(selected_species):
    with open(r'iris.csv') as file:
        for line in file:
            *measurements, species = line.strip().split(',')
            if species == selected_species:
                yield measurements


if __name__ == '__main__':
    fun = function_filter('setosa')
    gen = generator_filter('setosa')

    print(sys.getsizeof(fun))
    print(sys.getsizeof(gen))
