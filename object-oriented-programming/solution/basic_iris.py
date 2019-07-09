class Iris:
    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, species: str):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)
        self.species = str(species)

    def total(self):
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self):
        return self.total() / 4


flower = Iris(5.4, 3.9, 1.3, 0.4, 'setosa')
print(f'Total: {flower.total():.2f}')
print(f'Average: {flower.average():.2f}')
