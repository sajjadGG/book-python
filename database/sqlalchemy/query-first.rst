Query First
===========


Rationale
---------


First
-----
* https://docs.sqlalchemy.org/en/stable/orm/query.html#sqlalchemy.orm.Query.first

>>> results = Valuation.query.filter_by(..).order_by(sqlalchemy.desc(Valuation.date)).first()


Last
----
* No last method

>>> results = Valuation.query.filter_by(..).order_by(sqlalchemy.desc(Valuation.date)).all()
>>> first_valuation = results[0]
>>> last_valuation = results[-1]


Where
-----


>>> shrew = Animal(u'shrew')
>>> shrew[u'cuteness'] = 5
>>> shrew[u'weasel-like'] = False
>>> shrew[u'poisonous'] = True
>>>
>>> session.add(shrew)
>>> session.flush()
>>>
>>> q = (session.query(Animal).
...      filter(Animal.facts.any(
...        and_(AnimalFact.key == u'weasel-like',
...             AnimalFact.value == True))))
>>> print('weasel-like animals', q.all())
