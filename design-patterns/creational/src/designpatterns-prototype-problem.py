from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self) -> None: ...


class Circle(Component):
    radius: int

    def set_radius(self, value: int) -> None:
        self.radius = value

    def get_radius(self) -> int:
        return self.radius

    def render(self) -> None:
        print('Rendering circle')


class ContextMenu:
    def duplicate(self, component: Component) -> None:
        if isinstance(component, Circle):
            source = component
            target = Circle()
            target.set_radius(source.get_radius())
