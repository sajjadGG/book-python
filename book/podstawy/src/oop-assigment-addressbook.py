neil = Kontakt(imie='Neil', nazwisko='Armstrong')
print(neil)
# Neil Armstrong

alan = Kontakt(imie='Alan', nazwisko='Shepard', adresy=[Adres(miasto='Houston'), Adres(miasto='Cocoa Beach')])
print(alan)
# Alan Shepard [Houston, Cocoa Beach]

ksiazka_adresowa = [
    Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

print(ksiazka_adresowa)
# [Max Peck [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
