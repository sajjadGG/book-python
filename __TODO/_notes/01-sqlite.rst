SQLite3
=======


RDBMS
-----
SQL - Relacyjne bazy danych (list[tuple]):

* PostgreSQL (postgres)
* MySQL, MariaDB
* Oracle
* MSSQL
* SQLite3

NoSQL - Nierelacyjne bazy danych (inne niż list[tuple]):

* Timeseries: list[tuple[datetime, tuple]], przykład: Prometheus, InfluxDB
* Dokumentowe: list[dict], przykład: CouchDB, MongoDB
* Append: list[list[tuple]], przykład: Cassandra
* Grafowe: list[graph], przykład: neo4j
* Obiektowe: list[object]
* Key-value: dict, przykład: BigTable, Riak, Redis, Memcached (meh...)
* Stream: ...

NewSQL - ...

Polyglot persistence (zastosowanie wielu baz danych w jednym projekcie):

* PostgreSQL - do danych użytkowników
* InfluxDB - dane z sensorów
* Cassandra - logi z systemu
* Redis - cache


Różnice
-------
* SQLite3: ``AUTOINCREMENT``
* MySQL: ``AUTO_INCREMENT``
* PostgreSQL: ``SERIAL``

Dlatego stosujemy ORM i autogenerowanie zapytań SQL, aby kod był
przenaszalny pomiędzy różnymi bazami danych (np. testy i produkcja).

1. Czy to ma sens, aby testować kod na innym środowisku niż produkcja?
2. Jak często w projekcie zmieniacie bazę danych?


SQLite3
-------
* Jest w każdej aplikacji na iOS, Android i inne...
* Jest w każdej przeglądarce: Chrome, Firefox, Safari, Edge, Vivaldi
* Jest w każdym Pythonie
* Nie wymaga instalacji żadnego serwera, jest mała i działa
* Jest to tylko i wyłącznie plik binarny oraz opcjonalnie małe narzędzie do zarządzania nim przez linie poleceń
* Obsługuje SQL w standardzie SQL92
* Składnią najbardziej podobny jest do PostgreSQL
* W SQLite3 jest wiele aliasów, np. można napisać ``INT``, ``INTEGER``, ``SMALLINT``, ``BIGINT``, ``BOOL``; wszystkie znaczą to samo - int64
* SQLite3 ma dwa tryby: plik oraz pamięć
* W trybie in-memory (pamięć) dane nie są zapisywane (jest to przydatne w testach, development, i podczas szkoleń)
* in-memory są znacznie szybsze niż plikowe, ale nie zapisują danych
* W SQLite3 nie można zmieniać kolejności oraz nazw kolumn
* Maksymalny rozmiar bazy danych to 281TB (ten limit wynika z maksymalnej wielkości pliku na filesystem, a nie dlatego że SQLite3 limituje)
* Maksymalna liczba tabel to 2 miliardy
* Maksymalna liczba wierszy to 2**64
* Maksymalna liczba kolumn w tabeli to 2000

Pomocnicze polecenia (zaczynają się od kropki):

* ``.help``
* ``.backup FILE``
* ``.dump [TABLE]``
* ``.restore FILE``
* ``.excel``
* ``.import FILE TABLE``
* ``.quit``
* ``.save FILE``
* ``.schema [TABLE]``
* ``.tables``


Typy w bazie danych
-------------------
* ``INTEGER`` -> ``int``    # int64
* ``REAL`` -> ``float``     # float64
* ``TEXT`` -> ``str``       # unicode, utf-8
* ``BLOB`` -> ``bytes``     # Binary Large OBject
* ``NULL`` -> ``None``      # wartości puste lub nieznane

Aliasy:

* ``INTEGER`` -> ``INT``, ``INTEGER``, ``SMALLINT``, ``BIGINT``, ``BOOL``
* ``REAL`` -> ``FLOAT``, ``DOUBLE``, ``DOUBLE PRECISION``, ``NUMERIC``, ``DECIMAL``
* ``TEXT`` -> ``CHAR``, ``VARCHAR``, ``VARYING CHARACTER``, ``CLOB``

Affinity:

* ``TIMESTAMP`` -> ``INTEGER`` lub ``REAL`` w zależności od precyzji
* ``DATE``, ``DATETIME``, ``TIME`` -> albo ``INTEGER``, ``REAL``, ``TEXT`` w zależności od ustawień
* jeżeli data jest ``TEXT``, to w formacie ISO-8601, np. '1969-07-21 02:56:15+00:00'
* jeżeli data jest ``REAL``, to liczba dni liczonych wg. kalendarza Juliańskiego od dnia 4714-11-24 p.n.e. północ czasu Greenwich
* jeżeli data jest ``INTEGER``, to liczba sekund od 1970-01-01 00:00:00 UTC

Constraints:

* ``PRIMARY KEY``
* ``FOREIGN KEY``
* ``NOT NULL``
* ``UNIQUE``
* ``DEFAULT``
* ``INDEX``
* ``CHECK``

Funkcje:

* ``CURRENT_TIMESTAMP``
* ``CURRENT_DATE``
* ``CURRENT_TIME``
* ``DATETIME('NOW', 'LOCALTIME')``
* ``DATETIME('NOW', 'UTC')``
* ``STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')``


SQL
---
* SQLite3: ``AUTOINCREMENT``
* MySQL: ``AUTO_INCREMENT``
* PostgreSQL: ``SERIAL``

* W SQL elementy składni języka (polecania, słowa kluczowe) zwyczajowo zapisujemy dużymi literami
* Małymi literami zapisujemy wprowadzone przez nas elementy, np. nazwy tabel, column, indeksów itp.
* Komentarze w SQL robi się za pomocą ``--``
* W SQL nowe linie oraz puste linie i białe znaki (powyżej jednej spacji) nie mają znaczenia


Tabele
------
* ``CREATE TABLE``
* ``ALTER TABLE``
* ``DROP TABLE``
* ``ALTER TABLE oldname RENAME TO newname``
* ``CREATE TABLE name AS (query)``
* Wyrzuca błąd gdy tabela istnieje
* Można to ominąć dodając ``IF NOT EXISTS``
* Można podglądnąć jak tabela wygląda za pomocą ``.schema``

Tworzenie:

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT UNIQUE,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified DATETIME DEFAULT (DATETIME('NOW', 'UTC'))
    );

Modyfikacja:

.. code-block:: sql

    ALTER TABLE user ADD COLUMN born DATE; -- MySQL
    ALTER TABLE user ADD born DATE; -- PostgreSQL, SQLite3

Kasowanie:

.. code-block:: sql

    DROP TABLE user;


Indeksy
-------
* ``CREATE INDEX``, ``DROP INDEX``
* ``CREATE UNIQUE INDEX`` - no duplicate values allowed
* Można ominąć błąd dodając ``IF NOT EXISTS``
* Wolniej zapisujemy dane
* Szybciej wyszukujemy dane
* Trzeba się zastanowić, czego mamy więcej, zapisów czy odczytów

Typy:

* Column Index
* Partial Index
* Multi Column Index
* Unique Index
* Functional Index
* Binary Index

Tworzenie:

.. code-block:: sql

    CREATE INDEX idx_user_lastname
    ON user(lastname);

.. code-block:: sql

    CREATE UNIQUE INDEX IF NOT EXISTS idx_user_email
    ON user(email);

Kasowanie:

.. code-block:: sql

    DROP INDEX idx_user_email;


Dane
----
* ``INSERT``
* ``UPDATE``
* ``DELETE``
* Bezpieczne pisanie poleceń destruktywnych

Tworzenie:

.. code-block:: sql

    INSERT INTO user
    VALUES (1, 'Mark', 'Watney', 'mwatney@nasa.gov', '2022-02-23 14:38:10', '2022-02-23 14:38:10');

.. code-block:: sql

    INSERT INTO user (firstname, lastname, email)
    VALUES ('Melissa', 'Lewis', 'mlewis@nasa.gov');

Dump:

.. code-block:: console

    $ .dump
    PRAGMA foreign_keys=OFF;
    BEGIN TRANSACTION;
    CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT UNIQUE,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            modified DATETIME DEFAULT (DATETIME('NOW', 'UTC'))
        );
    INSERT INTO user VALUES(1,'Mark','Watney','mwatney@nasa.gov','2022-02-23 14:48:10','2022-02-23 14:48:10');
    INSERT INTO user VALUES(2,'Melissa','Lewis','mlewis@nasa.gov','2022-02-23 13:39:58','2022-02-23 12:39:58');
    COMMIT;

Modyfikacja:

.. code-block:: sql

    UPDATE user SET
        firstname='Rick',
        lastname='Martinez'
    WHERE id=1;

Kasowanie:

.. code-block:: sql

    DELETE FROM user;  -- wszystkie dane
    DELETE FROM user WHERE id=1;
    DELETE FROM user WHERE created < '2000-01-01';


Wybór danych
------------
Słowa kluczowe:

* ``SELECT``
* ``FROM``
* ``ORDER BY``
* ``LIMIT``
* ``OFFSET``
* ``WHERE``
* ``GROUP BY``
* ``HAVING``
* ``WITH``

Operatory:

* ``<``
* ``>``
* ``!=`` lub ``<>``
* ``==`` lub ``=``
* ``>=``
* ``<=``
* ``BETWEEN``
* ``IN``, ``NOT IN``
* ``IS``, ``IS NOT``

Funkcje/Agregacje:

* ``COUNT``
* ``DISTINCT``
* ``SUM``
* ``AVG``


.. code-block:: sql

    SELECT category,
           COUNT(category) AS count
    FROM apollo11
    GROUP BY category
    HAVING count > 50

.. code-block:: sql

    WITH important_categories AS (

        SELECT DISTINCT(category)
        FROM apollo11
        GROUP BY category
        HAVING COUNT(category) < 50
        ORDER BY category ASC
        LIMIT 5
        OFFSET 0

    )

    SELECT datetime AS dt,
           category,
           event

    FROM apollo11

    WHERE category != 'DEBUG'
      AND date >= '1969-07-16'
      AND date <= '1969-07-24'
      AND (date == '1969-07-20' OR date == '1969-07-21')
      AND datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00'
      AND event LIKE '%CDR%'
      AND category IS NOT NULL
      AND category NOT IN ('DEBUG', 'INFO')
      AND category IN ('CRITICAL', 'ERROR')
      AND category IN important_categories
      AND category IN (

        SELECT DISTINCT(category)
        FROM apollo11
        GROUP BY category
        HAVING COUNT(category) < 50
        ORDER BY category ASC
        LIMIT 5
        OFFSET 0

      ) -- CRITICAL, ERROR


    ORDER BY category DESC,
             date ASC NULLS FIRST,
             time ASC NULLS LAST

    LIMIT 30
    OFFSET 0;


Projekcja:

* ``SELECT`` - klauzula projekcji, pozwala na specyfikowanie kolumn, które wyświetlamy
* ``AS`` - pozwala na tworzenie aliasów kolumn, które można użyć w dalszej części zapytania, ale także będą w wynikach (np. w Python lub Pandas)

Selekcja:

* ``WHERE`` - klauzula selekcji, pozwala na określenie warunków, które mają mieć wyniki
* Przy ``WHERE`` można użyć nawet tych kolumn, które są ukryte (nie wybrane w ``SELECT``)
* Jeden warunek w ``WHERE`` nazywa się "criteria"
* ``AND`` i ``OR`` - pozwalają na łączenie kryteriów
* daty można wpisywać jako string i zostaną przekonwertowane przy wyszukiwaniu
* można wpisać tylko część daty, np: '1969-07' (uwaga na różne bazy danych)

Regex:

* ``%`` - dowolny ciąg znaków
* ``_`` - dowolny jeden znak
* można je łączyć np. ``Arm%st_ong
* może być więcej niż jedno wystąpienie, np. '%CDR%'

Podzapytania:

* Układając podzapytanie najlepiej sprawdzać jego wyniki jako osobne query
* W podzapytaniach można używać całej składni ``SELECT``, tj. ``WHERE``, ``LIMIT``, ``OFFSET``, ``ORDER BY``, ``GROUP BY``, ``HAVING``
* W podzapytaniach można także tworzyć kolejne podzapytania

Grupowanie:

* Zbiera wyniki mające tę samą wartość, przykład: ``category``, ``lastname``, ``user_id``
* Otwiera drogę do wykonania innych funkcji i agregacji

Having:

* ``HAVING`` występuje tylko po ``GROUP BY``
* Zwraca wyniki spełniające jakieś warunki, np. ``COUNT(*) > 5``

Funkcje:

* ``COUNT(x)`` - liczba wierszy w kolumnie ``x``
* ``DISTINCT(x)`` - unikalne (niepowtarzające się) wiersze w kolumnie ``x``
* ``DISTINCT x`` - można go używać również jako słowo kluczowe

CTE:

* Common Table Expression
* prawie to samo co subquery
* wykorzystuje konstrukcję ``WITH nazwa AS (...)``
* Bazy danych, które to obsługują mogą lepiej niż w subquery optymalizować wyniki tego CTE

Sortowanie:

* ``ORDER BY`` - sortowanie
* ``ASC`` - rosnące (domyślne)
* ``DESC`` - malejące
* ``NULLS FIRST`` albo ``NULLS LAST``
* ``ORDER BY`` idzie pod koniec zapytania, ale przed ``LIMIT``
* Przy ``ORDER BY`` można użyć nawet tych kolumn, które są ukryte (nie wybrane w ``SELECT``)

Limit:

* paginacja wyników za pomocą ``LIMIT`` i ``OFFSET``
* ``LIMIT`` zawsze idzie na koniec zapytania

Uwagi generalne:

* zapytanie musi kończyć się średnikiem ``;``
* w ``WHERE`` ustawiać klauzule tak, aby jak najszybciej wykluczały jak najwięcej danych (1/2 * 1/24 vs 1/24 * 1/2)
* ``EXPLAIN`` lub ``.explain`` (w SQLite3) które daje nam informacje debugowe dotyczące zapytania


Transakcje
----------
* ``BEGIN TRANSACTION``
* ``COMMIT``
* ``ROLLBACK``
* można tworzyć nazwane transakcje
* można tworzyć podtransakcje i definiować tzw. ``SAVEPOINT nazwa``, a później wycofywać (``ROLLBACK`` tylko do określonego ``SAVEPOINT``, bez utraty całej transakcji
* bazy danych mają automatyczne transakcje, czyli same do każdego naszego zapytania dokładają ``BEGIN TRANSACTION`` i ``COMMIT``


Triki bezpieczeństwa
--------------------
* Wszystkie zapytania modyfikujące scheme lub dane zaczynać od komentarza ``--``, a po napisaniu i upewnieniu się, że jest ok, skasować komentarz i wykonać polecenie
* Zmiana tła w terminalu
* Zmiana prompt (najlepiej dopisać do `/etc/profile` - wtedy jest dla wszystkich userów)

Bash:

.. code-block:: shell

    red='\[\033[00;31m\]'
    green='\[\033[00;32m\]'
    blue='\[\033[00;36m\]'
    white='\[\033[00;39m\]'

    export PS1="\n${red}produkcja> ${white}"

Zsh:

.. code-block:: shell

    export PS1=$'\n%F{red}produkcja> %F{white}'

Dodatkowo można:

.. code-block:: shell

    [ $SSH_CONNECTION ] && export PS1="\n${green}\h $ ${white}"
    [ $UID == 0 ] && export PS1="\n${red}# ${white}"


Python
------


Pandas
------


SQL Injection
-------------



Further Reading
---------------
* https://www.youtube.com/playlist?list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv
* https://www.youtube.com/watch?v=pxrQEp6hqNQ
* https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm
