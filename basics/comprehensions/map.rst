Comprehension Map
=================


Syntax
------
Applying function to each output element:

>>> [float(x) for x in range(0,5)]
[0.0, 1.0, 2.0, 3.0, 4.0]

>>> [float(x) for x in range(0,5) if x%2==0]
[0.0, 2.0, 4.0]

Applying function to each output element:

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [pow(2,x) for x in range(0,5) if x%2==0]
[1, 4, 16]

Using ``list`` comprehension for filtering:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>> [tuple(features) for *features,label in DATA if label == 'setosa']  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]
>>>
>>> [tuple(X) for *X,y in DATA if y=='setosa']  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]


Use Case - Join Numbers
-----------------------
>>> DATA = [1, 2, 3]
>>>
>>>
>>> ','.join(DATA)
Traceback (most recent call last):
TypeError: sequence item 0: expected str instance, int found

>>> DATA = [1, 2, 3]
>>>
>>>
>>> ','.join(str(x) for x in DATA)
'1,2,3'


Use Case - CSV
--------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> data = [','.join(str(x) for x in row) for row in DATA]  # doctest: +NORMALIZE_WHITESPACE
['Sepal length,Sepal width,Petal length,Petal width,Species',
 '5.8,2.7,5.1,1.9,virginica',
 '5.1,3.5,1.4,0.2,setosa',
 '5.7,2.8,4.1,1.3,versicolor',
 '6.3,2.9,5.6,1.8,virginica',
 '6.4,3.2,4.5,1.5,versicolor',
 '4.7,3.2,1.3,0.2,setosa',
 '7.0,3.2,4.7,1.4,versicolor']

Use Case - Power
----------------
>>> [pow(x,2) for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]

>>> [pow(2,x) for x in range(0,5)]
[1, 2, 4, 8, 16]

>>> [2**x for x in range(0,5)]
[1, 2, 4, 8, 16]


Use Case - Map list[dict]
-------------------------
>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': person['name'].split()[0],
...                'lastname': person['name'].split()[1]}
...                for person in DATA
...                if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'Twardowski'},
 {'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': person['name'].split()[0].capitalize(),
...                'lastname': person['name'].split()[1][0]+'.'}
...                for person in DATA
...                if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'T.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Melissa', 'lastname': 'L.'}]


>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [{'firstname': fname, 'lastname': lname}
...                for person in DATA
...                if person['is_astronaut']
...                and (name := person['name'].split())
...                and (fname := name[0].capitalize())
...                and (lname := f'{name[1][0]}.')]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Jan', 'lastname': 'T.'},
 {'firstname': 'Mark', 'lastname': 'W.'},
 {'firstname': 'Melissa', 'lastname': 'L.'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [f'{fname} {lname[0]}.'
...               for person in DATA
...               if person['is_astronaut']
...               and (fullname := person['name'].split())
...               and (fname := fullname[0].capitalize())
...               and (lname := fullname[1].upper())]
>>>
>>> print(astronauts)
['Jan T.', 'Mark W.', 'Melissa L.']

More information in `Assignment Expression`

Using ``list`` comprehension for filtering with more complex expression:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> def is_setosa(species):
...     if species == 'setosa':
...         return True
...     else:
...         return False
>>>
>>>
>>> [tuple(X) for *X,y in DATA if is_setosa(y)]  # doctest: +NORMALIZE_WHITESPACE
[(5.1, 3.5, 1.4, 0.2),
 (4.7, 3.2, 1.3, 0.2)]

Quick parsing lines:

>>> DATA = ['5.8,2.7,5.1,1.9,virginica',
...         '5.1,3.5,1.4,0.2,setosa',
...         '5.7,2.8,4.1,1.3,versicolor']
>>>
>>> result = []
>>>
>>> for row in DATA:
...     row = row.split(',')
...     result.append(row)
>>>
>>> print(result)  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]
>>>
>>> [row.split(',') for row in DATA]  # doctest: +NORMALIZE_WHITESPACE
[['5.8', '2.7', '5.1', '1.9', 'virginica'],
 ['5.1', '3.5', '1.4', '0.2', 'setosa'],
 ['5.7', '2.8', '4.1', '1.3', 'versicolor']]


Assignments
-----------
.. todo:: Create Assignments
