*******
Zadania
*******


``map()``, ``filter()`` i ``lambda``
====================================

:Nazwa skryptu: ``bin/funkcyjne.py``
:Uruchamianie: ``python bin/funkcyjne.py``

:Zadanie 1:
    Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33.

:Zadanie 2:
    * Używając funkcji ``filter()`` usuń z niej wszystkie liczby parzyste
    * Używając wyrażenia ``lambda`` i funkcji ``map()`` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
    * Odpowiednio używając funkcji ``sum()``  i ``len()`` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.


REST API
========

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


Generatory vs. Przetwarzanie Listy
==================================

Napisz program, który wczyta plik ``/etc/passwd``, a następnie:

* przefiltruje linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``)
* przefiltruje linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
* zwróci listę loginów takich użytkowników

* Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję.
* Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``.

* Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

Wielowątkowość
==============

* Stwórz kolejkę ``queue`` do której dodasz różne polecenia systemowe do wykonania, np. ``['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']``.
* Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki.
* Wątki powinny być uruchamiane jako ``subprocess`` w systemie operacyjnym z timeoutem równym ``PROCESSING_TIMEOUT = 2.0`` sekundy
* Ilość poleceń może się zwiększać w miarę wykonywania zadania.
* Wątki powinny być uśpione za pomocą ``Timer`` przez 5.0 sekund, a następnie ruszyć do roboty.
* Wątki mają być uruchomione w tle (ang. ``daemon``)
* Użyj logowania za pomocą biblioteki ``logging`` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku
* Napisz testy do workerów i kolejki

:Podpowiedź:
    .. code-block:: python

        import subprocess
        import shlex

        cmd = 'ls -la'

        with Popen(shlex.split(cmd), stdout=PIPE) as proc:
            log.write(proc.stdout.read())

Mini Botnet
===========

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


Panel administracyjny dla Botnetu
=================================

Za pomocą ``Django`` stwórz panel administracyjny dla botnetu:

* Wyszukiwanie aktywnych hostów
* `command`
