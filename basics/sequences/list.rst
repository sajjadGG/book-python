Sequence List
=============
* Mutable - can add, remove, and modify items
* Stores elements of any type


Syntax
------
* ``data = []`` - empty list
* ``data = [1, 2.2, 'abc']`` - list with values
* ``data = []`` is faster than ``data = list()``

Defining empty list with ``[]`` is used more often, but ``list()`` is more
explicit:

>>> data = list()
>>> data = []

Comma after last element is optional:

>>> data = [1]
>>> data = [1,]

Can store elements of any types:

>>> data = [1, 2, 3]
>>> data = [1.1, 2.2, 3.3]
>>> data = [True, False]
>>> data = ['a', 'b', 'c']
>>> data = ['a', 1, 2.2, True, None]

Brackets are required

>>> data = [1, 2, 3]


Type Casting
------------
* ``list()`` converts argument to ``list``
* Takes one iterable as an argument
* Multiple arguments are not allowed

Builtin function ``list()`` converts argument to ``list``

>>> color = 'red'
>>> list(color)
['r', 'e', 'd']

>>> colors = ['red', 'green', 'blue']
>>> list(colors)
['red', 'green', 'blue']

>>> colors = ('red', 'green', 'blue')
>>> list(colors)
['red', 'green', 'blue']

>>> list('red', 'green', 'blue')
Traceback (most recent call last):
TypeError: list expected at most 1 argument, got 4


Get Item
--------
* Returns a value at given index
* Note, that Python start counting at zero (zero based indexing)
* Raises ``IndexError`` if the index is out of range
* More information in `Sequence GetItem`
* More information in `Sequence Slice`

>>> colors = ['red', 'green', 'blue']
>>>
>>> colors[0]
'red'
>>> colors[1]
'green'
>>> colors[2]
'blue'


Set Item
--------
>>> colors = ['red', 'green', 'blue']
>>> colors[0] = 'black'
>>>
>>> print(colors)
['black', 'green', 'blue']

>>> colors = ['red', 'green', 'blue']
>>> colors[4] = 'black'
Traceback (most recent call last):
IndexError: list assignment index out of range


Del Item
--------
>>> colors = ['red', 'green', 'blue']
>>> del colors[2]
>>>
>>> print(colors)
['red', 'green']

>>> colors = ['red', 'green', 'blue']
>>> result = colors.pop()
>>>
>>> colors
['red', 'green']
>>> result
'blue'


Append
------
* ``list + list``
* ``list += list``
* ``list.extend()``
* ``list.append()``

>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]

>>> [1, 2, 3] + 4
Traceback (most recent call last):
TypeError: can only concatenate list (not "int") to list

>>> [1, 2, 3] + [4]
[1, 2, 3, 4]

>>> data = [1, 2, 3]
>>> data = data + [4, 5, 6]
>>>
>>> print(data)
[1, 2, 3, 4, 5, 6]

>>> data = [1, 2, 3]
>>> data += [4, 5, 6]
>>>
>>> print(data)
[1, 2, 3, 4, 5, 6]

>>> data = [1, 2, 3]
>>> data.extend([4, 5, 6])
>>>
>>> print(data)
[1, 2, 3, 4, 5, 6]

>>> data = [1, 2, 3]
>>> data.append(4)
>>>
>>> print(data)
[1, 2, 3, 4]

>>> data = [1, 2, 3]
>>> data.append([4, 5, 6])
>>>
>>> print(data)
[1, 2, 3, [4, 5, 6]]


Insert
------
* ``list.insert(idx, object)``
* Insert object at specific position

>>> data = ['red', 'green', 'blue']
>>> data.insert(0, 'black')
>>>
>>> print(data)
['black', 'red', 'green', 'blue']

>>> data = ['red', 'green', 'blue']
>>> data.insert(1, 'black')
>>>
>>> print(data)
['red', 'black', 'green', 'blue']


Sort vs Sorted
--------------
* ``sorted()`` - returns new sorted list, but does not modify the original
* ``list.sort()`` - sorts list and returns ``None``

Timsort is a hybrid stable sorting algorithm, derived from merge sort and
insertion sort, designed to perform well on many kinds of real-world data.
It was implemented by Tim Peters in 2002 for use in the Python programming
language. The algorithm finds subsequences of the data that are already
ordered (runs) and uses them to sort the remainder more efficiently. This
is done by merging runs until certain criteria are fulfilled. Timsort has
been Python's standard sorting algorithm since version 2.3. It is also used
to sort arrays of non-primitive type in Java SE 7, on the Android platform,
in GNU Octave, on V8, Swift, and Rust. [#timsort]_

* Worst-case performance: :math:`O(n\log{n})`
* Best-case performance: :math:`O(n)`
* Average performance: :math:`O(n\log{n})`
* Worst-case space complexity: :math:`O(n)`

* ``sorted()`` - Returns sorted list, do not modify the original
* ``list.sort()`` - Changes object permanently, returns ``None``

Return sorted values without modifying a list:

>>> data = [3, 1, 2]
>>>
>>> sorted(data)
[1, 2, 3]
>>>
>>> sorted(data, reverse=True)
[3, 2, 1]

Permanent sorting with list modification (note that ``list.sort()`` modifies
data, and returns ``None``, not values):

>>> data = [3, 1, 2]
>>>
>>> data.sort()
>>> data
[1, 2, 3]
>>>
>>> data.sort(reverse=True)
>>> data
[3, 2, 1]

You can also use ``list.sort()`` and/or ``sorted()`` with ``str``. It will
sort strings according to Unicode (UTF-8) value, that is ASCII table for
latin alphabet and Unicode for extended encoding. This kind of sorting is
called lexicographic order.

>>> data = ['a', 'c', 'b']
>>>
>>> sorted(data)
['a', 'b', 'c']


Reverse
-------
* ``reversed()``
* ``list.reverse()``

>>> data = [1, 2, 3]
>>> data.reverse()
>>> data
[3, 2, 1]

>>> data = [1, 2, 3]
>>>
>>> list(reversed(data))
[3, 2, 1]

Why?:

>>> data = [1, 2, 3]
>>> result = reversed(data)
>>>
>>> result  # doctest: +ELLIPSIS
<list_reverseiterator object at 0x...>
>>>
>>> next(result)
3
>>> next(result)
2
>>> next(result)
1
>>> next(result)
Traceback (most recent call last):
StopIteration


Method Chaining
---------------
>>> data = [3, 1, 2]
>>> data.sort()
>>> data.append(4)
>>>
>>> print(data)
[1, 2, 3, 4]

>>> data = [3, 1, 2]
>>>
>>> data.sort().append(4)
Traceback (most recent call last):
AttributeError: 'NoneType' object has no attribute 'append'


Index
-----
* ``list.index()`` - position at which something is in the list
* Note, that Python start counting at zero (zero based indexing)
* Raises ``ValueError`` if the value is not present

>>> colors = ['red', 'green', 'blue']
>>> colors.index('blue')
2


Count
-----
* ``list.count()`` - number of occurrences of value

>>> colors = ['red', 'green', 'blue', 'red', 'blue']
>>> colors.count('blue')
2


Built-in Functions
------------------
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``all()`` - All values are ``True``
* ``any()`` - Any values is ``True``

List with numeric values:

>>> data = [3, 1, 2]
>>>
>>> len(data)
3
>>> min(data)
1
>>> max(data)
3
>>> sum(data)
6

List with string values:

>>> data = ['a', 'c', 'b']
>>>
>>> len(data)
3
>>> min(data)
'a'
>>> max(data)
'c'
>>> sum(data)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'int' and 'str'

List with boolean values:

>>> data = [True, False, True]
>>>
>>> any(data)
True
>>> all(data)
False


Memory
------
.. figure:: img/memory-list.png

    Memory representation for ``list``


Shallow Copy vs Deep Copy
-------------------------
* Shallow Copy (by reference) - identifiers are pointing to the same object in memory
* Deep Copy - identifiers are pointing to distinct objects
* Shallow Copy is faster and requires less memory (no duplicated objects)
* Deep Copy is slower and requires twice sa much memory, but is safe for modification

Shallow Copy:

>>> first = ['a', 'b', 'c']
>>> second = first
>>>
>>> first.append('d')
>>>
>>> first
['a', 'b', 'c', 'd']
>>> second
['a', 'b', 'c', 'd']
>>>
>>> id(first)  # doctest: +SKIP
4417433984
>>> id(second)  # doctest: +SKIP
4417433984

Deep Copy:

>>> first = ['a', 'b', 'c']
>>> second = first.copy()
>>>
>>> first.append('d')
>>>
>>> first
['a', 'b', 'c', 'd']
>>> second
['a', 'b', 'c']
>>>
>>> id(first)  # doctest: +SKIP
4391796976
>>> id(second)  # doctest: +SKIP
4391797008


References
----------
.. [#timsort] https://en.wikipedia.org/wiki/Timsort


Assignments
-----------
.. literalinclude:: assignments/sequence_list_a.py
    :caption: :download:`Solution <assignments/sequence_list_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_b.py
    :caption: :download:`Solution <assignments/sequence_list_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_list_c.py
    :caption: :download:`Solution <assignments/sequence_list_c.py>`
    :end-before: # Solution
