class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses


class Address:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


addressbook = Contact(first_name='Jan', last_name='Twardowski', addresses=(
    Address(center='Johnson Space Center', location='Houston, TX'),
    Address(center='Kennedy Space Center', location='Merritt Island, FL'),
    Address(center='Jet Propulsion Laboratory', location='Pasadena, CA'),
))

for contact in addressbook:
    print(contact)
