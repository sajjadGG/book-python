Comprehension Tuple
===================


Rationale
---------
* Tuple Comprehension vs. Generator Expression
* More information in `Generators`


Long Syntax
-----------
>>> tuple(x+10 for x in range(0,5))
(10, 11, 12, 13, 14)


Short Syntax
------------
* There is no short syntax for Tuple Comprehension
* Round brackets will create Generator Expression

>>> (x+10 for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


.. todo:: Assignments
