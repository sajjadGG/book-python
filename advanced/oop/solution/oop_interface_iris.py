class IrisInterface:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def sum(self):
        raise NotImplementedError

    def len(self):
        raise NotImplementedError

    def avg(self):
        raise NotImplementedError


class Setosa(IrisInterface):
    def sum(self):
        return sum(self.__dict__.values())

    def len(self):
        return len(self.__dict__.values())

    def avg(self):
        return self.sum() / self.len()


iris = IrisInterface(5.8, 2.7, 5.1, 1.9)
setosa = Setosa(5.1, 3.5, 1.4, 0.2)

print('Setosa', setosa.avg())
print('Iris', iris.avg())
