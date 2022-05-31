"""
* Assignment: Model Data PetstoreFlat
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. You received input data in JSON format from the API
    2. Using `dataclass` model data to create class `Pet`
    3. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any Python standard library module
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use 3rd party modules
    4. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
    2. Wykorzystując `dataclass` zamodeluj dane aby stwórzyć klasę `Pet`
    3. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
    4. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1]: https://petstore.swagger.io/#/pet/getPetById

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass
    >>> import json

    >>> assert isclass(Pet)
    >>> assert is_dataclass(Pet)

    >>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
    >>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
    f'Invalid fields, your fields should be: {fields}'

    >>> data = json.loads(DATA)
    >>> result = Pet(**data)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    Pet(id=0, category='dogs', name='doggie', photoUrls='img/dogs/0.png',
        tags=['dog', 'hot-dog'], status='available')
"""

from dataclasses import dataclass

DATA = """
{
  "id": 0,
  "category": "dogs",
  "name": "doggie",
  "photoUrls": "img/dogs/0.png",
  "tags": ["dog", "hot-dog"],
  "status": "available"
}
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


DatabaseModel = declarative_base()


# class: Using `dataclass` model data to create class `Pet`
class Tag(DatabaseModel):
    name: str = Column(String, primary_key=True)
    pet_id: int = Column(Integer, ForeignKey('pet.id'))
    # pet: relacja -> pet.id == tag.pet_id (pole pet zostało stworzone przez Pet.backref='pet')

class Pet(DatabaseModel):
    id: int = Column(Integer, primary_key=True)
    category: str = Column(String)
    name: str = Column(String)
    photoUrls: str = Column(String)
    status: str = Column(String)
    tags: list[Tag] = relationship('Tag', backref='pet')
