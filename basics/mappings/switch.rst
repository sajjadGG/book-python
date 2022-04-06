Mapping Switch
==============
* No ``switch`` statement in Python!
* ``switch`` in Object Oriented Programming is considered a bad practise
* :pep:`275` -- Switching on Multiple Values [Rejected]
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial


Example
-------
>>> hello = {
...    'English': 'Hello',
...    'German': 'Guten Tag',
...    'Polish': 'Witaj',
... }
>>>
>>>
>>> hello.get('English')
'Hello'
>>>
>>> hello.get('Polish')
'Witaj'


Dict Switch
-----------
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['French'])

>>> hello = {
...     'English': 'Hello',
...     'German': 'Guten Tag',
...     'Polish': 'Witaj',
...     'default': "I don't speak this language",
... }
>>>
>>>
>>> language = input('What is your language?: ')  #input: 'French'
>>> result = hello.get(language, hello['default'])
>>>
>>> print(result)
I don't speak this language


Function Switch
---------------
>>> def hello(language):
...     data = {
...         'English': 'Hello',
...         'German': 'Guten Tag',
...         'Polish': 'Witaj',
...         'default': "I don't speak this language"}
...     return data.get(language, data['default'])
>>>
>>>
>>> hello('Polish')
'Witaj'
>>>
>>> hello('French')
"I don't speak this language"


Use Case - 0x01
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
... }
>>>
>>> MONTHS[1]
'January'
>>>
>>> MONTHS['1']
Traceback (most recent call last):
KeyError: '1'
>>>
>>> MONTHS['01']
Traceback (most recent call last):
KeyError: '01'


Use Case - 0x02
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
... }
>>>
>>> MONTHS.get(1)
'January'
>>>
>>> MONTHS.get(13)
>>>
>>> MONTHS.get(13, 'invalid month')
'invalid month'


Use Case - 0x03
---------------
>>> MONTHS = {
...     1: 'January',
...     2: 'February',
...     3: 'March',
...     4: 'April',
...     5: 'May',
...     6: 'June',
...     7: 'July',
...     8: 'August',
...     9: 'September',
...     10: 'October',
...     11: 'November',
...     12: 'December'
... }
>>>
>>> DATE = '1961-04-12'
>>>
>>> year, month, day = DATE.split('-')
>>>
>>> year
'1961'
>>> month
'04'
>>> day
'12'
>>>
>>> MONTHS[month]
Traceback (most recent call last):
KeyError: '04'
>>>
>>> MONTHS[int(month)]
'April'


Assignments
-----------
.. literalinclude:: assignments/mapping_switch_a.py
    :caption: :download:`Solution <assignments/mapping_switch_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_switch_b.py
    :caption: :download:`Solution <assignments/mapping_switch_b.py>`
    :end-before: # Solution
