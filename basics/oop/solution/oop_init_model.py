class Astronaut:
    def __init__(self, firstname, lastname, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth


class SpaceAgency:
    def __init__(self, name, location, formation):
        self.name = name
        self.location = location
        self.formation = formation


twardowski = Astronaut('Jan', 'Twardowski', '1961-04-12')
watney = Astronaut('Mark', 'Watney', '1969-07-21')

esa = SpaceAgency(
    name='European Space Agency',
    location='Europe',
    formation='1975-05-30')

nasa = SpaceAgency(
     name='National Aeronautics and Space Administration',
    location='USA',
    formation='1958-07-29')

polsa = SpaceAgency(
    name='Polish Space Agency',
    location='Poland',
    formation='2014-09-26')


print(twardowski.__dict__)
print(watney.__dict__)
print(esa.__dict__)
print(nasa.__dict__)
print(polsa.__dict__)

