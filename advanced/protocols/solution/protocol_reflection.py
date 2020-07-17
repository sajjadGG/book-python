class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError

        if hasattr(self, name):
            raise PermissionError

        return super().__setattr__(name, value)

    def __str__(self):
        return str((self.x, self.y, self.z))


pt = Point(1, 2, 3)

print(pt)

# pt.a = 0
# PermissionError

# pt.x = 0
# PermissionError

del pt.x
# PermissionError
