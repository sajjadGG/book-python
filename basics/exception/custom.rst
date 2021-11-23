Exception Define
================


Define Custom Exceptions
------------------------
* Class which inherits from ``Exception``
* Exceptions should have ``Error`` at the end of their names

>>> class MyError(Exception):
...     pass
>>>
>>>
>>> raise MyError
Traceback (most recent call last):
MyError
>>>
>>> raise MyError('More verbose description')
Traceback (most recent call last):
MyError: More verbose description


Example
-------
>>> class AstronautsOnlyError(Exception):
...     pass
>>>
>>>
>>> profession = 'pilot'
>>>
>>> if profession != 'astronaut':
...     raise AstronautsOnlyError
Traceback (most recent call last):
AstronautsOnlyError


Use Case - 0x01
---------------
Django Framework Use-case of Custom Exceptions:

>>> # doctest: +SKIP
... from django.contrib.auth.models import User
>>>
>>>
>>> def login(request):
...     username = request.POST.get('username')
...     password = request.POST.get('password')
...
...     try:
...         user = User.objects.get(username, password)
...     except User.DoesNotExist:
...         print('Sorry, no such user in database')


Use Case - 0x02
---------------
* Dragon

>>> class Dragon:
...     def take_damage(self, damage):
...         raise self.IsDead
...
...     class IsDead(Exception):
...         pass
>>>
>>>
>>> wawelski = Dragon()
>>>
>>> try:
...     wawelski.take_damage(10)
... except Dragon.IsDead:
...     print('Dragon is dead')
Dragon is dead


Assignments
-----------
.. literalinclude:: assignments/exception_custom_a.py
    :caption: :download:`Solution <assignments/exception_custom_a.py>`
    :end-before: # Solution
