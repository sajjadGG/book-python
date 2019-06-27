from statistics import mean, median, stdev, variance
from pprint import pprint


DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]


header, *data = DATA

output = dict()

for sepal_length, sepal_width, petal_length, petal_width, species in data:
    if species not in output:
        output[species] = {
            'sepal_length': {'values': []},
            'sepal_width': {'values': []},
            'petal_length': {'values': []},
            'petal_width': {'values': []},
        }

    output[species]['sepal_length']['values'].append(sepal_length)
    output[species]['sepal_width']['values'].append(sepal_width)
    output[species]['petal_length']['values'].append(petal_length)
    output[species]['petal_width']['values'].append(petal_width)


def compute(species, parameter):
    values = output[species][parameter]['values']
    output[species][parameter]['mean'] = mean(values)
    output[species][parameter]['median'] = median(values)
    output[species][parameter]['stdev'] = stdev(values)
    output[species][parameter]['variance'] = variance(values)


for species in output:
    compute(species, 'sepal_length')
    compute(species, 'sepal_width')
    compute(species, 'petal_length')
    compute(species, 'petal_width')


pprint(output)
