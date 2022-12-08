class Point:
    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'

    def get_coordinates(self) -> tuple[int,int]:
        return self.x, self.y

    def set_coordinates(self, x: int = None, y: int = None) -> None:
        if x is None or y is None:
            raise TypeError
        self.x = x
        self.y = y


## Tests
from unittest import TestCase


class PointInitTest(TestCase):

    def test_init_noargs(self):
        pt = Point()
        self.assertIsInstance(pt, Point)

    def tet_init_default(self):
        pt = Point()
        self.assertEqual(pt.x, 0)
        self.assertEqual(pt.y, 0)

    def test_init_args(self):
        pt = Point(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)

    def test_init_kwargs(self):
        pt = Point(x=1, y=2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)


class PointOtherTest(TestCase):

    def setUp(self) -> None:
        self.pt = Point(x=1, y=2)

    def test_str(self):
        self.assertEqual(str(self.pt), '(1, 2)')

    def test_repr(self):
        self.assertEqual(repr(self.pt), 'Point(x=1, y=2)')

    def test_get_coordinates(self):
        self.assertEqual(self.pt.get_coordinates(), (1, 2))

    def test_set_coordinates_args(self):
        with self.assertRaises(TypeError):
            self.pt.set_coordinates()

    def test_set_coordinates_kwargs(self):
        self.pt.set_coordinates(x=10, y=20)
        self.assertEqual(self.pt.x, 10)
        self.assertEqual(self.pt.y, 20)
