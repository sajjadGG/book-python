from typing import Dict


class GEOProperty:
    def __get__(self, parent, parent_type):
        return parent.values[self.__class__.__name__]

    def __set__(self, parent, value):
        if self.MIN <= value <= self.MAX:
            parent.values[self.__class__.__name__] = value

    def __delete__(self, parent):
        parent.values[self.__class__.__name__] = None

    def __str__(self):
        return f'{self}'


class Latitude(GEOProperty):
    MIN = -90
    MAX = 90


class Longitude(GEOProperty):
    MIN = -180
    MAX = 180


class Elevation(GEOProperty):
    MIN = -10994
    MAX = 8848

    def __set__(self, parent, value):
        if self.__class__.__name__ in parent.values:
            raise PermissionError('Changing value is prohibited.')
        else:
            super().__set__(parent, value)


class GeographicCoordinate:
    latitude: Latitude = Latitude()
    longitude: Longitude = Longitude()
    elevation: Elevation = Elevation()

    def __init__(self, latitude, longitude, elevation):
        self.values: Dict[float] = {}
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __str__(self):
        return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'


geo1 = GeographicCoordinate(50, 120, 8000)
print(f'GEO1: {geo1}')
# GEO1: Latitude: 50, Longitude: 120, Elevation: 8000

geo2 = GeographicCoordinate(22, 33, 44)
print(f'GEO2: {geo2}')
# GEO2: Latitude: 1, Longitude: 2, Elevation: 3

print('-' * 55)

geo1.latitude = 1
geo1.longitude = 11
print(f'GEO1: {geo1}')
print(f'GEO2: {geo2}')

print('-' * 55)

geo1.elevation = 999
# PermissionError: Changing value is prohibited.
