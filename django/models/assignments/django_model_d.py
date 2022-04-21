"""
* Assignment: Database Model Shop
* Complexity: medium
* Lines of code: 100 lines
* Time: 55 min

English:
    0. Create project `shop`
    1. Create model `Customer`:
        a. firstname
        b. lastname
        c. born
        d. tax_number
        e. email
        f. phone (including country code)
    2. Create model `Address` with fields:
        a. type - billing or shipping
        b. street - street, house number, apartment
        c. postcode
        d. city
        e. region
        f. country
    3. Create model `Product` with fields:
        a. ean13 - EAN-13 Barcode
        b. name - Product name
        c. price - Net price (without tax)
    4. Create model `Orders` with fields:
        a. customer
        b. product
    5. Functional requirements:
        a. Customer has only one email address and one phone number
        b. Customer has only one shipping address and one billing address
        c. Address without street, or postcode are possible
        d. Customer can buy many products
        e. Product might not be sold
    6. Non-functional requirements:
        a. You may use any Python standard library module
        b. You can use Django with migrations
        c. Do not install any additional packages
    7. Display data which answer the following questions:
        a. Firstname and lastname of a customer who did the most purchases
        b. Firstname and lastname of a customer who paid the most
        c. Total amount, of purchases done by woman
        d. Name of a product which was purchased the most
        e. Amount and country name, from which people did the most purchases
        f. Amount and country name, from which people paid the most

Polish:
    0. Stwórz projekt `shop`
    1. Stwórz model `Customer` z polami:
        a. firstname - imię
        b. lastname - nazwisko
        c. born - data urodzenia
        d. tax_number - NIP
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
        a. customer - Klient
        b. product - Produkt
    5. Wymagania funkcjonalne:
        a. Klient ma tylko jeden email i jeden telefon
        b. Klient może mieć jeden adres rozliczeniowy i jeden do wysyłki
        c. Adres może nie mieć ulicy lub kodu pocztowego
        d. Klient może zakupić wiele produktów
        e. Produkt mógł nie zostać sprzedany
    6. Wymagania niefunkcjonalne:
        a. Możesz użyć dowolnego modułu z biblioteki standardowej
        b. Możesz użyć Django
        c. Nie instaluj ani nie używaj dodatkowych pakietów
    7. Wyświetl dane odpowiadające na pytania:
        a. Imię i nazwisko osoby, która dokonała najwięcej zakupów?
        b. Imię i nazwisko osoby, która dokonała zakupów za największą kwotę?
        c. Kwota, za jaką łącznie dokonały zamówień kobiety?
        d. Nazwa produktu, który był najczęściej kupowany?
        e. Kwota i nazwa kraju, którego obywatele dokonali najwięcej zakupów?
        f. Kwota i nazwa kraju, którego obywatele dokonali zakupów za
        największą kwotę?
"""

CUSTOMERS = [
    {'firstname': 'Mark', 'lastname': 'Watney', 'born': '1994-10-12',
     'gender': 'male', 'ssn': '94101212345', 'email': 'mwatney@nasa.gov',
     'phone': '+1 (234) 555-0000'},
    {'firstname': 'Melissa', 'lastname': 'Lewis', 'born': '1995-07-15',
     'gender': 'female', 'ssn': '95071512345', 'email': 'mlewis@nasa.gov',
     'phone': '+1 (234) 555-0001'},
    {'firstname': 'Rick', 'lastname': 'Martinez', 'born': '1996-01-21',
     'gender': 'male', 'ssn': '96012112345', 'email': 'rmartinez@nasa.gov',
     'phone': '+1 (234) 555-0010'},
    {'firstname': 'Alex', 'lastname': 'Vogel', 'born': '1994-11-15',
     'gender': 'male', 'ssn': '94111512345', 'email': 'avogel@esa.int',
     'phone': '+49 (234) 555-0011'},
    {'firstname': 'Beth', 'lastname': 'Johanssen', 'born': '2006-05-09',
     'gender': 'female', 'ssn': '06250912345', 'email': 'bjohanssen@nasa.gov',
     'phone': '+1 (234) 555-0100'},
    {'firstname': 'Chris', 'lastname': 'Beck', 'born': '1999-08-02',
     'gender': 'male', 'ssn': '99080212345', 'email': 'cbeck@nasa.gov',
     'phone': '+1 (234) 555-0101'}]

ADDRESSES = [
    {'user': 'mwatney@nasa.gov', 'type': 'billing',
     'street': '2101 E NASA Pkwy', 'city': 'Houston', 'postcode': '77058',
     'region': 'Texas', 'country': 'USA'},
    {'user': 'mwatney@nasa.gov', 'type': 'shipping', 'street': '',
     'city': 'Kennedy Space Center', 'postcode': '32899', 'region': 'Florida',
     'country': 'USA'},
    {'user': 'mlewis@nasa.gov', 'type': 'shipping',
     'street': 'Kamienica Pod św. Janem Kapistranem', 'city': 'Kraków',
     'postcode': '31008', 'region': 'Małopolskie', 'country': 'Poland'},
    {'user': 'rmartinez@nasa.gov', 'type': 'billing', 'street': '',
     'city': 'Звёздный городо́к', 'postcode': '141160',
     'region': 'Московская область', 'country': 'Россия'},
    {'user': 'rmartinez@nasa.gov', 'type': 'shipping', 'street': '',
     'city': 'Космодро́м Байкону́р', 'postcode': '',
     'region': 'Кызылординская область', 'country': 'Қазақстан'},
    {'user': 'avogel@esa.int', 'type': 'shipping', 'street': 'Linder Hoehe',
     'city': 'Köln', 'postcode': '51147', 'region': 'North Rhine-Westphalia',
     'country': 'Germany'},
    {'user': 'bjohanssen@nasa.gov', 'type': 'shipping',
     'street': '2825 E Ave P', 'city': 'Palmdale', 'postcode': '93550',
     'region': 'California', 'country': 'USA'},
    {'user': 'cbeck@nasa.gov', 'type': 'shipping',
     'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'postcode': '91109',
     'region': 'California', 'country': 'USA'}]

PRODUCTS = [
    {'ean13': '5039271113244', 'name': 'Alfa', 'price': '123.00'},
    {'ean13': '5202038482222', 'name': 'Bravo', 'price': '312.22'},
    {'ean13': '5308443764554', 'name': 'Charlie', 'price': '812.00'},
    {'ean13': '5439667086587', 'name': 'Delta', 'price': '332.18'},
    {'ean13': '5527865721147', 'name': 'Echo', 'price': '114.00'},
    {'ean13': '5535686226512', 'name': 'Foxtrot', 'price': '99.12'},
    {'ean13': '5721668602638', 'name': 'Golf', 'price': '123.00'},
    {'ean13': '5776136485596', 'name': 'Hotel', 'price': '444.40'},
    {'ean13': '5863969679442', 'name': 'India', 'price': '674.21'},
    {'ean13': '5908105406923', 'name': 'Juliet', 'price': '324.00'},
    {'ean13': '5957751061635', 'name': 'Kilo', 'price': '932.20'},
    {'ean13': '6190780033092', 'name': 'Lima', 'price': '128.00'},
    {'ean13': '6512625994397', 'name': 'Mike', 'price': '91.00'},
    {'ean13': '6518235371269', 'name': 'November', 'price': '12.00'},
    {'ean13': '6565923118590', 'name': 'Oscar', 'price': '43.10'},
    {'ean13': '6650630136545', 'name': 'Papa', 'price': '112.00'},
    {'ean13': '6692669560199', 'name': 'Quebec', 'price': '997.10'},
    {'ean13': '6711341590108', 'name': 'Romeo', 'price': '1337.00'},
    {'ean13': '6816011714454', 'name': 'Sierra', 'price': '998.10'},
    {'ean13': '7050114819954', 'name': 'Tango', 'price': '123.00'},
    {'ean13': '7251625012784', 'name': 'Uniform', 'price': '564.99'},
    {'ean13': '7251925199277', 'name': 'Victor', 'price': '990.50'},
    {'ean13': '7283004100423', 'name': 'Whisky', 'price': '881.89'},
    {'ean13': '7309682004683', 'name': 'X-Ray', 'price': '123.63'},
    {'ean13': '7324670042560', 'name': 'Zulu', 'price': '311.00'}]

ORDERS = [
    {'user': 'mwatney@nasa.gov', 'product': 'Sierra'},
    {'user': 'mwatney@nasa.gov', 'product': 'Victor'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Delta'},
    {'user': 'mlewis@nasa.gov', 'product': 'November'},
    {'user': 'rmartinez@nasa.gov', 'product': 'Mike'},
    {'user': 'mwatney@nasa.gov', 'product': 'Bravo'},
    {'user': 'mwatney@nasa.gov', 'product': 'Kilo'},
    {'user': 'avogel@esa.int', 'product': 'Victor'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Romeo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'user': 'cbeck@nasa.gov', 'product': 'Zulu'},
    {'user': 'mwatney@nasa.gov', 'product': 'Romeo'},
    {'user': 'avogel@esa.int', 'product': 'Romeo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Victor'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'user': 'mlewis@nasa.gov', 'product': 'Whisky'},
    {'user': 'rmartinez@nasa.gov', 'product': 'Mike'},
    {'user': 'mwatney@nasa.gov', 'product': 'November'},
    {'user': 'mwatney@nasa.gov', 'product': 'Kilo'},
    {'user': 'avogel@esa.int', 'product': 'Bravo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'X-Ray'},
    {'user': 'avogel@esa.int', 'product': 'Romeo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Victor'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'India'},
    {'user': 'mlewis@nasa.gov', 'product': 'Juliet'},
    {'user': 'rmartinez@nasa.gov', 'product': 'Foxtrot'},
    {'user': 'avogel@esa.int', 'product': 'Victor'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Romeo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Whisky'},
    {'user': 'cbeck@nasa.gov', 'product': 'Zulu'},
    {'user': 'mwatney@nasa.gov', 'product': 'Alfa'},
    {'user': 'avogel@esa.int', 'product': 'Romeo'},
    {'user': 'bjohanssen@nasa.gov', 'product': 'Quebec'}]
