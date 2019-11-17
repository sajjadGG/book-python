class Point:
    def __init__(self, x, y, z):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)
        object.__setattr__(self, 'z', z)

    def __delattr__(self, item):
        raise PermissionError

    def __setattr__(self, key, value):
        raise PermissionError

p = Point(x=1, y=2, z=3)

print(p.x)
print(p.y)
print(p.z)

# del p.x


## Alternative

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __delattr__(self, item):
        raise PermissionError

    def __setattr__(self, key, value):
        if not hasattr(self, key) and key in {'x', 'y', 'z'}:
            object.__setattr__(self, key, value)
        else:
            raise PermissionError

p = Point(x=1, y=2, z=3)

print(p.x)
print(p.y)
print(p.z)

# del p.x
