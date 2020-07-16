from dataclasses import dataclass
from typing import List, Optional, Union


DATA = [
    {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},

    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": "", "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "city": "Космодро́м Байкону́р", "postcode": "", "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": "", "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]


@dataclass
class Address:
    street: str
    city: str
    postcode: Union[int, str]
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: Optional[List[Address]] = None


@dataclass
class Crew:
    members: List[Astronaut]


# crew = []
#
# for row in DATA:
#     addr = row.pop('addresses')
#     astro = Astronaut(**row, addresses=[Address(**a) for a in addr])
#     crew.append(astro)
#
# result = Crew(crew)
# print(result)


result = Crew(members=[
    Astronaut(**row, addresses=[Address(**a) for a in addr])
    for row in DATA
    if (addr := row.pop('addresses'))
])

print(result)
