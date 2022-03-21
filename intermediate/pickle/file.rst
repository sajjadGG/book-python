Pickle File
===========


Important
---------
* File extension ``pkl``


Serialize to File
-----------------
>>> import pickle
>>>
>>>
>>> DATA = [1, 2, 3]
>>>
>>> with open('filename.pkl', mode='wb') as file:
...     pickle.dump(DATA, file)


Deserialize from File
---------------------
Load from file:

>>> import pickle
>>>
>>>
>>> with open('filename.pkl', mode='rb') as file:
...     result = pickle.load(file)
>>>
>>> print(result)
[1, 2, 3]


Assignments
-----------
.. literalinclude:: assignments/pickle_file_a.py
    :caption: :download:`Solution <assignments/pickle_file_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pickle_file_b.py
    :caption: :download:`Solution <assignments/pickle_file_b.py>`
    :end-before: # Solution
