from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    addresses: tuple = ()

    def __iter__(self):
        self._current_element = 0
        return self

    def __next__(self):
        if self._current_element >= len(self.addresses):
            raise StopIteration

        result = self.addresses[self._current_element]
        self._current_element += 1
        return result


@dataclass
class Address:
    center: str
    location: str


addressbook = Contact(first_name='Jan', last_name='Twardowski', addresses=(
    Address(center='Johnson Space Center', location='Houston, TX'),
    Address(center='Kennedy Space Center', location='Merritt Island, FL'),
    Address(center='Jet Propulsion Laboratory', location='Pasadena, CA'),
))

for contact in addressbook:
    print(contact)

# Address(center='Johnson Space Center', location='Houston, TX')
# Address(center='Kennedy Space Center', location='Merritt Island, FL')
# Address(center='Jet Propulsion Laboratory', location='Pasadena, CA')
