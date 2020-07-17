class Point:
    position = property()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @position.getter
    def position(self):
        return (self._x, self._y, self._z)

    @position.setter
    def position(self, new_value):
        raise PermissionError('Cannot modify values')

    @position.deleter
    def position(self):
        self._x = 0
        self._y = 0
        self._z = 0


my = Point(x=1, y=2, z=3)

print(my.position)
# (1, 2, 3)

del my.position
print(my.position)
# (0, 0, 0)

my.position = (4, 5, 6)
# PermissionError: Cannot modify values
