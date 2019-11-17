class GeographicCoordinate:
    class GEOProperty:
        def __init__(self, initial_value=None):
            self.value = initial_value

        def __get__(self, parent, parent_type):
            return self.value

        def __set__(self, parent, value):
            if self.MIN <= value <= self.MAX:
                self.value = value

        def __delete__(self, parent):
            self.value = None

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
            if hasattr(self, 'value'):
                raise PermissionError('Changing value is prohibited.')
            else:
                object.__set__('value', value)

    def __init__(self, latitude, longitude, elevation):
        self.latitude = GeographicCoordinate.Latitude(latitude)
        self.longitude = GeographicCoordinate.Longitude(longitude)
        self.elevation = GeographicCoordinate.Elevation(elevation)


geo1 = GeographicCoordinate(50, 120, 8000)
geo2 = GeographicCoordinate()

geo1.elevation = 100
geo2.elevation = 200

print(geo1.elevation)
print(geo2.elevation)
