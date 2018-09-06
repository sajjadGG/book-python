
class Contact:
    def __init__(self, name, addresses=[]):
        self.name = name
        self.addresses = addresses

    def __iadd__(self, other):
        self.addresses.append(other)
        return self

    def __str__(self):
        return f'{self.__dict__}'

    def __contains__(self, item):
        if item in self.addresses:
            return True
        else:
            return False


class Address:
    def __init__(self, location):
        self.city = location

    def __repr__(self):
        return f'{self.__dict__}'


contact = Contact(name='Jose', addresses=[Address(location='JPL')])
contact += Address(location='Houston')
contact += Address(location='KSC')

print(contact)

if Address(location='Bajkonur') in contact:
    print(True)
else:
    print(False)
