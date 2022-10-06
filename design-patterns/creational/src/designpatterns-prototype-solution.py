from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self) -> None: ...

    @abstractmethod
    def clone(self) -> Component: ...


class Circle(Component):
    radius: int

    def set_radius(self, value: int) -> None:
        self.radius = value

    def get_radius(self) -> int:
        return self.radius

    def clone(self) -> Component:
        new_circle = Circle()
        new_circle.set_radius(self.radius)
        return new_circle

    def render(self) -> None:
        print('Rendering circle')


class ContextMenu:
    def duplicate(self, component: Component) -> None:
        new_component = component.clone()
