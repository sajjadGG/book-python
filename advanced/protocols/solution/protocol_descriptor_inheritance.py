class GEOProperty:
    MIN = None
    MAX = None

    @property
    def attrname(self):
        return '_' + self.__class__.__name__.lower()

    def __set__(self, parent, value):
        if self.MIN <= value <= self.MAX:
            setattr(parent, self.attrname, value)
        else:
            raise ValueError('Out of bounds')

    def __get__(self, parent, parent_type):
        return getattr(parent, self.attrname)

    def __delete__(self, parent):
        delattr(parent, self.attrname)


class Latitude(GEOProperty):
    MIN = -90
    MAX = +90


class Longitude(GEOProperty):
    MIN = -180
    MAX = +180


class Elevation(GEOProperty):
    MIN = -10994
    MAX = +8848

    def __set__(self, parent, value):
        if hasattr(parent, self.attrname):
            raise PermissionError('Changing value is prohibited.')

        super().__set__(parent, value)


class GeographicCoordinate:
    """
    >>> GeographicCoordinate(-91, 0, 0)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

    >>> GeographicCoordinate(+91, 0, 0)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, -181, 0)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, +181, 0)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, -10995)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, +8849)
    Traceback (most recent call last):
      ...
    ValueError: Out of bounds

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
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()

    def __init__(self, latitude, longitude, elevation):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __str__(self):
        return f'Latitude: {self.latitude}, Longitude: {self.longitude}, Elevation: {self.elevation}'


# from dataclasses import dataclass
#
#
# @dataclass
# class Location:
#     latitude = Latitude()
#     longitude = Longitude()
#     elevation = Elevation()
