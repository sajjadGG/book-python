"""
* Assignment: Database Model Shop
* Complexity: medium
* Lines of code: 50 lines
* Time: 55 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz model `User` z polami:
        a. firstname - imię
        b. lastname - nazwisko
        c. born - data urodzenia
        d. ssn - PESEL
        e. email - adres email
        f. phone - telefon z numerem kierunkowym kraju
    2. Stwórz model `Address` z polami:
        a. type - rodzaj adresu: rozliczeniowy, dostawy
        b. street - ulica, numer domu, numer mieszkania
        c. postcode - kod pocztowy
        d. city - miasto
        e. region - województwo lub stan
        f. country - kraj
    3. Stwórz model `Product`:
        a. ean13 - Kod kreskowy EAN-13
        b. name - Nazwa produktu
        c. price - Cena netto
    4. Stwórz model `Orders`:
        a. user - Użytkownik
        b. product - Produkt
    5. Wymagania funkcjonalne:
        a. Użytkownik ma tylko jeden email i jeden telefon
        b. Użytkownik może mieć jeden adres rozliczeniowy i jeden do wysyłki
        c. Adres może nie mieć ulicy lub kodu pocztowego
        d. Użytkownik może zakupić wiele produktów
        e. Produkt mógł nie zostać kupiony
    6. Wymagania niefunkcjonalne:
        a. Dodaj pola `id` jeżeli są potrzebne
        b. Możesz użyć dowolnego modułu z biblioteki standardowej
        c. Możesz użyć SQLAlchemy i Alembic
        d. Nie instaluj ani nie używaj dodatkowych pakietów
    7. Wyświetl dane odpowiadające na pytania:
        a. Imię i nazwisko osoby, która dokonała najwięcej zakupów?
        b. Imię i nazwisko osoby, która dokonała zakupów za największą kwotę?
        c. Kwota, za jaką łącznie dokonały zamówień kobiety?
        d. Nazwa produktu, który był najczęściej kupowany?
        e. Kwota i nazwa kraju, którego obywatele dokonali najwięcej zakupów?
        f. Kwota i nazwa kraju, którego obywatele dokonali zakupów za największą kwotę?

    Tests:
        >>> import sys; sys.tracebacklimit = 0

        >>> assert result_a is not Ellipsis, \
        'Assign result to variable: `result_a`'
        >>> assert type(result_a) is tuple, \
        'Variable `result_a` has invalid type, should be tuple[str,str]'
        >>> assert type(result_a[0]) is str, \
        'Variable `result_a` has invalid type, should be tuple[str,str]'
        >>> assert type(result_a[1]) is str, \
        'Variable `result_a` has invalid type, should be tuple[str,str]'

        >>> assert result_b is not Ellipsis, \
        'Assign result to variable: `result_b`'
        >>> assert type(result_b) is tuple, \
        'Variable `result_b` has invalid type, should be tuple[str,str]'
        >>> assert type(result_b[0]) is str, \
        'Variable `result_b` has invalid type, should be tuple[str,str]'
        >>> assert type(result_b[1]) is str, \
        'Variable `result_b` has invalid type, should be tuple[str,str]'

        >>> assert result_c is not Ellipsis, \
        'Assign result to variable: `result_c`'
        >>> assert type(result_c) is float, \
        'Variable `result_c` has invalid type, should be float'

        >>> assert result_d is not Ellipsis, \
        'Assign result to variable: `result_d`'
        >>> assert type(result_d) is str, \
        'Variable `result_d` has invalid type, should be str'

        >>> assert result_e is not Ellipsis, \
        'Assign result to variable: `result_e`'
        >>> assert type(result_e) is tuple, \
        'Variable `result_e` has invalid type, should be tuple[float,str]'
        >>> assert type(result_e[0]) is float, \
        'Variable `result_e` has invalid type, should be tuple[float,str]'
        >>> assert type(result_e[1]) is str, \
        'Variable `result_e` has invalid type, should be tuple[float,str]'

        >>> assert result_f is not Ellipsis, \
        'Assign result to variable: `result_f`'
        >>> assert type(result_f) is tuple, \
        'Variable `result_f` has invalid type, should be tuple[float,str]'
        >>> assert type(result_f[0]) is float, \
        'Variable `result_f` has invalid type, should be tuple[float,str]'
        >>> assert type(result_f[1]) is str, \
        'Variable `result_f` has invalid type, should be tuple[float,str]'
"""


USERS = """firstname,lastname,gender,born,ssn,email,phone
Mark,Watney,male,1994-10-12,94101212345,mwatney@nasa.gov,+1 (234) 555-0000
Melissa,Lewis,female,1995-07-15,95071512345,mlewis@nasa.gov,+1 (234) 555-0001
Rick,Martinez,male,1996-01-21,96012112345,rmartinez@nasa.gov,+1 (234) 555-0010
Alex,Vogel,male,1994-11-15,94111512345,avogel@esa.int,+49 (234) 555-0011
Beth,Johanssen,female,2006-05-09,06250912345,bjohanssen@nasa.gov,+1 (234) 555-0100
Chris,Beck,male,1999-08-02,99080212345,cbeck@nasa.gov,+1 (234) 555-0101"""

ADDRESSES = """user,type,street,city,postcode,region,country
mwatney@nasa.gov,billing,2101 E NASA Pkwy,Houston,77058,Texas,USA
mwatney@nasa.gov,shipment,,Kennedy Space Center,32899,Florida,USA
mlewis@nasa.gov,shipment,Kamienica Pod św. Janem Kapistranem,Kraków,31008,Małopolskie,Poland
rmartinez@nasa.gov,billing,,Звёздный городо́к,141160,Московская область,Россия
rmartinez@nasa.gov,shipment,,Космодро́м Байкону́р,,Кызылординская область,Қазақстан
avogel@esa.int,shipment,Linder Hoehe,Köln,51147,North Rhine-Westphalia,Germany
bjohanssen@nasa.gov,shipment,2825 E Ave P,Palmdale,93550,California,USA
cbeck@nasa.gov,shipment,4800 Oak Grove Dr,Pasadena,91109,California,USA"""

PRODUCTS = """ean13,name,price
5039271113244,Alfa,123.00
5202038482222,Bravo,312.22
5308443764554,Charlie,812.00
5439667086587,Delta,332.18
5527865721147,Echo,114.00
5535686226512,Foxtrot,99.12
5721668602638,Golf,123.00
5776136485596,Hotel,444.40
5863969679442,India,674.21
5908105406923,Juliet,324.00
5957751061635,Kilo,932.20
6190780033092,Lima,128.00
6512625994397,Mike,91.00
6518235371269,November,12.00
6565923118590,Oscar,43.10
6650630136545,Papa,112.00
6692669560199,Quebec,997.10
6711341590108,Romeo,1337.00
6816011714454,Sierra,998.10
7050114819954,Tango,123.00
7251625012784,Uniform,564.99
7251925199277,Victor,990.50
7283004100423,Whisky,881.89
7309682004683,X-Ray,123.63
7324670042560,Zulu,311.00"""

ORDERS = """user,product
mwatney@nasa.gov,Sierra
mwatney@nasa.gov,Victor
bjohanssen@nasa.gov,Delta
mlewis@nasa.gov,November
rmartinez@nasa.gov,Mike
mwatney@nasa.gov,Bravo
mwatney@nasa.gov,Kilo
avogel@esa.int,Victor
bjohanssen@nasa.gov,Romeo
bjohanssen@nasa.gov,Whisky
cbeck@nasa.gov,Zulu
mwatney@nasa.gov,Romeo
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Victor
bjohanssen@nasa.gov,Whisky
mlewis@nasa.gov,Whisky
rmartinez@nasa.gov,Mike
mwatney@nasa.gov,November
mwatney@nasa.gov,Kilo
avogel@esa.int,Bravo
bjohanssen@nasa.gov,X-Ray
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Victor
bjohanssen@nasa.gov,India
mlewis@nasa.gov,Juliet
rmartinez@nasa.gov,Foxtrot
avogel@esa.int,Victor
bjohanssen@nasa.gov,Romeo
bjohanssen@nasa.gov,Whisky
cbeck@nasa.gov,Zulu
mwatney@nasa.gov,Alfa
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Quebec"""

# Solution
def parse(data):
    header, *rows = data.splitlines()
    header = header.split(',')
    return [dict(zip(header,values))
            for row in rows
            if (values := row.split(','))]

users = parse(USERS)
addresses = parse(ADDRESSES)
products = parse(PRODUCTS)
orders = parse(ORDERS)


# Imię i nazwisko osoby, która dokonała najwięcej zakupów.
# result_a: tuple[str,str]
result_a = ...

# Imię i nazwisko osoby, która dokonała zakupów za największą kwotę.
# result_b: tuple[str,str]
result_b = ...

# Kwota, za jaką łącznie dokonały zamówień kobiety.
# result_c: int
result_c = ...

# Nazwa produktu, który był najczęściej kupowany.
# result_d: str
result_d = ...

# Kwota i nazwa kraju, którego obywatele dokonali najwięcej zakupów.
# result_e: tuple[float,str]
result_e = ...

# Kwota i nazwa kraju, którego obywatele dokonali zakupów za największą kwotę.
# result_f: tuple[float,str]
result_f = ...
