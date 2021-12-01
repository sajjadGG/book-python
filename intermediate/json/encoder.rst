JSON Encoder
============


Rationale
---------
* Problem with ``date``, ``datetime``, ``time``, ``timedelta``
* Exception during encoding datetime
* Encoder will be used, when standard procedure fails

>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>> result = json.dumps(DATA)
Traceback (most recent call last):
TypeError: Object of type date is not JSON serializable


Monkey Patching Lambda Expression
---------------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>> json.JSONEncoder.default = lambda self,x: x.isoformat()
>>> result = json.dumps(DATA)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney", "born": "1994-10-12"}


Monkey Patching Function
------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>>
>>> def encoder(self, x):
...     return x.isoformat()
>>>
>>> json.JSONEncoder.default = encoder
>>> result = json.dumps(DATA)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney", "born": "1994-10-12"}


Content Dependency Injection
----------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'born': date(1994, 10, 12)}
>>>
>>>
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, x):
...         return x.strftime('%Y-%m-%d')
>>>
>>>
>>> result = json.dumps(DATA, cls=MyEncoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{"firstname": "Mark",
 "lastname": "Watney",
 "born": "1994-10-12"}


Use Case - 0x01
---------------
>>> from datetime import date, time, datetime, timedelta
>>> import json
>>>
>>>
>>> DATA = {'name': 'Mark Watney',
...         'born': date(1994, 10, 12),
...         'launch': datetime(1969, 7, 21, 2, 56, 15),
...         'landing': time(12, 30),
...         'duration': timedelta(days=13)}
>>>
>>>
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, value):
...         if type(value) in (datetime, date, time):
...             return value.isoformat()
...         if type(value) is timedelta:
...             return value.days
>>>
>>>
>>> result = json.dumps(DATA, cls=MyEncoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{"name": "Mark Watney",
 "born": "1994-10-12",
 "launch": "1969-07-21T02:56:15",
 "landing": "12:30:00",
 "duration": 13}


Assignments
-----------
.. literalinclude:: assignments/json_encoder_a.py
    :caption: :download:`Solution <assignments/json_encoder_a.py>`
    :end-before: # Solution
