Pickle To File
==============


Rationale
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
.. literalinclude:: assignments/pickle_tofile_a.py
    :caption: :download:`Solution <assignments/pickle_tofile_a.py>`
    :end-before: # Solution
