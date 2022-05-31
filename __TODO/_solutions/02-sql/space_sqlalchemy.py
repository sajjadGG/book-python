from sqlalchemy import Table, Column, MetaData, select
from sqlalchemy import String, Enum, Integer, Time, Date, DateTime
from sqlalchemy import create_engine
from sqlalchemy import select, distinct, func

DATABASE = 'sqlite:///space.db'
engine = create_engine(DATABASE)


def debug(query):
    compiled = query.compile(engine, compile_kwargs={'literal_binds': True})
    print(compiled)



# CREATE TABLE IF NOT EXISTS "apollo11" (
#   "datetime" TIMESTAMP,
#   "date" DATE,
#   "time" TIME,
#   "met" INTEGER,
#   "category" TEXT,
#   "event" TEXT
# );


Model = MetaData()

# CATEGORIES = Enum('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG')

apollo11 = Table('apollo11', Model,
    Column('id', Integer, primary_key=True),
    Column('datetime', DateTime),
    Column('date', Date),
    Column('time', Time),
    Column('met', Integer, comment='Mission Elapsed Time'),
    Column('category', Enum('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG')),
    Column('event', String(255)),
)

"""
# CHAR(5) - zawsze stała długość, char jest szybszy, marnuje trochę miejsca
# is_adult: Char(1) -> T, F => Boolean -> 0,1
# VARCHAR(255) - zajmuje tyle ile ma tekst, ale nie więcej niż 255
# Najdłuższy VARCHAR ma 255 znaków
# Nie dotyczy to SQLite3, gdzie zarówno CHAR jak i VARCHAR to tylko alias do TEXT o nieskończonej długości

#  12345
#  -----
# '  abc'  # char(5)
# 'abc'    # varchar(255)

Standardowo wiele where jest łączone za pomocą AND

# select(...).
# where(...).
# where(...).
# where(...)

Za pomocą funkcji ``and_()``:

select().
where(and_(
    ...,
    ...,
    ...,
))

Za pomocą operatora ``&``:

select().
where(...
    & ...
    & ...
    & ...
))

W SQLAlchemy zamiast is NULL robi się != None

"""

important_categories = (
    select(distinct(apollo11.c.category)).
    group_by(apollo11.c.category).
    having(func.count(apollo11.c.category) < 50).
    order_by(apollo11.c.category.asc()).
    limit(5).
    offset(0)
).cte('important_categories')

query = (
    select(apollo11.c.datetime.label('dt'),
           apollo11.c.category,
           apollo11.c.event).

    where((apollo11.c.category != 'DEBUG')
        & (apollo11.c.date >= '1969-07-16')
        & (apollo11.c.date <= '1969-07-24')
        & ((apollo11.c.date == '1969-07-20') | (apollo11.c.date == '1969-07-21'))
        & (apollo11.c.datetime.between('1969-07-20 20:17:41', '1969-07-21 15:00'))
        & (apollo11.c.event.like('%CDR%'))
        & (apollo11.c.category != None)
        & (~apollo11.c.category.in_(['DEBUG', 'INFO']))
        & (apollo11.c.category.in_(['CRITICAL', 'ERROR']))
        & (apollo11.c.category.in_(important_categories))).

    order_by(apollo11.c.category.desc(),
             apollo11.c.date.asc().nullsfirst(),
             apollo11.c.time.asc().nullslast()).

    limit(30).
    offset(0)
)


debug(query)


print('\n'*3)

with engine.connect() as db:
    for row in db.execute(query).all():
        print(row)

print('\n'*3)
