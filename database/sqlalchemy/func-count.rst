Func Count
==========


Rationale
---------


Use Case - 0x01
---------------
Count User records, without sing a subquery

>>> from sqlalchemy import func
>>>
>>>
>>> session.query(func.count(User.id))


Use Case - 0x02
---------------
Return count of user "id" grouped by "name"

>>> from sqlalchemy import func
>>>
>>>
>>> session.query(func.count(User.id)).\
...         group_by(User.name)


Use Case - 0x02
---------------
Count distinct "name" values

>>> from sqlalchemy import func
>>> from sqlalchemy import distinct
>>>
>>>
>>> session.query(func.count(distinct(User.name)))
