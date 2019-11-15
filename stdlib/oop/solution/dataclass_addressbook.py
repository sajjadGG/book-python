from dataclasses import dataclass


@dataclass
class Address:
    location: str = None
    city: str = None


@dataclass
class Contact:
    first_name: str
    last_name: str
    addresses: tuple = ()


@dataclass
class AddressBook:
    contacts: tuple


INPUT = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Contact(first_name='Mark', last_name='Watney'),
    Contact(first_name='Melissa', last_name='Lewis', addresses=()),
]
