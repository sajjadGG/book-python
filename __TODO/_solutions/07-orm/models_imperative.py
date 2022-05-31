from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import String, Integer, Date, DateTime, Enum, Float, Numeric, Boolean


DatabaseModel = MetaData()


User = Table('user', DatabaseModel,

     # pola systemowe i diagnostyczne
     Column('id', Integer, primary_key=True),
     Column('created', DateTime, default=datetime.now),
     Column('modified', DateTime, default=datetime.now),

     # pola biometryczne
     Column('firstname', String(length=50), nullable=False),
     Column('lastname', String(length=50), nullable=False, index=True),
     Column('gender', Enum('male', 'female')),
     Column('born', Date),
     Column('is_adult', Boolean),
     Column('height', Numeric(3,1)),
     Column('weight', Numeric(3,1)),

     # pola kontaktu
     Column('email', String(length=100), unique=True),
)



# wprowadzanie zmian do bazy danych
engine = create_engine('sqlite:///tmp.db', future=True)

with engine.connect() as db:
    DatabaseModel.create_all(db)
