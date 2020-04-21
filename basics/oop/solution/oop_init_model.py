class Astronaut:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class SpaceAgency:
    def __init__(self, short_name, long_name, location):
        self.short_name = short_name
        self.long_name = long_name
        self.location = location


twardowski = Astronaut('Jan', 'Twardowski', '1961-04-12')
watney = Astronaut('Mark', 'Watney', '1969-07-21')

esa = SpaceAgency(
    short_name='ESA',
    long_name='European Space Agency',
    location='Europe')

nasa = SpaceAgency(
    short_name='NASA',
    long_name='National Aeronautics and Space Administration',
    location='USA')

polsa = SpaceAgency(
    short_name='POLSA',
    long_name='Polish Space Agency',
    location='Poland')

print(twardowski.__dict__)
print(watney.__dict__)
print(esa.__dict__)
print(nasa.__dict__)
print(polsa.__dict__)

