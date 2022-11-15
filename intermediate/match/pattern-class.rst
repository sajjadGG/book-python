Match Pattern Class
===================
A `class pattern` is similar to the above but matches attributes
instead of keys. It looks like ``datetime.date(year=y, day=d)``. It
matches instances of the given type, having at least the specified
attributes, as long as the attributes match with the corresponding
sub-patterns. It binds whatever the sub-patterns bind when matching
with the values of the given attributes. An optional protocol also
allows matching positional arguments.



Use Case - 0x01
---------------
>>> import json
>>> from datetime import date, time, datetime, timezone
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>>
>>> def encoder(value):
...     match value:
...         case date() | time() | datetime():
...             return value.isoformat()
...         case timedelta():
...             return value.total_seconds()
>>>
>>>
>>> json.dumps(DATA, default=encoder)
'{"firstname": "Mark", "lastname": "Watney", "born": "1994-10-12"}'
