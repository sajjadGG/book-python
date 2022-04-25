RE Match
========
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Example
-------
Usage of ``re.match()``:

>>> import re
>>>
>>>
>>> def is_valid_email(email: str) -> bool:
...     PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,20}$'
...
...     if re.match(PATTERN, email):
...         return True
...     else:
...         return False
>>>
>>>
>>> is_valid_email('mark.watney@nasa.gov')
True
>>> is_valid_email('mark.watney@nasa.g')
False


Good Practices
--------------
* Doctests

>>> import re
>>>
>>>
>>> username = r'[a-z][a-z0-9._-]*'
>>> domain   = r'([a-z0-9-.]+)+'
>>> tld      = r'[a-z]{2,10}'
>>> email    = f'{username}@{domain}.{tld}'
>>>
>>> def is_valid(data):
...     if re.match(pattern, data):
...         return True
...     else:
...         return False

>>> import re
>>>
>>>
>>> username = r'^(?P<username>[a-z][a-z0-9._-]*)'
>>> domain   = r'(?P<domain>([a-z0-9-.]+)+)'
>>> tld      = r'(?P<tld>[a-z]{2,10})'
>>> email    = f'^{username}@{domain}.{tld}$'
>>>
>>> def is_valid(data):
...     if re.match(pattern, data):
...         return True
...     else:
...         return False


Doctests
--------
>>> import re
>>>
>>>
>>> username = r'^(?P<username>[a-z][a-z0-9._-]*)'
>>> domain   = r'(?P<domain>([a-z0-9-.]+)+)'
>>> tld      = r'(?P<tld>[a-z]{2,10})'
>>> email    = f'^{username}@{domain}.{tld}$'
>>> pattern = re.compile(email, flags=re.IGNORECASE)
>>>
>>>
>>> def is_valid(data):
...     """
...     >>> is_valid('3ares@nasa.gov')
...     False
...     >>> is_valid('ares3@nasa.gov')
...     True
...     >>> is_valid('a3@nasa.gov')
...     True
...     >>> is_valid('3@nasa.gov')
...     False
...     >>> is_valid('m@nasa.gov')
...     True
...     >>> is_valid('m.watney@nasa.gov')
...     True
...     >>> is_valid('m_watney@nasa.gov')
...     True
...     >>> is_valid('m-watney@nasa.gov')
...     True
...     >>> is_valid('mark.watney@nasa.gov')
...     True
...     >>> is_valid('markwatney@nasa.gov')
...     True
...     >>> is_valid('pan.twardowski@polsa.gov.pl')
...     True
...     >>> is_valid('pan.twardowski@polsa24.gov.pl')
...     True
...     """
...     if pattern.match(data):
...         return True
...     else:
...         return False


Assignments
-----------
.. literalinclude:: assignments/re_match_a.py
    :caption: :download:`Solution <assignments/re_match_a.py>`
    :end-before: # Solution
