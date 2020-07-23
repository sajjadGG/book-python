class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        raise NotImplementedError

    def avg(self):
        raise NotImplementedError

    def sum(self):
        raise NotImplementedError

    def len(self):
        raise NotImplementedError


class Setosa(IrisInterface):
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def len(self):
        return len(self.__dict__)

    def sum(self):
        return sum(self.__dict__.values())

    def avg(self):
        return self.sum() / self.len()


setosa = Setosa(5.1, 3.5, 1.4, 0.2)
print('Setosa', setosa.avg())

iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
# NotImplementedError
