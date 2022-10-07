from dataclasses import dataclass, field
from enum import Enum
from typing import Final


class PointType(Enum):
    HOSPITAL = 1
    CAFE = 2
    RESTAURANT = 3


@dataclass
class PointIcon:
    type: Final[PointType]   # 1064 bytes
    icon: Final[bytearray]   # empty: 56 bytes, but with PNG icon: 20 KB

    def get_type(self):
        return self.type


@dataclass
class PointIconFactory:
    icons: dict[PointType, PointIcon] = field(default_factory=dict)

    def get_point_icon(self, type: PointType) -> PointIcon:
        if not self.icons.get(type):
            self.icons[type] = PointIcon(type, None)  # Here read icon from filesystem
        return self.icons.get(type)


@dataclass
class Point:
    x: int  # 28 bytes
    y: int  # 28 bytes
    icon: PointIcon

    def draw(self) -> None:
        print(f'{self.icon.get_type()} at ({self.x}, {self.y})')


@dataclass
class PointService:
    icon_factory: PointIconFactory

    def get_points(self) -> list[Point]:
        points: list[Point] = list()
        point: Point = Point(1, 2, self.icon_factory.get_point_icon(PointType.CAFE))
        points.append(point)
        return points


if __name__ == '__main__':
    service = PointService(PointIconFactory())
    for point in service.get_points():
        point.draw()
        # PointType.CAFE at (1, 2)
