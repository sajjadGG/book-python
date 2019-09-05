class Property:
    def __get__(self, parent, parent_type):
        return self.value

    def __set__(self, parent, value):
        if self.MIN <= value <= self.MAX:
            self.value = value
        else:
            raise ValueError(f'Value must be between {self.MIN} and {self.MAX}')

    def __delete__(self):
        self.value = None


class Latitude(Property):
    MIN = -90.0
    MAX = 90.0


class Longitude(Property):
    MIN = -180.0
    MAX = 180.0


class Elevation(Property):
    MIN = -10994.0
    MAX = 8848.0

    def __set__(self, parent, value):
        if not hasattr(self, 'value'):
            super().__set__('value', value)
        else:
            raise PermissionError('Changing value is prohibited.')


class GeographicCoordinate:
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()


geo = GeographicCoordinate()

geo.latitude = 10.0
print(geo.latitude)

geo.longitude = -20.0
print(geo.longitude)

geo.elevation = 1000.0
print(geo.elevation)
