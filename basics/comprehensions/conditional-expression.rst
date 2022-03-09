Comprehension Conditionals
==========================


Syntax
------
>>> result = ['even' if x % 2 == 0 else 'odd'
...           for x in range(0,10)]
>>> result
['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

>>> result = ['even' if x % 2 == 0 else 'odd'
...           for x in range(0,10)
...           if x % 3 == 0]
>>> result
['even', 'odd', 'even', 'odd']


.. todo:: Assignments
