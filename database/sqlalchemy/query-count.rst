Query Count
===========


Rationale
---------
* https://docs.sqlalchemy.org/en/stable/faq/sessions.html#faq-query-deduplicating

It is important to note that the value returned by count() is not the same as
the number of ORM objects that this Query would return from a method such as
the .all() method. The Query object, when asked to return full entities, will
deduplicate entries based on primary key, meaning if the same primary key value
would appear in the results more than once, only one object of that primary key
would be present. This does not apply to a query that is against individual
columns.


Count
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.count


Use Case - 0x01
---------------
Count User records, without sing a subquery

>>> from sqlalchemy import func
>>>
>>>
>>> session.query(func.count(User.id))


Use Case - 0x02
---------------
Return count of user 'id' grouped by 'name'

>>> from sqlalchemy import func
>>>
>>>
>>> session.query(func.count(User.id)).\
...         group_by(User.name)


Use Case - 0x02
---------------
Count distinct 'name' values

>>> from sqlalchemy import func
>>> from sqlalchemy import distinct
>>>
>>>
>>> session.query(func.count(distinct(User.name)))
