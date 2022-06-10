ORM
===


Rationale
---------
* są dwa sposoby pracy z SQLAlchemy
* Database first approach
* Python class first approach


DB First Approach
-----------------
* Najpierw projektujemy bazę danych
* Najczęściej modele przestawiamy jako ERD
* Z tego generujemy scheme
* Generalnie bardziej rozbudowane (płatne) narzędzia do ERD mają eksport do SQL (CREATE TABLE statements)
* Jak zaprojektujemy bazę danych, to musimy w naszym kodzie ją odwzorować tworząc obiekt ``Table``, który posiada ``MetaData`` oraz zestaw ``Column``.
* Tu najpierw zmienia się schemat bazy danych
* później musimy pamiętać, aby to odwzorować w kodzie
* Problem się pojawia jak przeoczymy zmianę
* Można używać narzędzia dodatkowe, jak również generowanie klas Pythona na podstawie bazy danych (inspectdb w Django, w SQLAlchemy też jest odpowiednik do tego)
* problem jest w tym, że jeżeli nowa wygenerowana klasa jest niekompatybilna wstecznie, to musimy refactorować cały kod

>>> from datetime import datetime
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Table, Column, MetaData
>>> from sqlalchemy import String, Integer, Date, DateTime, Enum, Numeric, Boolean
>>>
>>>
>>> DatabaseModel = MetaData()
>>>
>>>
>>> User = Table('user', DatabaseModel,
...
...      # pola systemowe i diagnostyczne
...      Column('id', Integer, primary_key=True),
...      Column('created', DateTime, default=datetime.now),
...      Column('modified', DateTime, default=datetime.now),
...
...      # pola biometryczne
...      Column('firstname', String(length=50), nullable=False),
...      Column('lastname', String(length=50), nullable=False, index=True),
...      Column('gender', Enum('male', 'female')),
...      Column('born', Date),
...      Column('is_adult', Boolean),
...      Column('height', Numeric(3,1)),
...      Column('weight', Numeric(3,1)),
...
...      # pola kontaktu
...      Column('email', String(length=100), unique=True),
... )


Python Class First Approach
---------------------------
* ORM
* Najpierw definiujemy klasę w Python
* Dopiero później każemy frameworkowi stworzyć bazę danych na podstawie modeli
* Można używać narzędzi do migracji schematu bazy danych
* Narzędzia chociaż coraz lepsze, to nie zawsze dają same radę


ORM
---
* SQLAlchemy automatycznie generuje nam ``__init__()``
* ``__init__()`` przyjmuje tylko parametry keywordowe
* nie obsługuje pozycyjnych
* dobra praktyka zdefiniować ``__repr__()``


Create Models
-------------
* You should use engine.begin() for create_all

Add
---

    # Alternatywnie dodajemy do bazy danych za pomocą add_all
    # db.add_all([
    #     ares1,
    #     ares3,
    #     mark,
    # ])

    # Alternatywnie dodajemy do bazy danych za pomocą add_all objektów anonimowych
    # db.add_all([
    #     Mission(year=2031, name='Ares1'),
    #     Mission(year=2035, name='Ares3'),
    #     Astronaut(firstname='Mark', lastname='Watney'),
    # ])


    # Dodajemy do bazy danych za pomocą add
    db.add(ares1)
    db.add(ares3)
    db.add(mark)


Query
-----
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_URL
from models import Astronaut, Mission


engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)


query = select(Astronaut)


with session.begin() as db:
    result = db.execute(query)

    for astro in result.scalars():
        fullname = f'{astro.firstname}, {astro.lastname}'
        mission = astro.missions.name
        print(f'{fullname} -> {mission}')


# https://stackoverflow.com/questions/51335298/concepts-of-backref-and-back-populate-in-sqlalchemy


class Email(HabitatModel, MissionDate, MissionTime):
    STATUS_READ = 'read'
    STATUS_UNREAD = 'unread'
    STATUS_ARCHIVED = 'archived'
    STATUS_CHOICES = [
        (STATUS_READ, _('Read')),
        (STATUS_UNREAD, _('Unread'))]

    PRIORITY_NORMAL = 'normal'
    PRIORITY_CRITICAL = 'critical'
    PRIORITY_CHOICES = [
        (PRIORITY_NORMAL, _('Normal')),
        (PRIORITY_CRITICAL, _('Simulation is in danger (email is not time delayed!)'))]

    priority = models.CharField(verbose_name=_('Priority'), max_length=30, choices=PRIORITY_CHOICES, default=PRIORITY_NORMAL)
    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUS_CHOICES, default=STATUS_UNREAD, db_index=True)
    sender = models.ForeignKey(verbose_name=_('From'), to=settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE, db_index=True)
    recipients = models.ManyToManyField(verbose_name=_('To'), to=settings.AUTH_USER_MODEL, db_index=True, related_name='to')
    subject = models.CharField(verbose_name=_('Subject'), max_length=255, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True, null=True, default=None)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to='communication.Tag', blank=True, default=None)

    def body_as_html(self):
        return format_html(self.body)

    def __str__(self):
        return f'[{self.date} {self.time}] <{self.sender}> {self.subject}'

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')


One to One
----------
>>> class User:
...   firstname: str
...   lastname: str
...   group: Group  # relationship('Email', backref='user', uselist=False)
>>>
>>> class Group:
...     name: str
...     user_id: int  # ForeignKey('User.id')

>>> User.group.name
>>> Group.user.name  # backref will create Group.user


One to Many
-----------
>>> class User:
...   firstname: str
...   lastname: str
...   group: Group  # relationship('Email', backref='user')
>>>
>>> class Group:
...     name: str
...     user_id: int  # ForeignKey('User.id')

>>> User.group.name
>>> Group.user[0].name  # backref will create Group.user


Many to Many
------------
>>> class User:
...     firstname: str
...     lastname: str
...     groups: list[Group]  # relationship('Group', secondary='Membership')
>>>
>>>
>>> class Membership:
...     user_id: int  # ForeignKey('User.id')
...     group_id: int  # ForeignKey('Group.id')
>>>
>>>
>>> class Group:
...     name: str
...     users: list[User]  # relationship('User', secondary='Membership')
>>>
>>>
>>> User.groups[0].name
>>> Group.users[0].lastname
