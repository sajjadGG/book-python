Operacje
========
* insert
* update
* select
* delete



SetUp
-----
Create engine:

>>> engine = create_engine('sqlite:///tmp1.db')


Debugging
---------
>>> def print_query(query, comment):
...     compiled = query_insert.compile(engine, compile_kwargs={'literal_binds': True})
...     print(compiled)


Create Table
------------
Create database schema (tables):

>>> with engine.connect() as db:
...     Model.create_all(db)


Insert data
-----------
>>> query = (
...     insert(product).
...     values(ean13=1234567890123,
...            name='Alfa',
...            price=123.50))
>>>
>>> with engine.connect() as db:
...     db.execute(query)

>>> print_query(query)


Update data
-----------
>>> query = (
...     update(product).
...     values(name='Bravo').
...     where(product.c.id==1))
>>>
>>> with engine.connect() as db:
...     db.execute(query)

>>> print_query(query)


Select data
-----------
>>> query = (
...     select(product.c.ean13, product.c.name).
...     where(product.c.name == 'Alfa'))
>>>
>>> with engine.connect() as db:
...     db.execute(query)

>>> print_query(query)


Delete data
-----------
>>> query_delete = (
...     delete(product).
...     where(product.c.id==1))
>>>
>>> with engine.connect() as db:
...     db.execute(query)

>>> print_query(query)


Case Study
----------
>>> important_categories = (
...     select(distinct(apollo11.c.category)).
...     group_by(apollo11.c.category).
...     having(func.count(apollo11.c.category) < 50).
...     order_by(apollo11.c.category.asc()).
...     limit(5).
...     offset(0)
... ).cte('important_categories')
>>>
>>> query = (
...     select(apollo11.c.datetime.label('dt'),
...            apollo11.c.category,
...            apollo11.c.event).
...
...     where((apollo11.c.category != 'DEBUG')
...         & (apollo11.c.date >= '1969-07-16')
...         & (apollo11.c.date <= '1969-07-24')
...         & ((apollo11.c.date == '1969-07-20') | (apollo11.c.date == '1969-07-21'))
...         & (apollo11.c.datetime.between('1969-07-20 20:17:41', '1969-07-21 15:00'))
...         & (apollo11.c.event.like('%CDR%'))
...         & (apollo11.c.category != None)
...         & (~apollo11.c.category.in_(['DEBUG', 'INFO']))
...         & (apollo11.c.category.in_(['CRITICAL', 'ERROR']))
...         & (apollo11.c.category.in_(important_categories))).
...
...     order_by(apollo11.c.category.desc(),
...              apollo11.c.date.asc().nullsfirst(),
...              apollo11.c.time.asc().nullslast()).
...
...     limit(30).
...     offset(0)
... )
>>>
>>>
>>> debug(query)
WITH important_categories AS
(SELECT DISTINCT apollo11.category AS anon_1
FROM apollo11 GROUP BY apollo11.category
HAVING count(apollo11.category) < 50 ORDER BY apollo11.category ASC
 LIMIT 5 OFFSET 0)
 SELECT apollo11.datetime AS dt, apollo11.category, apollo11.event
FROM apollo11
WHERE apollo11.category != 'DEBUG' AND apollo11.date >= '1969-07-16' AND apollo11.date <= '1969-07-24' AND (apollo11.date = '1969-07-20' OR apollo11.date = '1969-07-21') AND apollo11.datetime BETWEEN '1969-07-20 20:17:41' AND '1969-07-21 15:00' AND apollo11.event LIKE '%CDR%' AND apollo11.category IS NOT NULL AND (apollo11.category NOT IN ('DEBUG', 'INFO')) AND apollo11.category IN ('CRITICAL', 'ERROR') AND apollo11.category IN (SELECT important_categories.anon_1
FROM important_categories) ORDER BY apollo11.category DESC, apollo11.date ASC NULLS FIRST, apollo11.time ASC NULLS LAST
 LIMIT 30 OFFSET 0
