"""
* Assignment: Model Data PetstoreNested
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. You received input data in JSON format from the API
    2. Using `dataclass` model `DATA` to create class `Pet`
       a. Leave `category` as `dict`
       b. Leave `tags` as `list[dicts]`
    3. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any Python standard library module
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use 3rd party modules
    4. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
    2. Wykorzystując `dataclass` zamodeluj `DATA` aby stwórzyć klasę `Pet`
       a. Pozostaw `category` jako `dict`
       b. Pozostaw `tags` jako `list[dicts]`
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
    Pet(id=0, category={'id': 0, 'name': 'dogs'}, name='doggie',
        photoUrls=['img/dogs/0.png'], tags=[{'id': 0, 'name': 'dog'},
                                            {'id': 1, 'name': 'hot-dog'}],
        status='available')
"""

from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship


DATA = """
{
  "id": 0,
  "category": {
    "id": 0,
    "name": "dogs"
  },
  "name": "doggie",
  "photoUrls": [
    "img/dogs/0.png"
  ],
  "tags": [
    {
      "id": 0,
      "name": "dog"
    },
    {
      "id": 1,
      "name": "hot-dog"
    }
  ],
  "status": "available"
}
"""

DatabaseModel = declarative_base()

# class: Using `dataclass` model data to create class `Pet`

class Category(DatabaseModel):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    pet_id: int = Column(Integer, ForeignKey('pet.id'))


class Photo(DatabaseModel):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    pet_id: int = Column(Integer, ForeignKey('pet.id'))


class Tag(DatabaseModel):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    pet_id: int = Column(Integer, ForeignKey('pet.id'))


class Pet(DatabaseModel):
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    photoUrls: str = Column(String)
    status: str = Column(String)

    category: Category = relationship('Category', backref='pet', uselist=False)
    photos: list[Photo] = relationship('Photo', backref='pet')
    tags: list[Tag] = relationship('Tag', backref='pet')
