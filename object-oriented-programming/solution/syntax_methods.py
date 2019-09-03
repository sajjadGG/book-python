class Iris:
    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, species: str):
        self.sepal_length: float = float(sepal_length)
        self.sepal_width: float = float(sepal_width)
        self.petal_length: float = float(petal_length)
        self.petal_width: float = float(petal_width)
        self.species: str = str(species)

    def total(self) -> float:
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self) -> float:
        return self.total() / 4


setosa = Iris(5.4, 3.9, 1.3, 0.4, 'setosa')
print(f'{setosa.species}')
print(f'Total: {setosa.total():.2f}')
print(f'Average: {setosa.average():.2f}')

virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')
print(f'{virginica.species}')
print(f'Total: {virginica.total():.2f}')
print(f'Average: {virginica.average():.2f}')
