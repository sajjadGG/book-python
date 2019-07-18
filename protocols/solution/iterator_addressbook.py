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
    building: str
    location: str


kontakt = Contact(first_name='Jan', last_name='Twardowski', addresses=(
    Address(building='Johnson Space Center', location='Houston, Texas'),
    Address(building='Kennedy Space Center', location='Florida'),
    Address(building='Jet Propulsion Laboratory', location='Pasadena, California'),
))

for adres in kontakt:
    print(adres)

# Address(building='Johnson Space Center', location='Houston, Texas')
# Address(building='Kennedy Space Center', location='Florida')
# Address(building='Jet Propulsion Laboratory', location='Pasadena, California')
