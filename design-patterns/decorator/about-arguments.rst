Decorator About Arguments
=========================
* Without Arguments
* With Positional Arguments
* With Mixed Arguments
* With Keyword Arguments


Without Arguments
-----------------
>>> @mydecorator  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Positional Arguments
-------------------------
>>> @mydecorator('Mark', 'Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Mixed Arguments
--------------------
>>> @mydecorator('Mark', lastname='Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...


With Keyword Arguments
----------------------
>>> @mydecorator(firstname='Mark', lastname='Watney')  # doctest: +SKIP
... def myfunction(*args, **kwargs):
...     ...
