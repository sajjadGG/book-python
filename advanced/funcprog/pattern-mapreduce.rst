Pattern MapReduce
=================

SetUp
-----
>>> from functools import reduce


Pattern
-------
>>> class MapReduce:
...     def __init__(self, values):
...         self.values = values
...
...     def filter(self, fn):
...          self.values = filter(fn, self.values)
...          return self
...
...     def map(self, fn):
...         self.values = map(fn, self.values)
...         return self
...
...     def reduce(self, fn):
...         return reduce(fn, self.values)


Usage
-----
>>> DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> result = (
...     MapReduce(DATA)
...     .map(lambda x: x ** 2)
...     .map(lambda x: x / 2)
...     .map(lambda x: x + 2)
...     .map(lambda x: round(x, 2))
...     .map(lambda x: int(x))
...     .filter(lambda x: x > 10)
...     .reduce(lambda x,y: x + y)
... )
>>>
>>> result
136

