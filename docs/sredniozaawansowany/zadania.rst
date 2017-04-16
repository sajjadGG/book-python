*******
Zadania
*******


Parsowanie ``/etc/hosts``
=========================

Z twojego systemu operacyjnego wyciągnij plik ``/etc/hosts`` i przedstaw go w formie listy dictów jak w przykładzie poniżej:

.. code-block:: python

    {'ip': '127.0.0.1', 'hostnames': ['localhost'], 'protocol': 'ipv4'},
    {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'ipv4'},
    {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'ipv6'},

:Uwaga:
    * Zwróć uwagę na uprawnienia do odczytu pliku
    * System Windows również posiada ten plik (``C:/Windows/System32/drivers/etc/hosts``)

Parsowanie ``/etc/passwd``
==========================
The ``/etc/passwd`` file is a colon-separated file that contains the following information:
- User name
- Encrypted password
- User ID number (UID)
- User's group ID number (GID)
- Full name of the user (GECOS)
- User home directory
- Login shell


Książka adresowa
================

:Nazwa skryptu: ``bin/ksiazka-adresowa.py``
:Uruchamianie: ``python bin/ksiazka-adresowa.py``

:Zadanie:
    Napisz książkę adresową, która będzie zapisywała dane do pliku w formacie json.
    Każdy z użytkowników jest reprezentowany przez:

    * imię
    * nazwisko
    * telefon
    * adres

     * ulica
     * miasto
     * kod_pocztowy
     * wojewodztwo
     * panstwo

    Wszystkie dane w książce muszą być reprezentowane przez typy proste.

:Zadanie 2:
    Bardzo często wykorzystywanym typem pliku jest CSV, czyli wartości oddzielone przecinkami. Zamień format pliku na ten typ. Zrób tak, aby dane trafiły do odpowiednich kolumn nawet po przesortowaniu. Użyj ``csv.DictWriter()``. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami.

:Zadanie 3:
    Zmodyfikuj aby można było wpisywać wiele adresów.

:Zadanie 4:
    Zmodyfikuj program aby wykorzystywał klasy do reprezentowania wpisów w książce. Które podejście jest lepsze?

:Zadanie 5:
    Teraz wykorzystaj plik bazy danych sqlite aby trzymać informacje w tabeli. Które podejście jest lepsze?

:Zadanie 6:
    Wykorzystaj Django do stworzenia takiego modelu i wygeneruj panel administracyjny. Trudne?

:Pytanie:
    * Które podejście było najłatwiejsze?
    * W jakim formacie najlepiej przechowywać dane?
    * Które podejście jest najlepsze dla innych programistów, a które dla użytkowników?

Walidacja PESEL
===============

Za pomocą wyrażeń regularnych sprawdź:

* czy pesel jest poprawny
* jaka jest data urodzenia? (podaj obiekt ``datetime.date``
* płeć użytkownika który podał PESEL

:Z gwiazdką:
    * sprawdź walidację numerów PESEL dla osób urodzonych po 2000 roku.
    * sprawdź sumę kontrolną

Zbalansowanie nawiasów
======================

:Nazwa skryptu: ``bin/zbalansowanie-nawiasow.py``
:Uruchamianie: ``python bin/zbalansowanie-nawiasow.py``

:Zadanie 1:
    Napisz kod który sprawdzi zbalansowanie nawiasów, tzn. czy ilość otwieranych nawiasów jest równa ilości nawiasów zamykanych. Zwórć uwagę, że mogą być cztery typy nawiasów:

    * okrągłe: ``(`` i ``)``
    * kwadratowe: ``[`` i ``]``
    * klamrowe ``{`` i ``}``
    * trójkątne ``<`` i ``>``

:Zadanie 2:
    Rozbuduj poniższy zestaw testów i napisz funkcjonalność.

    .. code-block:: python

        >>> dane = "() [] () ([]()[])"
        >>> zbalansowanie_nawiasow(a)
        True
        >>> dane = "( (] ([)]"
        >>> zbalansowanie_nawiasow(a)
        False

:Zadanie 3:
    Spróbuj użyć rekurencji.
