from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


class Component(metaclass=ABCMeta):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass


class Shape(Component):
    def move(self) -> None:
        print('Move Shape')

    def render(self) -> None:
        print('Render Shape')


@dataclass
class Group(Component):
    __components: list[Component] = field(default_factory=list)

    def add(self, component: Component) -> None:
        self.__components.append(component)

    def render(self) -> None:
        for component in self.__components:
            component.render()

    def move(self) -> None:
        for component in self.__components:
            component.move()


if __name__ == '__main__':
    group1 = Group()
    group1.add(Shape())  # square
    group1.add(Shape())  # square

    group2 = Group()
    group2.add(Shape())  # circle
    group2.add(Shape())  # circle

    group = Group()
    group.add(group1)
    group.add(group2)
    group.render()
    group.move()
