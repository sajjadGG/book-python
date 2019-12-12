class Astronaut:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.date_of_birth: str = date_of_birth


class SpaceAgency:
    def __init__(self, short_name, long_name, location):
        self.short_name: str = short_name
        self.long_name: str = long_name
        self.location: str = location


twardowski = Astronaut('Jan', 'Twardowski', '1961-04-12')
watney = Astronaut('Mark', 'Watney', '1969-07-21')

esa = SpaceAgency('ESA', 'European Space Agency', 'Europe')
nasa = SpaceAgency('NASA', 'National Aeronautics and Space Administration', 'USA')
polsa = SpaceAgency('POLSA', 'Polish Space Agency', 'Poland')
