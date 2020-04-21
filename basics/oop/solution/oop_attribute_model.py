class Astronaut:
    pass


class SpaceAgency:
    pass


twardowski = Astronaut()
twardowski.first_name = 'Jan'
twardowski.last_name = 'Twardowski'
twardowski.date_of_birth = '1961-04-12'

watney = Astronaut()
watney.first_name = 'Mark'
watney.last_name = 'Watney'
watney.date_of_birth = '1969-07-21'

esa = SpaceAgency()
esa.short_name = 'ESA'
esa.long_name = 'European Space Agency'
esa.location = 'Europe'

nasa = SpaceAgency()
nasa.short_name = 'NASA'
nasa.long_name = 'National Aeronautics and Space Administration'
nasa.location = 'USA'

polsa = SpaceAgency()
polsa.short_name = 'POLSA'
polsa.long_name = 'Polish Space Agency'
polsa.location = 'Poland'
