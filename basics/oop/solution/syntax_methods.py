class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_length(self):
        return len(self.__dict__) - 1

    def total(self):
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self):
        return self.total() / self.get_length()


setosa = Iris(5.4, 3.9, 1.3, 0.4, 'setosa')
print(f'{setosa.species}')
print(f'Total: {setosa.total():.2f}')
print(f'Average: {setosa.average():.2f}')

virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
print(f'{virginica.species}')
print(f'Total: {virginica.total():.2f}')
print(f'Average: {virginica.average():.2f}')
