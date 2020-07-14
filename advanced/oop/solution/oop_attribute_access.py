import sys

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


class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def __repr__(self):
        name = self.__class__.__name__
        total = self.sum()
        avg = self.mean()
        return f'\n{name:>10} {total:>5.1f} {avg:>5.2f}'

    def length(self):
        return len(self.__dict__.values())

    def sum(self):
        return sum(self.__dict__.values())

    def mean(self):
        return self.sum() / self.length()


class Setosa(Iris):
    pass

class Versicolor(Iris):
    pass

class Virginica(Iris):
    pass


CURRENT_MODULE = sys.modules[__name__]

header, *data = DATA
*header, _ = tuple(x.replace(' ', '_').lower() for x in header)
result = []

result = [cls(**row)
          for *features, species in data
          if (cls := getattr(CURRENT_MODULE, species.capitalize()))
          and (row := dict(zip(header, features)))]


print('Species    Total   Avg')
print('-' * 22)
print(result)


# for *features, species in data:
#     row = dict(zip(header, features))
#     species = species.capitalize()
#     current_module = sys.modules[__name__]
#     cls = getattr(current_module, species)
#     result.append(cls(**row))
#
# print(result)
