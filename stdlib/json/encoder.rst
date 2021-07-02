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
>>>         'lastname': 'Watney',
>>>         'date_of_birth': date(1994, 10, 12)}
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
>>>         'lastname': 'Watney',
>>>         'date_of_birth': date(1994, 10, 12)}
>>>
>>> json.JSONEncoder.default = lambda self,x: x.isoformat()
>>> result = json.dumps(DATA)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney", "date_of_birth": "1994-10-12"}


Monkey Patching Function
------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'date_of_birth': date(1994, 10, 12)}
>>>
>>>
>>> def encoder(self, x):
...     return x.isoformat()
>>>
>>> json.JSONEncoder.default = encoder
>>> result = json.dumps(DATA)
>>>
>>> print(result)
{"firstname": "Mark", "lastname": "Watney", "date_of_birth": "1994-10-12"}


Content Dependency Injection
----------------------------
>>> from datetime import date
>>> import json
>>>
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'date_of_birth': date(1994, 10, 12)}
>>>
>>>
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, x):
...         return x.strftime('%Y-%m-%d')
>>>
>>>
>>> result = json.dumps(DATA, cls=MyEncoder)
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
{"firstname": "Mark",
 "lastname": "Watney",
 "date_of_birth": "1994-10-12",
 "first_mission": "1969-07-21T02:56:15.000000+00:00"}


Use Case
--------
>>> from datetime import date, time, datetime, timedelta
>>> import json
>>>
>>>
>>> YEAR = 365
>>>
>>> DATA = {'firstname': 'Mark',
...         'lastname': 'Watney',
...         'date_of_birth': date(1994, 10, 12),
...         'first_mission': datetime(1969, 7, 21, 2, 56, 15),
...         'nap_time': time(12, 30, 0),
...         'age': timedelta(days=44*YEAR)}
>>>
>>>
>>> class MyEncoder(json.JSONEncoder):
...     def default(self, value):
...         if type(value) in (datetime, date, time):
...             return value.isoformat()
...         if type(value) is timedelta:
...             return value.days // YEAR
>>>
>>>
>>> result = json.dumps(DATA, cls=MyEncoder)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{"firstname": "Mark",
 "lastname": "Watney",
 "date_of_birth": "1994-10-12",
 "first_mission": "1969-07-21T02:56:15",
 "nap_time": "12:30:00",
 "age": 44}


Assignments
-----------
.. literalinclude:: assignments/json_encoder_a.py
    :caption: :download:`Solution <assignments/json_encoder_a.py>`
    :end-before: # Solution
