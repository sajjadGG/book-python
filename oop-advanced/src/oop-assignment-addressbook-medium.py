class Contact:
    pass

class Address:
    pass


neil = Contact(imie='Neil', nazwisko='Armstrong')
print(neil)
# Neil Armstrong

alan = Contact(imie='Alan', nazwisko='Shepard', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
print(alan)
# Alan Shepard [Houston, Cocoa Beach]

addressbook = [
    Contact(imie='Max', nazwisko='Peck', adresy=[
        Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(imie='José', nazwisko='Jiménez'),
    Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
]


print(addressbook)
# [Max Peck [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
