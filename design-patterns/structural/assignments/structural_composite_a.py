from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass


class Ellipse(Shape):
    def print(self):
        print('Ellipse')


class Circle(Shape):
    def print(self):
        print('Circle')


@dataclass
class Group(Shape):
    __children: list = field(default_factory=list)

    def add(self, graphic):
        self.__children.append(graphic)

    def print(self):
        for children in self.__children:
            children.print()


if __name__ == '__main__':
    group1 = Group()
    group1.add(Ellipse())

    group2 = Group()
    group2.add(Circle())
    group2.add(group1)
    group2.print()
