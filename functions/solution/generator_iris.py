import sys

FILE = r'iris.csv'


def function_filter(selected_species):
    output = []

    with open(FILE) as file:
        for line in file:
            line = line.strip().split(',')
            measurements = line[0:4]
            species = line[4]

            if species == selected_species:
                output.append(measurements)

    return output


def generator_filter(selected_species):
    with open(FILE) as file:
        for line in file:
            line = line.strip().split(',')
            measurements = line[0:4]
            species = line[4]

            if species == selected_species:
                yield measurements


if __name__ == '__main__':
    fun = function_filter('setosa')
    gen = generator_filter('setosa')

    print(sys.getsizeof(fun))
    print(sys.getsizeof(gen))

