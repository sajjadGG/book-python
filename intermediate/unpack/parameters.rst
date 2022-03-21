Unpack Parameters
=================


Important
---------
* More information in `Unpack Assignment`
* More information in `Unpack Parameters`
* More information in `Unpack Arguments`

.. figure:: img/unpack-assignment,args,params.png


Syntax
------
>>> def myfunction(*args):
...     pass

>>> def myfunction(**kwargs):
...     pass

>>> def myfunction(*args, **kwargs):
...     pass


Recap
-----
* parameter - Receiving variable used within the function/block
* required parameters - Parameter which is necessary to call function
* optional parameters (with default value) - Parameter which is optional and has default value (if not specified at call time)

Required parameters:

>>> def echo(a, b):
...     pass

Optional parameters:

>>> def echo(a=1, b=2):
...     pass

Required and optional parameters:

>>> def echo(a, b=2):
...     pass

Required parameters must be the leftmost:

>>> def echo(a=1, b):
...     pass
Traceback (most recent call last):
SyntaxError: non-default argument follows default argument


Positional Parameters
---------------------
* ``*`` is used for positional parameters
* ``args`` is a convention, but you can use any name
* ``*args`` unpacks to ``tuple``

>>> def echo(*args):
...     print(args)
>>>
>>>
>>> echo()
()
>>>
>>> echo(1)
(1,)
>>>
>>> echo(2, 3)
(2, 3)
>>>
>>> echo(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)


Keyword Parameters
------------------
* ``**`` is used for keyword parameters
* ``kwargs`` is a convention, but you can use any name
* ``**kwargs`` unpacks to ``dict``

>>> def echo(**kwargs):
...     print(kwargs)
>>>
>>>
>>> echo()
{}
>>>
>>> echo(a=1)
{'a': 1}
>>>
>>> echo(a=1, b=2)
{'a': 1, 'b': 2}
>>>
>>> echo(a=1, b=2, c=3, d=4, e=5)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


Positional and Keyword Parameters
---------------------------------
* ``*`` is used for positional parameters
* ``**`` is used for keyword parameters
* ``*args`` unpacks to ``tuple``
* ``**kwargs`` unpacks to ``dict``

>>> def echo(*args, **kwargs):
...     print(f'{args=}, {kwargs=}')
>>>
>>>
>>> echo()
args=(), kwargs={}
>>>
>>> echo(1, 2, 3)
args=(1, 2, 3), kwargs={}
>>>
>>> echo(d=4, e=5, f=6)
args=(), kwargs={'d': 4, 'e': 5, 'f': 6}
>>>
>>> echo(1, 2, 3, d=4, e=5, f=6)
args=(1, 2, 3), kwargs={'d': 4, 'e': 5, 'f': 6}


Parameters with Args, Kwargs
----------------------------
>>> def echo(a, b, c=0, *args):
...     print(f'{a=}, {b=}, {c=}, {args=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=0, args=()
>>>
>>> echo(1, 2, 3)
a=1, b=2, c=3, args=()
>>>
>>> echo(1, 2, 3, 4)
a=1, b=2, c=3, args=(4,)
>>>
>>> echo(1, 2, 3, 4, 5, 6)
a=1, b=2, c=3, args=(4, 5, 6)

>>> def echo(a, b, c=0, **kwargs):
...     print(f'{a=}, {b=}, {c=}, {kwargs=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=0, kwargs={}
>>>
>>> echo(1, 2, 3)
a=1, b=2, c=3, kwargs={}
>>>
>>> echo(1, 2, 3, d=7, e=8, f=9)
a=1, b=2, c=3, kwargs={'d': 7, 'e': 8, 'f': 9}
>>>
>>> echo(1, 2, a=7)
Traceback (most recent call last):
TypeError: echo() got multiple values for argument 'a'

>>> def echo(a, b, c=0, *args, **kwargs):
...     print(f'{a=}, {b=}, {c=}, {args=}, {kwargs=}')
>>>
>>>
>>> echo(1, 2)
a=1, b=2, c=0, args=(), kwargs={}
>>>
>>> echo(1, 2, 3, 4, 5, 6)
a=1, b=2, c=3, args=(4, 5, 6), kwargs={}
>>>
>>> echo(1, 2, 3, d=7, e=8, f=9)
a=1, b=2, c=3, args=(), kwargs={'d': 7, 'e': 8, 'f': 9}
>>>
>>> echo(1, 2, 3, 4, 5, 6, d=7, e=8, f=9)
a=1, b=2, c=3, args=(4, 5, 6), kwargs={'d': 7, 'e': 8, 'f': 9}


Use Case - 0x01
---------------
>>> def echo(a, b, c=0, *args):
...     print(locals())
>>>
>>>
>>> echo(*range(0,10))
{'a': 0, 'b': 1, 'c': 2, 'args': (3, 4, 5, 6, 7, 8, 9)}


Use Case - 0x02
---------------
>>> def add(*values):
...     total = 0
...     for value in values:
...         total += value
...     return total
>>>
>>>
>>> add()
0
>>>
>>> add(1)
1
>>>
>>> add(1, 4)
5
>>>
>>> add(3, 1)
4
>>>
>>> add(1, 2, 3, 4)
10


Use Case - 0x03
---------------
>>> def celsius_to_kelvin(degree):
...     return degree + 273.15
>>>
>>>
>>> celsius_to_kelvin(1)
274.15
>>>
>>> celsius_to_kelvin([1,2,3])
Traceback (most recent call last):
TypeError: can only concatenate list (not "float") to list

>>> def celsius_to_kelvin(*degrees):
...     return [x+273.15 for x in degrees]
>>>
>>>
>>> celsius_to_kelvin(1)
[274.15]
>>>
>>> celsius_to_kelvin(1, 2, 3, 4, 5)
[274.15, 275.15, 276.15, 277.15, 278.15]


Use Case - 0x04
---------------
>>> def html_list(*fruits):
...     print('<ul>')
...     for fruit in fruits:
...         print(f'<li>{fruit}</li>')
...     print('</ul>')
>>>
>>>
>>> html_list('apple', 'banana', 'orange')
<ul>
<li>apple</li>
<li>banana</li>
<li>orange</li>
</ul>


Use Case - 0x05
---------------
Intuitive definition of ``print`` function:

>>> def print(*values, sep=' ', end='\n'):
...     return sep.join(values) + end
>>>
>>>
>>> print('a')
'a\n'
>>>
>>> print('a', 'b')
'a b\n'
>>>
>>> print('a', 'b', 'c')
'a b c\n'
>>>
>>> print('a', 'b', 'c', sep=',')
'a,b,c\n'
>>>
>>> print('a', 'b', 'c', sep='|')
'a|b|c\n'


Assignments
-----------
.. literalinclude:: assignments/unpack_parameters_a.py
    :caption: :download:`Solution <assignments/unpack_parameters_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_parameters_b.py
    :caption: :download:`Solution <assignments/unpack_parameters_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_parameters_c.py
    :caption: :download:`Solution <assignments/unpack_parameters_c.py>`
    :end-before: # Solution
