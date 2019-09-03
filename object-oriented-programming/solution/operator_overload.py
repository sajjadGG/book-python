class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = list(addresses)

    def __str__(self):
        return f'{self.__dict__}'

    def __iadd__(self, other):
        self.addresses.append(other)
        return self

    def __contains__(self, item):
        for address in self.addresses:
            if address == item:
                return True
        return False


class Address:
    def __init__(self, location, center):
        self.center = center
        self.location = location

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if self.location == other.location:
            return True
        else:
            return False


contact = Contact(first_name='Jan', last_name='Twardowski', addresses=(
    Address(center='Johnson Space Center', location='Houston, TX'),
    Address(center='Kennedy Space Center', location='Merritt Island, FL'),
))

contact += Address(center='Jet Propulsion Laboratory', location='Pasadena, CA')
contact += Address(center='Armstrong Flight Research Center', location='Edwards AFB, CA')

print(contact)
# {'name': 'José Jiménez', 'addresses': [
#       {'location': 'JPL'},
#       {'location': 'Houston'},
#       {'location': 'KSC'}
# ]}

if Address(center='Armstrong Flight Research Center', location='Edwards AFB, CA') in contact:
    print(True)
else:
    print(False)
# True
