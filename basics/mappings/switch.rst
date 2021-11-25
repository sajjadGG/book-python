Mapping Switch
==============

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['French'])


Rationale
---------
* No ``switch`` statement in Python!
* ``switch`` in Object Oriented Programming is considered a bad practise
* :pep:`275` -- Switching on Multiple Values [Rejected]
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial


Example
-------
>>> hello = {
...    'English': 'Hello',
...    'Russian': 'Здравствуйте',
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
>>>
>>> hello.get('Russian')
'Здравствуйте'


Dict Switch
-----------
>>> hello = {
...     'English': 'Hello',
...     'Russian': 'Здравствуйте',
...     'German': 'Guten Tag',
...     'Polish': 'Witaj',
...     'default': "I don't speak this language",
... }
>>>
>>>
>>> language = input('What is your language?: ')  # User input: 'French'
>>> result = hello.get(language, hello['default'])
>>>
>>> print(result)
I don't speak this language


Function Switch
---------------
>>> def hello(language):
...     data = {
...         'English': 'Hello',
...         'Russian': 'Здравствуйте',
...         'German': 'Guten Tag',
...         'Polish': 'Witaj',
...         'default': "I don't speak this language"}
...     return data.get(language, data['default'])
>>>
>>>
>>> hello('Russian')
'Здравствуйте'
>>>
>>> hello('French')
"I don't speak this language"


Assignments
-----------
.. literalinclude:: assignments/mapping_switch_a.py
    :caption: :download:`Solution <assignments/mapping_switch_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_switch_b.py
    :caption: :download:`Solution <assignments/mapping_switch_b.py>`
    :end-before: # Solution
