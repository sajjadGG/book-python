from dataclasses import dataclass


# class Point:
#     def __init__(self, x: int, y: int) -> None:
#         self.x: int = x
#         self.y: int = y
#
#     def __setattr__(self, attribute_name, new_value):
#         if hasattr(self, attribute_name):
#             raise PermissionError
#         elif attribute_name not in ('x', 'y'):
#             raise PermissionError
#         else:
#             object.__setattr__(self, attribute_name, new_value)


@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass
class Moveable:
    position: Point

    def get_position(self) -> Point:
        return self.position

    def print_position(self) -> None:
        print(self.position)

    def change_position(self, position: Point) -> None:
        return self.set_position(position)

    def change_coordinates(self, x: int, y: int) -> None:
        return self.set_position(Point(x, y))

    def set_position(self, position: Point):
        self.position = position

    def set_coordinates(self, x, y):
        self.position = Point(x, y)


p = Point(1,2)
print(p.x)
p.x = 3
