Modelowanie
===========


Polski vs Angielski
-------------------
* Generalna uwaga do wszystkiego: ``str`` jest zawsze bezpiecznym wyborem
* Pola (kolumny) po polsku czy angielsku?
* https://python.astrotech.io/oop/good-practices.html

Numer identyfikacyjny obywatela:

* SSN to nie jest PESEL
* województwo to nie jest stan
* dobre alternatywy: region, state, district, province
* złe alternatywy: prefektura, shire, kanton, land

Kod pocztowy:

* nazwa w USA: zipcode
* nazwa na świecie: postcode, postalcode

Przykłady kodów:

* Polska: 30-219
* Holandia: 2201 AZ
* USA: 30219
* zwróć uwagę na format i występowanie liter, znaków specjalnych, spacji

Data Urodzenia:

* różne formaty dat na świecie
* USA: 7/21/1969
* Japonia: 69/7/21
* Niemcy: 21.07.1969
* Polska: ... brak standardu, jest rekomendacja aby stosować ISO-8601
* ISO-8601: 1969-07-21
* Czy można nie mieć daty urodzenia?
* Czy data urodzenia może nie być w formacie daty? (lato 43)

Nazwisko:

* ``MacGyver`` vs ``Macgyver`` vs ``McGyver``
* ``OHara`` vs ``O'Hara``
* ``Bush, Sr.`` vs ``Bush, Jr.``
* ``Nowak-Kowalski`` -> ``Nowak Kowalski`` (staropolska forma)
* Czy te nazwiska znaczą to samo?


Sanityzacja
-----------
* sanitization podchodzi od słowa 'sane' (świadomy, przytomny)
* normalization pochodzi od słowa 'norm' (norma, standard)
* sanityzacja dotyczy bardziej usuwania znaków specjalnych i eskejpowania (aby ktoś nie zrobił SQL injection)
* normalizacja dotyczy sprowadzania danych do ustandaryzowanej formy (np. wszystkie nazwiska dużymi literami, aby łatwiej porównywać)

>>> def clean_phone(phone):
...     phone = phone.replace('+', '00')
...     phone = re.findall('\d', phone)
...     return phone
>>>
>>>
>>> clean_phone('+48 (12) 345 6789')
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> clean_phone('+48 123 456 789')
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> clean_phone('0048123456789')
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> clean_phone('+48 12 3456-789')
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> clean_phone('+48123456789,1,2')
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2']
>>>
>>> clean_phone('+48123456789,1,2')[:13]
['0', '0', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> def clean_phone(phone):
...     phone = phone.replace('+', '00')
...     phone = re.findall('\d', phone)
...     phone = ''.join(phone)
...     return int(phone)
>>>
>>>
>>> clean_phone('+48 (12) 345 6789')
48123456789
>>>
>>> clean_phone('+48 123 456 789')
48123456789
>>>
>>> clean_phone('0048123456789')
48123456789
>>>
>>> clean_phone('+48 12 3456-789')
48123456789
>>>
>>> clean_phone('+48123456789,1,2')
4812345678912


Problem z Integer
-----------------
>>> phone = 48123456789
>>>
>>> np.array(phone, dtype='int64')
array(48123456789)
>>>
>>> np.array(phone, dtype='int32')
array(878816533, dtype=int32)


Problem z Float
---------------
* Float
* Numeric/Decimal
* Integer
* String
* Float vs Decimal

* IEEE 754 - floating point numbers (oryginalnie z lat 80 - do sprawdzenia)
* konwencja w systemach operacyjnych dotycząca zapisu floatów w pamięci komputera
* dotyczy to producentów pamięci, procesorów oraz systemów operacyjnych
* dotyczy to wszystkich języków programowania (nie tylko Python)
* Wszyscy w fintech (internetowe banki, płatności, kantory itp) to wiedzą
* Prawie nikt poza fintech o tym nie słyszał
* Nigdy nie wolno porównywać floatów bez podania precyzji!

Konwersja float -> bin:

>>> bin(69)
'0b1000101'
>>>
>>> bin(69.0)
Traceback (most recent call last):
TypeError: 'float' object cannot be interpreted as an integer

>>> 1.23
1.23
>>>
>>> 123 * 1e-2
1.23
>>>
>>> mantissa = 123
>>> exponent = -2

Use Case:

>>> cukierek = 0.10
>>> guma = 0.20
>>>
>>> cukierek + guma
0.30000000000000004

>>> from decimal import Decimal
>>>
>>> cukierek = Decimal('0.10')
>>> guma = Decimal('0.20')
>>>
>>> cukierek + guma
Decimal('0.30')

>>> cukierek = 10  # Groszy
>>> guma = 20      # Groszy
>>>
>>> cukierek + guma  # Groszy
30

>>> ZLOTY = 1
>>> GROSZ = 0.01 * ZLOTY
>>>
>>> cukierek = 0.10 / GROSZ
>>> guma = 0.20 / GROSZ
>>>
>>> (cukierek + guma) * GROSZ

Why not Decimal by default?:

>>> %%timeit -n 10_000
>>> result = 0.1 + 0.2
18.1 ns ± 0.198 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

>>> %%timeit -n 10_000
>>> result = Decimal('0.1') + Decimal('0.2')
530 ns ± 9.81 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)


Konwencja nazewnicza
--------------------
* nazwy modeli w liczbie pojedynczej
* nazwy tabel w liczbie mnogiej
* nazwy pól małymi literami
* nazwy tabel (jeżeli są dwoma wyrazami) to nazywam używając snake_case (np. user_names)  lub joinedcase (np. usernames)
* nazwy tabel małymi literami i snake_case lub joinedcase
* nazwy pól z liczbami: snake_case (np. ean_13) lub joinedcase (np. ean13)
* nazwy pól z cyfrą: snake_case (np, ean_8), lub joinedcase (np. ean8)
* Stosujemy PascalCase

* indeksy powinny być
* ale uwaga aby nie było ich za dużo
* każdy indeks spowalnia zapis danych

* pamiętać o problemach IEEE-754: Decimal/Numeric, Float, Interger

* jeżeli jest relacja to zwykle używa się Integer oraz pól z nazwą tabeli docelowej oraz końcówką ``_id`` w nazwie (np. user_id, product_id)


Dobre praktyki
--------------
Tabele ``original`` i ``normalized``:

* Tabela ``user_original`` i w niej umieścić wszystkie dane oryginalne
* Tabela ``user_normalized`` i w niej wszystkie dane oczyszczone
* Zrobić ETL (extract, transform, load) -> do nowej tabeli z oczyszczonymi danymi

Pole ``original_data`` w modelu:

* Można dodać jedno ekstra pole typu ``JSONField``
* Może to być pole ``TEXT`` jak baza nie obsługuje ``JSONField``
* Do tego pola dodać zserializowany obiekt oryginalny
* W tabeli trzymać znormalizowane dane
* Jak będzie problem to zawsze można zaglądnąć do pola i zobaczyć wersję oryginalną

Wildstreamer (nazwa robocza):

* zapisujemy w bazie danych wszystkie requesty, które do nas przychodzą, wraz z nagłówkami HTTP, danymi itp.
* tabela która ma kolumny: ``datetime``, ``src_ip``, ``protocol``, ``method``, ``api_version``, ``sha256``, ``headers``, ``content``
* wszystkie odpowiedzi systemu też są składowane
* Bardzo często wykorzystywana jest Cassandra (zoptymalizowana na write oraz fault-tolerant)
