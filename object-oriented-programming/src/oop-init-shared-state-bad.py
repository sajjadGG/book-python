class Contact:
    def __init__(self, name, addresses=[]):
        self.name = name
        self.addresses = addresses


watney = Contact(name='Mark Watney')
watney.addresses.append('Houston, TX')
print(watney.addresses)
# ['Houston, TX']

twardowski = Contact(name='Jan Twardowski')
print(twardowski.addresses)
# ['Houston, TX']
