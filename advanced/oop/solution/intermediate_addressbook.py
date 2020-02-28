class Crew:
    def __init__(self, members=()):
        self.members = members

class Address:
    def __init__(self, location, city):
        self.location = location
        self.city = city

class Astronaut:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses


crew = Crew([
    Astronaut(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Astronaut(first_name='Mark', last_name='Watney'),
    Astronaut(first_name='Melissa', last_name='Lewis', addresses=()),
])
