class Astronaut:
    pass


class SpaceAgency:
    pass


watney = Astronaut()
watney.name = 'Mark Watney'
watney.location = 'USA'
watney.date_of_birth = '1969-07-21'

twardowski = Astronaut()
twardowski.name = 'Jan Twardowski'
twardowski.location = 'Poland'
twardowski.date_of_birth = '1961-04-12'

nasa = SpaceAgency()
nasa.name = 'National Aeronautics and Space Administration'
nasa.location = 'USA'
nasa.formation = '1958-07-29'

polsa = SpaceAgency()
polsa.name = 'Polish Space Agency'
polsa.location = 'Poland'
polsa.formation = '2014-09-26'


print(twardowski.__dict__)
print(watney.__dict__)
print(nasa.__dict__)
print(polsa.__dict__)
