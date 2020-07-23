from abc import ABC, abstractmethod


class Iris(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(Iris):
    def get_name(self):
        pass


# iris = Iris()
# TypeError: Can't instantiate abstract class Iris with abstract methods get_name

# setosa = Setosa()
# TypeError: Can't instantiate abstract class Setosa with abstract methods get_name

setosa = Setosa()
print('ok')
