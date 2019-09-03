class Astronaut:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.date_of_birth: str = date_of_birth


class Location:
    def __init__(self, name, city, state):
        self.name: str = name
        self.city: str = city
        self.state: str = state


twardowski = Astronaut('Jan', 'Twardowski', '1961-04-12')
watney = Astronaut('Mark', 'Watney', '1969-07-21')

ksc = Location('Kennedy Space Center', 'Merritt Island', 'Florida')
jsc = Location('Johnson Space Center', 'Houston', 'Texas')
jpl = Location('Jet Propulsion Laboratory', 'Pasadena', 'Texas')
