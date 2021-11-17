Block Match
===========

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(return_value=['French'])


Rationale
---------
* No ``switch`` statement in Python!
* ``switch`` in Object Oriented Programming is considered a bad practise
* :pep:`275` -- Switching on Multiple Values [Rejected]


Dict Switch
-----------
>>> switch = {
...     'English': 'Hello',
...     'Russian': 'Здравствуйте',
...     'German': 'Guten Tag',
...     'Polish': 'Witaj',
...     'default': "I don't speak this language"}
>>>
>>>
>>> language = input('What is your language?: ')  # User input: 'French'
>>>
>>> switch.get(language, switch['default'])
"I don't speak this language"


Function Switch
---------------
>>> def switch(language):
...     data = {
...         'English': 'Hello',
...         'Russian': 'Здравствуйте',
...         'German': 'Guten Tag',
...         'Polish': 'Witaj',
...         'default': "I don't speak this language"}
...     return data.get(language, data['default'])
>>>
>>>
>>> switch('Russian')
'Здравствуйте'
>>>
>>> switch('French')
"I don't speak this language"


Assignments
-----------
.. todo:: Create assignments
