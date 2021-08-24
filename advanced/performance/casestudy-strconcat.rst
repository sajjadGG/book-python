Case Study: Str Concat
======================


Code
----
>>> from time import time
>>>
>>>
>>> class Timeit:
...     def __init__(self, name):
...         self.name = name
...
...     def __enter__(self):
...         self.start = time()
...         return self
...
...     def __exit__(self, *arg):
...         end = time()
...         print(f'Duration of {self.name} is {end-self.start:.2f} second')
>>>
>>>
>>> a = 1
>>> b = 2
>>> repetitions = int(10)  # int(1e7)


F-String
--------
>>> with Timeit('f-string'):
...     for _ in range(repetitions):
...         f'{a}{b}'  # doctest: +SKIP
Duration of f-string is 2.70 second


Add
---
>>> with Timeit('string concat'):
...     for _ in range(repetitions):
...         a + b  # doctest: +SKIP
Duration of string concat is 0.68 second


Format
------
>>> with Timeit('str.format()'):
...     for _ in range(repetitions):
...         '{0}{1}'.format(a, b)  # doctest: +SKIP
Duration of str.format() is 3.46 second

>>> with Timeit('str.format()'):
...     for _ in range(repetitions):
...         '{}{}'.format(a, b)  # doctest: +SKIP
Duration of str.format() is 3.37 second

>>> with Timeit('str.format()'):
...     for _ in range(repetitions):
...         '{a}{b}'.format(a=a, b=b)  # doctest: +SKIP
Duration of str.format() is 4.85 second


%-style
-------
>>> with Timeit('%-style'):
...     for _ in range(repetitions):
...         '%s%s' % (a, b)  # doctest: +SKIP
Duration of %-style is 2.59 second

>>> with Timeit('%-style'):
...     for _ in range(repetitions):
...         '%d%d' % (a, b)  # doctest: +SKIP
Duration of %-style is 2.59 second

>>> with Timeit('%-style'):
...     for _ in range(repetitions):
...         '%f%f' % (a, b)  # doctest: +SKIP
Duration of %-style is 3.82 second
