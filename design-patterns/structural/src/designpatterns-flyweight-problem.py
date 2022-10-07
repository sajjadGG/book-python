from dataclasses import dataclass
from enum import Enum


class PointType(Enum):
    HOSPITAL = 1
    CAFE = 2
    RESTAURANT = 3


@dataclass
class Point:
    x: int            # 28 bytes
    y: int            # 28 bytes
    type: PointType   # 1064 bytes
    icon: bytearray   # empty: 56 bytes, but with PNG icon: 20 KB

    def draw(self) -> None:
        print(f'{self.type} at ({self.x}, {self.y})')


class PointService:
    def get_points(self) -> list[Point]:
        points: list[Point] = list()
        point: Point = Point(1, 2, PointType.CAFE, None)
        points.append(point)
        return points


if __name__ == '__main__':
    service = PointService()
    for point in service.get_points():
        point.draw()
        # PointType.CAFE at (1, 2)
