import sys
from dataclasses import dataclass

CURRENT_MODULE = sys.modules[__name__]

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


@dataclass
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __post_init__(self):
        self.species = self.__class__.__name__

    def total(self):
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self):
        return self.total() / 4


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


class Setosa(Iris):
    pass


header, *data = DATA
output = []

print('Species    Total   Avg')
print('-' * 22)


for *measurements, species in data:
    class_name = species.capitalize()
    cls = getattr(CURRENT_MODULE, class_name)
    iris = cls(*measurements)
    output.append(iris)

    ## Alternative solution
    # if species == 'setosa':
    #     iris = Setosa(*measurements)
    # elif species == 'versicolor':
    #     iris = Versicolor(*measurements)
    # elif species == 'virginica':
    #     iris = Virginica(*measurements)
    # output.append(iris)

    print(f'{iris.species:>10} {iris.total():>5.1f} {iris.average():>5.2f}')
