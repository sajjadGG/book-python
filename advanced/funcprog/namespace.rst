FuncProg Namespace
==================


Important
---------
* Functions provide namespaces
* Only code inside that namespace can access it's locals

>>> def run():
...     a = 1
...     print(a)
>>>
>>>
>>> print(a)
Traceback (most recent call last):
NameError: name 'a' is not defined
>>>
>>> run()
1


Variables Inside Function
-------------------------
* Variables inside function

>>> def run():
...     a = 1
...     b = 2


Functions Inside Function
-------------------------
* Functions inside function

>>> def run():
...     def a():
...         pass
...
...     def b():
...         pass


Classes Inside Function
-----------------------
>>> def run():
...     class A:
...         pass
...
...     class B:
...         pass


Variables, Functions and Classes Inside Function
------------------------------------------------
>>> def run():
...     myvariable = 1
...
...     def myfunction():
...         pass
...
...     class MyClass:
...         pass


Execute
-------
>>> def run():
...     def a():
...         print('A')
...
...     def b():
...         print('B')
...
...     a()
...     b()
>>>
>>>
>>> result = run()
A
B
>>>
>>> print(result)
None


Return
------
>>> def run():
...     def a():
...         return 'A'
...
...     def b():
...         return 'B'
...
...     return a(), b()
>>>
>>>
>>> run()
('A', 'B')
>>>
>>> run()()
Traceback (most recent call last):
TypeError: 'tuple' object is not callable
>>>
>>> ('A', 'B')()
Traceback (most recent call last):
TypeError: 'tuple' object is not callable

>>> def run():
...     def a():
...         print('A')
...
...     def b():
...         print('B')
...
...     return b
>>>
>>>
>>> run()  # doctest: +ELLIPSIS
<function run.<locals>.b at 0x...>
>>>
>>> run()()
B

>>> def run():
...     def a():
...         print('A')
...
...     def b():
...         print('B')
...
...     return a, b
>>>
>>>
>>> run()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(<function run.<locals>.a at 0x...>,
 <function run.<locals>.b at 0x...>)
>>>
>>> run()()
Traceback (most recent call last):
TypeError: 'tuple' object is not callable
>>>
>>> run()[0]  # doctest: +ELLIPSIS
<function run.<locals>.a at 0x...>
>>>
>>> run()[0]()
A
>>>
>>> run()[1]()
B
>>>
>>> a, b = run()
>>>
>>> a()
A
>>>
>>> b()
B
>>>
>>> x, y = run()
>>>
>>> x()
A
>>>
>>> y()
B

>>> def run():
...     a = 1
...     b = 2
...
...     def say_hello():
...         pass
...
...     class Astronaut:
...         def hello(self):
...             pass
...
...     return Astronaut
>>>
>>>
>>> run()
<class 'Astronaut'>


Locals
------
>>> def run(a=1):
...     b = 1
...     print(locals())
>>>
>>>
>>> run()
{'a': 1, 'b': 1}

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         pass
...
...     class Astronaut:
...         def hello(self):
...             pass
...
...     print(locals())
>>>
>>>
>>> run()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'say_hello': <function run.<locals>.say_hello at 0x...>,
 'Astronaut': <class 'Astronaut'>}
