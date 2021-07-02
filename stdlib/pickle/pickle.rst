Serialization Pickle
====================


What is ``pickle``?
-------------------
* Python object serialization format
* ``pickle`` vs. ``cPickle``


Dump Str to Bytes
-----------------
>>> import pickle
>>>
>>>
>>> pickle.dumps('Mark Watney')
b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bMark Watney\x94.'


Dump Int to Bytes
-----------------
>>> import pickle
>>>
>>>
>>> pickle.dumps(1)
b'\x80\x04K\x01.'
>>>
>>> pickle.dumps(0)
b'\x80\x04K\x00.'
>>>
>>> pickle.dumps(-1)
b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00J\xff\xff\xff\xff.'


Dump Float to Bytes
-------------------
>>> import pickle
>>>
>>>
>>> pickle.dumps(1)
b'\x80\x04K\x01.'
>>>
>>> pickle.dumps(1.0)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xf0\x00\x00\x00\x00\x00\x00.'

>>> import pickle
>>>
>>>
>>> pickle.dumps(0.1)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.'
>>>
>>> pickle.dumps(0.2)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xc9\x99\x99\x99\x99\x99\x9a.'
>>>
>>> pickle.dumps(0.3)
b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xd3333333.'


Dump Sequence to Bytes
----------------------
>>> import pickle
>>>
>>>
>>> pickle.dumps([1, 2, 3])
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
>>>
>>> pickle.dumps((1, 2, 3))
b'\x80\x04\x95\t\x00\x00\x00\x00\x00\x00\x00K\x01K\x02K\x03\x87\x94.'
>>>
>>> pickle.dumps({1, 2, 3})
b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00\x8f\x94(K\x01K\x02K\x03\x90.'


Dump Mapping to Bytes
---------------------
>>> import pickle
>>>
>>>
>>> pickle.dumps({'a': 1, 'b': 2, 'c': 3})
b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94K\x01\x8c\x01b\x94K\x02\x8c\x01c\x94K\x03u.'


Load Str from Bytes
-------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bMark Watney\x94.')
'Mark Watney'


Load Int from Bytes
-------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03K\x01.')
1
>>> pickle.loads(b'\x80\x04K\x00.')
0
>>> pickle.loads(b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00J\xff\xff\xff\xff.')
-1


Load Float from Bytes
-------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.')
0.1
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xc9\x99\x99\x99\x99\x99\x9a.')
0.2
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xd3333333.')
0.3


Load Sequence from Bytes
------------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.')
[1, 2, 3]
>>>
>>> pickle.loads(b'\x80\x03K\x01K\x02K\x03\x87q\x00.')
(1, 2, 3)
>>>
>>> pickle.loads(b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.')
{1, 2, 3}
>>>


Load Mapping from Bytes
-----------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.')
{'a': 1, 'b': 2, 'c': 3}


Serialize Datetimes
-------------------
>>> import pickle
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> pickle.dumps(dt)
b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94\x85\x94R\x94.'

>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00\x94\x85\x94R\x94.')
datetime.datetime(1969, 7, 21, 2, 56, 15)


Serialize and deserialize objects
---------------------------------
>>> import pickle
>>>
>>>
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>> result = pickle.dumps(vars(astro))
>>>
>>> result
b'\x80\x04\x95,\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94u.'
>>>
>>> data = pickle.loads(result)
>>> Astronaut(**data)  # doctest: +ELLIPSIS
<__main__.Astronaut object at 0x...>


Serialize and deserialize to file
---------------------------------
* File extension ``pkl``

Dump to file:

>>> import pickle
>>>
>>>
>>> DATA = [1, 2, 3]
>>>
>>> with open('filename.pkl', mode='wb') as file:
...     pickle.dump(DATA, file)

Load from file:

>>> import pickle
>>>
>>>
>>> with open('filename.pkl', mode='rb') as file:
...     result = pickle.load(file)
>>>
>>> print(result)
[1, 2, 3]


Examples
--------
Advanced Example:

>>> from datetime import date, datetime
>>> import pickle
>>>
>>>
>>> DATA = {'mission': 'Ares 3',
...         'launch_date': datetime(2035, 6, 29),
...         'destination': 'Mars',
...         'destination_landing': datetime(2035, 11, 7),
...         'destination_location': 'Acidalia Planitia',
...         'crew': [{'name': 'Melissa Lewis', 'born': date(1995, 7, 15)},
...                  {'name': 'Rick Martinez', 'born': date(1996, 1, 21)},
...                  {'name': 'Alex Vogel', 'born': date(1994, 11, 15)},
...                  {'name': 'Chris Beck', 'born': date(1999, 8, 2)},
...                  {'name': 'Beth Johansen', 'born': date(2006, 5, 9)},
...                  {'name': 'Mark Watney', 'born': date(1994, 10, 12)}]}
>>>
>>>
>>> result = pickle.dumps(DATA)
>>> print(result)
b'\x80\x04\x95\xac\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x07mission\x94\x8c\x06Ares 3\x94\x8c\x0blaunch_date\x94\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xf3\x06\x1d\x00\x00\x00\x00\x00\x00\x94\x85\x94R\x94\x8c\x0bdestination\x94\x8c\x04Mars\x94\x8c\x13destination_landing\x94h\x06C\n\x07\xf3\x0b\x07\x00\x00\x00\x00\x00\x00\x94\x85\x94R\x94\x8c\x14destination_location\x94\x8c\x11Acidalia Planitia\x94\x8c\x04crew\x94]\x94(}\x94(\x8c\x04name\x94\x8c\rMelissa Lewis\x94\x8c\x04born\x94h\x04\x8c\x04date\x94\x93\x94C\x04\x07\xcb\x07\x0f\x94\x85\x94R\x94u}\x94(h\x15\x8c\rRick Martinez\x94h\x17h\x19C\x04\x07\xcc\x01\x15\x94\x85\x94R\x94u}\x94(h\x15\x8c\nAlex Vogel\x94h\x17h\x19C\x04\x07\xca\x0b\x0f\x94\x85\x94R\x94u}\x94(h\x15\x8c\nChris Beck\x94h\x17h\x19C\x04\x07\xcf\x08\x02\x94\x85\x94R\x94u}\x94(h\x15\x8c\rBeth Johansen\x94h\x17h\x19C\x04\x07\xd6\x05\t\x94\x85\x94R\x94u}\x94(h\x15\x8c\x0bMark Watney\x94h\x17h\x19C\x04\x07\xca\n\x0c\x94\x85\x94R\x94ueu.'
>>>
>>> result = pickle.loads(result)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
{'mission': 'Ares 3',
 'launch_date': datetime.datetime(2035, 6, 29, 0, 0),
 'destination': 'Mars',
 'destination_landing': datetime.datetime(2035, 11, 7, 0, 0),
 'destination_location': 'Acidalia Planitia',
 'crew': [{'name': 'Melissa Lewis', 'born': datetime.date(1995, 7, 15)},
          {'name': 'Rick Martinez', 'born': datetime.date(1996, 1, 21)},
          {'name': 'Alex Vogel', 'born': datetime.date(1994, 11, 15)},
          {'name': 'Chris Beck', 'born': datetime.date(1999, 8, 2)},
          {'name': 'Beth Johansen', 'born': datetime.date(2006, 5, 9)},
          {'name': 'Mark Watney', 'born': datetime.date(1994, 10, 12)}]}


Assignments
-----------
.. literalinclude:: assignments/serialization_pickle_a.py
    :caption: :download:`Solution <assignments/serialization_pickle_a.py>`
    :end-before: # Solution
