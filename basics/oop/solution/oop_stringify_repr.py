DATA = [
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
]


class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __repr__(self):
        return f'Iris({features=}, {label=})'


for *features, label in DATA:
    iris = Iris(features, label)
    print(repr(iris))
