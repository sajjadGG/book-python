Pickle Load
===========


Deserialize Str
---------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bMark Watney\x94.')
'Mark Watney'


Deserialize Int
---------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03K\x01.')
1
>>> pickle.loads(b'\x80\x04K\x00.')
0
>>> pickle.loads(b'\x80\x04\x95\x06\x00\x00\x00\x00\x00\x00\x00J\xff\xff\xff\xff.')
-1


Deserialize Float
-----------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xb9\x99\x99\x99\x99\x99\x9a.')
0.1
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xc9\x99\x99\x99\x99\x99\x9a.')
0.2
>>>
>>> pickle.loads(b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G?\xd3333333.')
0.3


Deserialize Sequence
--------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.')
[1, 2, 3]
>>>
>>> pickle.loads(b'\x80\x03K\x01K\x02K\x03\x87q\x00.')
(1, 2, 3)
>>>
>>> pickle.loads(b'\x80\x03cbuiltins\nset\nq\x00]q\x01(K\x01K\x02K\x03e\x85q\x02Rq\x03.')
{1, 2, 3}
>>>


Deserialize Mapping
-------------------
>>> import pickle
>>>
>>>
>>> pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.')
{'a': 1, 'b': 2, 'c': 3}
