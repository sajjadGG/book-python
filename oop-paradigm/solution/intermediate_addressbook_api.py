from typing import List, Dict, Optional


class Address:
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        city = getattr(self, 'city', 'n/a')
        return f'{city}'

    def __repr__(self) -> str:
        return self.__str__()


class Contact:
    def __init__(self, first_name: str, last_name: str, addresses: Optional[List[Address]] = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = list(addresses) if addresses else list()

    def __str__(self) -> str:
        if self.addresses:
            return f'{self.first_name} {self.last_name} {self.addresses}'
        else:
            return f'{self.first_name} {self.last_name}'

    def __repr__(self) -> str:
        return self.__str__()


melissa = Contact(first_name='Melissa', last_name='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(first_name='Mark', last_name='Watney', addresses=[Address(city='Houston'), Address(city='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
]


print(addressbook)
# [Jan Twardowski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
