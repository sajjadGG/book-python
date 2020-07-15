class Crew:
    def __init__(self, members=()):
        self.members = members

class Address:
    def __init__(self, location, city):
        self.location = location
        self.city = city

class Astronaut:
    def __init__(self, firstname, lastname, addresses=()):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses = addresses


crew = Crew([
    Astronaut(firstname='Jan', lastname='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Astronaut(firstname='Mark', lastname='Watney'),
    Astronaut(firstname='Melissa', lastname='Lewis', addresses=()),
])
