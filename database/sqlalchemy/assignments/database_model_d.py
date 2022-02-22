"""
* Assignment: Database Model AddressBook
* Complexity: medium
* Lines of code: 50 lines
* Time: 21 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz model `Person` z polami:
        a. Imię
        b. Nazwisko
        c. Data Urodzenia
        d. Zdjęcie
        e. Telefon (do wyboru typ: domowy, praca, komórka)
        f. Email (do wyboru typ: domowy, praca, komórka)
        g. Adres
    2. Stwórz model `Address` z polami:
        a. Typ (do wyboru typ: domowy, praca, komórka)
        b. Ulica
        c. Numer bloku
        d. Numer mieszkania
        e. Kod pocztowy
        f. Miasto
        g. Region
        h. Kraj
    5. Osoba może mieć wiele adresów, telefonów i e-maili
"""

DATA = [
    {"firstname": "Jan", "lastname": "Twardowski", "addresses": [
        {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "postcode": "31-008", "region": "Małopolskie", "country": "Poland"}]},
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": None, "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": None, "city": "Космодро́м Байкону́р", "postcode": None, "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": None, "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]

# Solution
