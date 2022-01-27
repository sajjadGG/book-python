#%%md
# Program szkolenia
# -----------------
# Wprowadzenie do systemów ORM
# - Założenia projektowe baz danych i optymalizacja przechowywania informacji
# - Typy normalizacji baz danych
# - Dobre praktyki projektowe
#
# Modelowanie danych – SQLAlchemy:
# - Tworzenie lokalnej bazy danych
# - Tworzenie kluczy głównych i pomocniczych
# - Tworzenie prostych tablic
#
# Tworzenie relacyjnych tablic:
# a) 1 do 1
# b) 1 do ∞
# c) ∞ do ∞
#
# Operacje:
# - Usuwanie tablic
# - Zmiana schematu relacji tabel
# - Migracje
# - Przywracanie poprzedniej wersji bazy danych
#
# Interakcja z bazą danych:
# - Odczytywanie danych z tablic relacyjnych i nierelacyjnych
# - Edycja poszczególnych wartości/rekordów
# - Tworzenie zapytań z relacjami
# - Tworzenie podzapytań
# - Przekazywanie odpowiedzi zapytań do tablic pandas dataframe
#
# Funkcje i analiza:
# - Wykorzystanie podstawowych funkcji matematycznych dla wyselekcjonowanego zbioru danych
# - Funkcje generujące wykresy i statystyki
# - Wykorzystanie przypisanych funkcji pythona zdeterminowanych przez użytkownika


#%%md
# Queries
# -------
# * Q i F (analogia do Django)
# * Regexp
# * Full text search
# * Szukanie dat
# * Typy rezultatów
# * Agregacje
# * Current Timestamp
# * Current Date
# * Convert to Date, time, timestamp
# * Timezone support UTC
#
# Nomenklatura
# ------------
# * ix - index
# * uq - unique
# * ck - check constraints
# * fk - foreign key
# * pk - primary key
#
#
# Validation
# ----------
# * Validation for models
# * SQLAlchemy validation is before it save data to database
# * Unique constraints (unique together)
#
# Indeksy
# -------
# * Functional/Expression Indexing
# ann = {'references': []}
# reply1 = {'references': [ann]}
# reply2 = {'references': [ann, reply1]}
#
# Sesje
# -----
# * pozwalają na dodawanie rzeczy do bazy
# * na koniec commit
# * context manager with session
# * session scoping
# * in a web application, a session should follow the lifecycle of a request
#
# Connection Pools
# ----------------
# * opening new connection is slow
# * używane do nieubijania sesji po zakończeniu obsługiwania połączenia
# * po obsłudze requestu połączenie wraca do puli
# * parametr pool_size oraz max_overflow (o ile połączeń może pula przekroczyć)
# * timeout jest w sekundach
# * use_lifo - jeżeli True, to ostatnie połączenie które zostało zwrócone do puli będzie pierwszym oddanym przy nowym żądaniu (najstarsze połączenia są głodzone i giną)
# * znany problem, jeżeli od jakiegoś czasu nie dostaliśmy połączenia, to wszyskie połączenia w puli nam umrą i pierwszy request będzie długi
# * keepalive przy jdbc stringu będzie podtrzymywał połączenia (pingował) bazę, aby do tego nie doszło
#
# Debugging
# ----------
# * Debugowanie połączeń .statement
# * Profiling zapytań do bazy danych
# * Zmiana SQLAlchemy opcji DEBUG aby wyświetlał zapytania SQL
#
# Migracje
# --------
# * forward
# * wycofywanie
# * backward and forward compatible
# * większość developerów, którzy nie używają Django korzysta z Alembic
# * Przy dodawaniu tabelki oamiętać aby dodać model SQLAlchemy po napisaniu migracji
# * Przy dodawaniu kolumny pamiętać aby zmienić model
# * Skrypty migracyjne powinny zawsze działać, nawet kilka lat w przód, z tego powodu nie powinny bazować na innych modelach, bo one mogą ulec zmianie. Rozwiązaniem jest definiowanie modeli wewnątrz migracji
#
# Zadania
# -------
# * zamodelować profil użytkownika
# * dodać walidację haseł
# * dodać walidację email
# * automatycznie zmiana pola czy_pelnoletni
# * soft-delete (bez kasowania danych)
#
# Lazy loading
# ------------
# * zaletą lazy loading jest to, że nie musi pobierać wszystkich danych natychmiast
# * wadą jest to, że wykonuje zapytania w ostatnim momencie, np. jeżeli wyciągamy grupę, to wyciąga tylko informacje o tym obiekcie, a nie o uczestnikach. Natomiast jak wyświetlamy informacje o userach, to wykonuje query dla każdego z nich (a membersów może być np. 100)
# * joinedload pozwala na fetch_related, aby za pomocą jednego query wyciągnąć wszystkie dane natychmiast
#
# Problemy
# --------
# * Problem z Unexpected Query Generation

# %%

from sqlalchemy import create_engine, text
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE = 'sqlite:///:memory:'

engine = create_engine(DATABASE, future=True)
Model = declarative_base()


class User(Model):
    __tablename__ = 'users'
    uid = Column(Integer, autoincrement=True, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Model.metadata.create_all(engine)


with sessionmaker(engine).begin() as session:
    session.add_all([
        User('Mark', 'Watney'),
        User('Melissa', 'Lewis'),
        User('Rick', 'Martinez'),
        User('Alex', 'Vogel'),
        User('Beth', 'Johanssen'),
        User('Chris', 'Beck'),
    ])

with engine.begin() as db:
    result = db.execute(text('SELECT * FROM users'))
    for row in result.all():
        print(row)


#%%
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric, Enum


DATABASE = 'sqlite:///:memory:'
engine = create_engine(DATABASE)
metadata = MetaData()

astronaut = Table('astronaut', metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(50), nullable=False),
    Column('lastname', String(50), nullable=False),
    Column('born', DateTime),
    Column('height', Integer),
    Column('weight', Numeric(3,2)),
    Column('agency', Enum('NASA', 'ESA', 'Roscosmos')),
)


with engine.begin() as db:
    astronaut.create(db)
