SQLAlchemy
==========


Program szkolenia
-----------------
Wprowadzenie do systemów ORM
- Założenia projektowe baz danych i optymalizacja przechowywania informacji
- Typy normalizacji baz danych
- Dobre praktyki projektowe

Modelowanie danych – SQLAlchemy:
- Tworzenie lokalnej bazy danych
- Tworzenie kluczy głównych i pomocniczych
- Tworzenie prostych tablic

Tworzenie relacyjnych tablic:
a) 1 do 1
b) 1 do ∞
c) ∞ do ∞

Operacje:
- Usuwanie tablic
- Zmiana schematu relacji tabel
- Migracje
- Przywracanie poprzedniej wersji bazy danych

Interakcja z bazą danych:
- Odczytywanie danych z tablic relacyjnych i nierelacyjnych
- Edycja poszczególnych wartości/rekordów
- Tworzenie zapytań z relacjami
- Tworzenie podzapytań
- Przekazywanie odpowiedzi zapytań do tablic pandas dataframe

Funkcje i analiza:
- Wykorzystanie podstawowych funkcji matematycznych dla wyselekcjonowanego zbioru danych
- Funkcje generujące wykresy i statystyki
- Wykorzystanie przypisanych funkcji pythona zdeterminowanych przez użytkownika


Instalacja
----------
* Jakie bazy danych obsługuje
* Do czego służy
* Procentowy udział w rynku

.. code-block:: console

    $ pip install sqlalchemy


Struktura plików w projekcie
----------------------------
* Jak dzielić na pliki
* Stałe do konfiguracji


Korzystanie
-----------
* Gdzie konfiguracja
* Stringi JSBC do połączenia

>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Column, String, Integer
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker

Create engine:

>>> create_engine('sqlite:///myfile.db') # echo=True

Create session:

>>> sessionmaker(bind=engine).__call__()

Create model base:

>>> Base = declarative_base()


Modele
------
* modele dziedziczą po Base
* modele specyfikują atrybut __tablename__
* Można używać legacy bazy danych
* Preferowane jest stworzenie nowej bazy za pomocą SQLAlchemy
* Wtedy modele dokładnie odwzorowują to co jest w bazie danych
* Domyślny __init__, ale można użyć własnego
* Base pozwala na przechowywanie definicji tablic i zarządzanie nimi
* Pamiętać aby dodać __str__() bo się kiepsko wyświetla

>>> class User(Base):
...     __tablename__ = 'user'
...
...     username = Column(String, primary_key=True)
...     password = Column(String)
...
...     def __init__(self, username, password):
...         self.username = username
...         self.password = password

Create all tables in database:

>>> Base.metadata.create_all(engine)


Dodawanie obiektów
------------------
* Samo stworzenie instancji modelu nie wykonuje zapytania na bazie
* Dopiero commit to robi
* IntegrityError jest podnoszony, gdy naruszana jest np. unikalność pola

>>> user = User('myusername', 'mypassword')
>>> session.add(user)
>>> session.commit()

>>> user1 = User('Mark', 'Watney')
>>> user2 = User('Melissa', 'Lewis')
>>> session.add(user1)
>>> session.add(user2)
>>> session.commit()


Relacje
-------
* Specyfikacja
* Query
* Migracje


Query
-----
* Podzapytania
* Relacje
* Field lookup
* Q i F (analogia do Django)
* Regexp
* Full text search
* Szukanie dat
* All i One
* Typy rezultatów

>>> result = session.query(User).all()


Agregacje
---------


Funkcje
-------
* Count
* Timestamp
* Current date

>>> from sqlalchemy import func
>>> func.__all__


Nomenklatura
------------
* ix - index
* uq - unique
* ck - check constraints
* fk - foreign key
* pk - primary key


Validation
----------
* Validation for models
* SQLAlchemy validation is before it save data to database
* Unique constraints (unique together)


Indeksy
-------
* Multi-column indexes
* Partial indexing (indeksuje tylko część danych w kolumnie, np. pracowników tylko jednej firmy)
* Functional/Expression Indexing

ann = {'references': []}
reply1 = {'references': [ann]}
reply2 = {'references': [ann, reply1]}


Sesje
-----
* pozwalają na dodawanie rzeczy do bazy
* na koniec commit
* context manager with session
* session scoping
* in a web application, a session should follow the lifecycle of a request


Connection Pools
----------------
* opening new connection is slow
* używane do nieubijania sesji po zakończeniu obsługiwania połączenia
* po obsłudze requestu połączenie wraca do puli
* parametr pool_size oraz max_overflow (o ile połączeń może pula przekroczyć)
* timeout jest w sekundach
* use_lifo - jeżeli True, to ostatnie połączenie które zostało zwrócone do puli będzie pierwszym oddanym przy nowym żądaniu (najstarsze połączenia są głodzone i giną)
* znany problem, jeżeli od jakiegoś czasu nie dostaliśmy połączenia, to wszyskie połączenia w puli nam umrą i pierwszy request będzie długi
* keepalive przy jdbc stringu będzie podtrzymywał połączenia (pingował) bazę, aby do tego nie doszło


Debugging
----------
* Debugowanie połączeń .statement
* Profiling zapytań do bazy danych
* Zmiana SQLAlchemy opcji DEBUG aby wyświetlał zapytania SQL


Migracje
--------
* forward
* wycofywanie
* backward and forward compatible
* większość developerów, którzy nie używają Django korzysta z Alembic
* Przy dodawaniu tabelki oamiętać aby dodać model SQLAlchemy po napisaniu migracji
* Przy dodawaniu kolumny pamiętać aby zmienić model
* Skrypty migracyjne powinny zawsze działać, nawet kilka lat w przód, z tego powodu nie powinny bazować na innych modelach, bo one mogą ulec zmianie. Rozwiązaniem jest definiowanie modeli wewnątrz migracji


Zadania
-------
* zamodelować profil użytkownika
* dodać walidację haseł
* dodać walidację email
* automatycznie zmiana pola czy_pelnoletni
* soft-delete (bez kasowania danych)


Lazy loading
------------
* zaletą lazy loading jest to, że nie musi pobierać wszystkich danych natychmiast
* wadą jest to, że wykonuje zapytania w ostatnim momencie, np. jeżeli wyciągamy grupę, to wyciąga tylko informacje o tym obiekcie, a nie o uczestnikach. Natomiast jak wyświetlamy informacje o userach, to wykonuje query dla każdego z nich (a membersów może być np. 100)
* joinedload pozwala na fetch_related, aby za pomocą jednego query wyciągnąć wszystkie dane natychmiast


Problemy
--------
* Problem z Unexpected Query Generation
