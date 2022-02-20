SQLAlchemy Core Introspect
==========================


Rationale
---------
* Introspection - getting information about the object internals


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>> metadata = MetaData()
>>>
>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', DateTime),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'Roscosmos')),
... )
>>>
>>> with engine.begin() as db:
...     astronaut.create(db)


Inspect
-------
Define database query:

>>> query = (
...     insert(astronaut).
...     values(firstname='Mark', lastname='Watney')
... )

We can inspect database query by printing the query:

>>> print(query)
INSERT INTO astronaut (firstname, lastname) VALUES (:firstname, :lastname)


Compile
-------
If we want to get to the lower level we can:

>>> sql = query.compile()

But mind, that all databases has different syntax, hence it is good idea to
pass the database engine instance to the compile method to set SQL language
flavor:

>>> sql = query.compile(engine)

Or we can set the flavor explicitly:

>>> from sqlalchemy.dialects import postgresql
>>>
>>> sql = query.compile(dialect=postgresql.dialect())


Introspection
-------------
Compiled object will have attributes:

>>> sql = query.compile(engine)
>>>
>>> print(sql.statement)
INSERT INTO astronaut (firstname, lastname) VALUES (:firstname, :lastname)
>>>
>>> print(sql.params)
{'firstname': 'Alex', 'lastname': 'Vogel'}

However if you want to get the final version

>>> sql = query.compile(compile_kwargs={'literal_binds': True})
>>>
>>> print(sql)
INSERT INTO astronaut (firstname, lastname) VALUES ('Alex', 'Vogel')
