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
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = self.__class__.__name__

    def total(self):
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self):
        return self.total() / 4


class Virginica(Iris):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Versicolor(Iris):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Setosa(Iris):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


header, *data = DATA
out = []

for *measurements, species in data:
    if species == 'setosa':
        obj = Setosa(*measurements)
        out.append(obj)
    elif species == 'versicolor':
        obj = Versicolor(*measurements)
        out.append(obj)
    elif species == 'virginica':
        obj = Virginica(*measurements)
        out.append(obj)


print('Species    Total   Avg')
print('-' * 22)

for iris in out:
    name = iris.species
    total = iris.total()
    avg = iris.average()

    print(f'{name:>10} {total:>5.1f} {avg:>5.2f}')
