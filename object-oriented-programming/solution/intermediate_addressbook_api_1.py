class AddressBook:
    def __init__(self, contacts=()):
        self.contacts = contacts

    def __str__(self):
        out = ', '.join(str(x) for x in self.contacts)
        return f'[{out}]'


class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses

    def __str__(self):
        if not self.addresses:
            return f'{self.first_name} {self.last_name}'
        else:
            out = ', '.join(str(x) for x in self.addresses)
            return f'{self.first_name} {self.last_name} [{out}]'


class Address:
    def __init__(self, city=None, street=None, state=None, post_code=None, country=None):
        self.city = city
        self.street = street
        self.state = state
        self.post_code = post_code
        self.country = country

    def __str__(self):
        return f'{self.city}'


melissa = Contact(first_name='Melissa', last_name='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(first_name='Mark', last_name='Watney', addresses=[Address(city='Houston'), Address(city='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = AddressBook([
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston', state='Texas', post_code='77058', country='USA'),
        Address(street=None, city='Kennedy Space Center', post_code='32899', country='USA'),
        Address(street='4800 Oak Grove Dr', city='Pasadena', post_code='91109', country='USA'),
        Address(street='2825 E Ave P', city='Palmdale', state='California', post_code='93550', country='USA'),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
])


print(addressbook)
# [Jan Twardowski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]

print(addressbook.contacts[0].adresy[1].miasto)
