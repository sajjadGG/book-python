
class Contact:
    def __init__(self, name, addresses=[]):
        self.name = name
        self.addresses = addresses

    def __add__(self, other):
        self.addresses.append(other)

    def __str__(self):
        return f'{self.__dict__}'

    def __contains__(self, item):
        if item in self.addresses:
            return True
        else:
            return False


class Address:
    def __init__(self, city):
        self.city = city

    def __repr__(self):
        return f'{self.__dict__}'


contact = Contact(name='Jose')
address = Address(city='Houston')

contact + address
print(contact)

if address in contact:
    print(True)
else:
    print(False)
