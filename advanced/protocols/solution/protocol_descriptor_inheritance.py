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
    """
    >>> place1 = GeographicCoordinate(50, 120, 8000)
    >>> str(place1)
    'Latitude: 50, Longitude: 120, Elevation: 8000'

    >>> place2 = GeographicCoordinate(22, 33, 44)
    >>> str(place2)
    'Latitude: 22, Longitude: 33, Elevation: 44'

    >>> place1.latitude = 1
    >>> place1.longitude = 11
    >>> str(place1)
    'Latitude: 1, Longitude: 11, Elevation: 8000'

    >>> str(place2)
    'Latitude: 22, Longitude: 33, Elevation: 44'

    >>> place1.elevation = 999
    Traceback (most recent call last):
      ...
    PermissionError: Changing value is prohibited.
    """

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
