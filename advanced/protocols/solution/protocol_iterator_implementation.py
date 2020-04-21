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
    location: str
    city: str


INPUT = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Contact(first_name='Mark', last_name='Watney'),
    Contact(first_name='Melissa', last_name='Lewis', addresses=()),
]

for contact in INPUT:
    print(contact)

# Address(location='Johnson Space Center', city='Houston, TX')
# Address(location='Kennedy Space Center', city='Merritt Island, FL')
# Address(location='Jet Propulsion Laboratory', city='Pasadena, CA')
