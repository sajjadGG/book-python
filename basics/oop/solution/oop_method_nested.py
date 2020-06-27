class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):

        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_numeric_values(self):
        return [v for k,v in self.__dict__.items() if isinstance(v, float)]

    def total(self):
        return sum(self.get_numeric_values())

    def length(self):
        return len(self.get_numeric_values())

    def mean(self):
        return self.total() / self.length()

    def show(self):
        return f'total={self.total():.2f} mean={self.mean():.2f} {self.species}'


setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

print(f'{setosa.show()}')
print(f'{virginica.show()}')

# total=10.20 mean=2.55 setosa
# total=15.50 mean=3.88 virginica
