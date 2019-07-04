from dataclasses import dataclass


@dataclass
class Kontakt:
    first_name: str
    last_name: str
    addresses: tuple = ()

    def __iter__(self):
        self.current_element = 0
        return self

    def __next__(self):
        if self.current_element >= len(self.addresses):
            raise StopIteration

        address = self.addresses[self.current_element]
        self.current_element += 1
        return address


class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.__dict__}'


kontakt = Kontakt(first_name='Jan', last_name='Twardowski', addresses=(
    Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
    Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
    Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
    Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
))

for adres in kontakt:
    print(adres)
