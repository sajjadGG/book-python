class AddressBook:
    def __init__(self, contacts=()):
        self.contacts = contacts


class Address:
    def __init__(self, location, city):
        self.location = location
        self.city = city


class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.address = addresses


INPUT = AddressBook([
    Contact(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Contact(first_name='Mark', last_name='Watney'),
    Contact(first_name='Melissa', last_name='Lewis', addresses=()),
])
