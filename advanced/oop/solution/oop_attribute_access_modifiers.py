class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, setosa):
        self._sepal_length = sepal_length
        self._sepal_width = sepal_width
        self._petal_length = petal_length
        self._petal_width = petal_width
        self.setosa = setosa


class Virginica(Iris):
    pass


class Setosa(Iris):
    pass


class Versicolor(Iris):
    pass


result = [
    Virginica(5.8, 2.7, 5.1, 1.9, 'virginica'),
    Setosa(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Versicolor(5.7, 2.8, 4.1, 1.3, 'versicolor'),
]

for iris in result:
    public_atrrs = {k:v for k,v in iris.__dict__.items() if not k.startswith('_')}
    print(public_atrrs)
