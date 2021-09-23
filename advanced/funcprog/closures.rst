FuncProg Closure
================


Rationale
---------
* Technique by which the data is attached to some code even after end of
  those other original functions is called as closures

* When the interpreter detects the dependency of inner nested function on
  the outer function, it stores or makes sure that the variables in which
  inner function depends on are available even if the outer function goes
  away

* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants


Example
-------
>>> def f(x):
...     def g(y):
...         return x + y
...     return g


Recap
-----
* Function can access data from outer scope

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> run()
Hello Mark Watney

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> def run():
...     print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> run()
Hello Mark Watney


Nested Function
---------------
* Function inside the function
* Nested functions can access the variables of the enclosing scope

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def hello():
...         print(f'Hello {firstname} {lastname}')
...     hello()
>>>
>>>
>>> run()
Hello Mark Watney
>>>
>>> hello()
Traceback (most recent call last):
NameError: name 'hello' is not defined

>>> def run(firstname, lastname):
...     def hello():
...         print(f'Hello {firstname} {lastname}')
...     hello()
>>>
>>>
>>> run('Mark', 'Watney')
Hello Mark Watney


What is closure?
----------------
* Function local variables are stored on the stack (function stack frame)
* Inner functions have access to outer functions variables (access to
  outer function stack)
* In order to that work, you can call inner function only when outer
  function is running [#ytclosures]_

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def hello():
...         print(f'Hello {firstname} {lastname}')
...     return hello
>>>
>>>
>>> result = run()
>>> result()
Hello Mark Watney

Remove Outer Function:

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...     def hello():
...         print(f'Hello {firstname} {lastname}')
...     return hello
>>>
>>>
>>> result = run()
>>> del run
>>> result()
Hello Mark Watney


References
----------
.. [#ytclosures] Martin, Robert C. The S.O.L.I.D. Principles of OO & Agile Design. Year: 2015. Retrieved: 2021-09-22. https://youtu.be/t86v3N4OshQ?t=954


Assignments
-----------
.. literalinclude:: assignments/funcprog_closure_a.py
    :caption: :download:`Solution <assignments/funcprog_closure_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/funcprog_closure_b.py
    :caption: :download:`Solution <assignments/funcprog_closure_b.py>`
    :end-before: # Solution

