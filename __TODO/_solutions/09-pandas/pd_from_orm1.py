from datetime import datetime
from sqlalchemy import Interval, Time, create_engine, distinct, func, select
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import String, Integer, Date, DateTime, Enum, Float, Numeric, Boolean
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)



DATABASE = 'sqlite:///space.db'
engine = create_engine(DATABASE)
DatabaseModel = MetaData()


apollo11 = Table('apollo11', DatabaseModel,
    Column('datetime', DateTime),
    Column('date', Date),
    Column('time', Time),
    Column('met', Interval),
    Column('category', Enum('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG')),
    Column('event', String),
)

# query = (
#     select(apollo11.c.datetime, apollo11.c.category, apollo11.c.event).
#     where(apollo11.c.category == 'CRITICAL')
# )


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


with engine.connect() as db:
    df = pd.read_sql(query, engine)
    print(df)
