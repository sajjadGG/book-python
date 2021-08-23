FuncProg Namespace
==================


Rationale
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


Functions Inside Function
-------------------------
* Functions inside function

>>> def run():
...     def a():
...         print('A')
...
...     def b():
...         print('B')


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
...     def myfunction:
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
>>> run()
<function __main__.run.<locals>.b()>
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
>>> run()  # doctest: +NORMALIZE_WHITESPACE
(<function __main__.run.<locals>.a()>,
 <function __main__.run.<locals>.b()>)
>>>
>>> run()()
Traceback (most recent call last):
TypeError: 'tuple' object is not callable
>>>
>>> run()[0]
<function __main__.run.<locals>.a()>
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
...     a = 10
...     b = 20
...
...     class MyClass:
...         def hello(self):
...             pass
...
...     def abc():
...         pass
...
...     def self():
...         pass
...
...     return MyClass
>>>
>>>
>>> run()
<class '__main__.run.<locals>.MyClass'>


Locals
------
>>> def run(a=1):
...     b = 1
...     print(locals())
>>>
>>>
>>> run()
{'a': 1, 'b': 1}
