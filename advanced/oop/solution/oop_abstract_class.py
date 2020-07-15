from abc import ABC, abstractmethod


class Iris(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Setosa(Iris):
    def get_name(self):
        print('Setosa')


setosa = Setosa()
# iris = Iris()
