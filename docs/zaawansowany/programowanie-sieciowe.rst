**********************
Programowanie sieciowe
**********************

Socket
======

Otwieranie połączeń
-------------------

Nasłuchiwanie
-------------

Przekazywanie informacji
------------------------

Prosty serwer HTTP
==================

Biblioteki sieciowe
===================

``httplib``
-----------

``urllib``
----------

``smtp``
--------

``HTML Scrapping``
==================

* ``BeautifulSoup``


Zadania kontrolne
=================


REST API
--------

Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika Django na https://github.com

* w przeglądarce internetowej wygeneruj w swoim profilu token https://github.com/settings/tokens

* Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.

.. code-block:: python

    "name": "django",
    "full_name": "django/django",

    # wyszukaj "commits_url": ???

* Przeglądnij to repozytorium i jego listę commitów.
* Podaj datę i opis ostatniego commita
* Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu
* Spróbuj skorzystać zamiast biblioteki standardowej z pakietu ``requests``

.. code:: REST

    https://api.github.com/

    GET /orgs/django/repos
    GET /repos/dajngo/django/commits


.. code:: shell

    curl https://api.github.com/orgs/django/repos


.. code-block:: python

    >>> auth = b'username:token'
    >>> headers={
    ...     'Authorization': 'Basic {}'.format(base64.b64encode(auth).decode('ascii')),
    ...     'User-Agent': 'Python HTTP',
    ...}

    # ...

    >>> body = resp.read().decode()
    >>> data = json.loads(body)


Mini Botnet
-----------

Stwórz program, który otworzy socket na porcie na localhoście podanym przez użytkownika z linii poleceń (wykorzystaj ``argparse``) i będzie nasłuchiwał połączeń. Zweryfikuj za pomocą ``telnet`` albo ``netcat`` czy program odpowiada. Następnie napisz w pythonie klienta, który będzie wysyłał polecenia do tamtego programu.

:Uwaga:
    * nigdy nie rób tego na produkcji bez tzw. sanityzacji parametrów, np. lista zaufanych hostów, możliwe polecenia!
    * pliki nazwij:

        * ``victim.py`` - ofiara
        * ``attacker-ping-server.py`` - serwer przyjmujący
        * ``attacker-execute-client.py``

* zrób aby przetwarzanie requestów było nieblokujące, tzn. otwieraj wątek dla każdego zapytania
* program wykona polecenie za pomocą ``eval``, które przyszło z zapytania
* wykonaj polecenie w systemie operacyjnym i zwróć klientowi odpowiedź
* dodaj funkcję aby wyświetlał dowolny plik
* dodaj funkcję aby listował dowolny katalog - wykorzystaj ``os.walk`` oraz ``os.path.join`` do łączenia nazw katalogów
* zmodyfikuj program aby przyjmował zapytania w formacie XML, pole command oraz arguments powinny być osobno
* zmodyfikuj program aby przyjmował zapytania w formacie JSON, pole command oraz arguments powinny być osobno
* stwórz dekorator ``localhost_only``, który będzie sprawdzał IP źródłowe połączenia i jeżeli nie pochodzi z ``127.0.0.1`` odmówi wykonania polecenia
* stwórz dekorator ``log_request``, który weźmie parametry zapytania (IP, polecenie, argumenty) i zapisze je do pliku ``/tmp/botnet.log`` w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS``

:Podpowiedź:
    * ``subprocess.Popen``
    * użyj ``os.path.join`` do łączenia sciezki i nazwy pliku


:Zadanie z gwiazdką:
    Za pomocą ``Django`` stwórz panel administracyjny dla botnetu:

    * Wyszukiwanie aktywnych hostów
    * `command`
