Serialization Pickle
====================


What is ``pickle``?
-------------------
* Python object serialization format
* ``pickle`` vs. ``cPickle``


Dump to string
--------------
>>> import pickle
>>>
>>>
>>> pickle.dumps('Jan Twardowski')
b'\x80\x03X\x0e\x00\x00\x00Jan Twardowskiq\x00.'
>>>
>>> pickle.dumps(1)
b'\x80\x03K\x01.'
>>>
>>> pickle.dumps(1.0)
b'\x80\x03G?\xf0\x00\x00\x00\x00\x00\x00.'
>>>
>>> pickle.dumps(1.2)
b'\x80\x03G?\xf3333333.'
>>>
>>> pickle.dumps(1.5)
b'\x80\x03G?\xf8\x00\x00\x00\x00\x00\x00.'


Load from string
----------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03X\x0e\x00\x00\x00Jan Twardowskiq\x00.')
'Jan Twardowski'
>>>
>>> pickle.loads(b'\x80\x03K\x01.')
1
>>>
>>> pickle.loads(b'\x80\x03G?\xf0\x00\x00\x00\x00\x00\x00.')
1.0
>>>
>>> pickle.loads(b'\x80\x03G?\xf3333333.')
1.2
>>>
>>> pickle.loads(b'\x80\x03G?\xf8\x00\x00\x00\x00\x00\x00.')
1.5


Dump to string
--------------
>>> import pickle
>>>
>>>
>>> pickle.dumps([1, 2, 3])
b'\x80\x03]q\x00(K\x01K\x02K\x03e.
>>>
>>> pickle.dumps((1, 2, 3))
b'\x80\x03K\x01K\x02K\x03\x87q\x00.'
>>>
>>> pickle.dumps({1, 2, 3})
b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.'
>>>
>>> pickle.dumps({'a': 1, 'b': 2, 'c': 3})
b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.'


Load from string
----------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.)
[1, 2, 3]
>>>
>>> pickle.loads(b'\x80\x03K\x01K\x02K\x03\x87q\x00.')
(1, 2, 3)
>>>
>>> pickle.loads(b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.')
{1, 2, 3}
>>>
>>> pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.')
{'a': 1, 'b': 2, 'c': 3}


Serialize Dates and Datetimes
-----------------------------
>>> import pickle
>>>
>>>
>>> dt = datetime(1969, 7, 21, 2, 56, 15)
>>> pickle.dumps(dt)
b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00q\x01\x85q\x02Rq\x03.'

>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xb1\x07\x15\x028\x0f\x00\x00\x00q\x01\x85q\x02Rq\x03.')
datetime.datetime(1969, 7, 21, 2, 56, 15)


Serialize and deserialize objects
---------------------------------
>>> import pickle
>>>
>>>
>>> class Astronaut:
>>>     def __init__(self, firstname, lastname):
>>>         self.firstname = firstname
>>>         self.lastname = lastname
>>>
>>> jan = Astronaut('Jan', 'Twardowski')
>>>
>>> pickle.dumps(jan)
b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06ub.'
>>>
>>> pickle.loads(b'\x80\x03c__main__\nAstronaut\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00firstnameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00lastnameq\x05X\n\x00\x00\x00Twardowskiq\x06ub.')  # doctest: +ELLIPSIS
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
