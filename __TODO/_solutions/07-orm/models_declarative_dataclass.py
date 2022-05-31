from dataclasses import KW_ONLY, dataclass, field
from datetime import date, datetime
from typing import Literal
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date, DateTime, Enum
from sqlalchemy.orm import registry


engine = create_engine('sqlite:///tmp2.db')
DatabaseModel = registry()


@DatabaseModel.mapped
@dataclass
class User:
    __tablename__ = 'user'
    __sa_dataclass_metadata_key__ = 'db'
    _: KW_ONLY

    # Atrybuty systemowe
    id: int = field(init=False, metadata={'db': Column(Integer, primary_key=True)})
    created: datetime = field(default_factory=datetime.now, init=False, metadata={'db': Column(DateTime)})
    modified: datetime = field(default_factory=datetime.now, init=False, metadata={'db': Column(DateTime)})

    # Atrybuty biometryczne
    firstname: str = field(metadata={'db': Column(String(50), nullable=False)})
    lastname: str = field(metadata={'db': Column(String(50), nullable=False, index=True)})
    born: date | None = field(default=None, metadata={'db': Column(Date, nullable=True)})
    gender: Literal['male','female'] | None = field(default=None, metadata={'db': Column(Enum('male', 'female'), nullable=True)})

    # Atrybuty kontaktu
    email: str | None = field(default=None, metadata={'db':  Column(String(50), nullable=True, unique=True)})
    phone: str | None = field(default=None, metadata={'db': Column(String(50), nullable=True)})


with engine.connect() as db:
    DatabaseModel.metadata.create_all(db)
