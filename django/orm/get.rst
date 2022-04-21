.. testsetup::

    # doctest: +SKIP_FILE


ORM Get
=======
>>> Person.objects.get(id=1)
<Person: Mark Watney>

>>> Person.objects.get(id=999)
Traceback (most recent call last):
Person.models.Person.Person.DoesNotExist: Person matching query does not exist.

>>> try:
...     user = Person.objects.get(firstname='Mark', lastname='Jimenez')
... except Person.DoesNotExist:
...     print('Sorry user does not exist')
Sorry user does not exist

>>> Person.objects.get(firstname='Mark')
Traceback (most recent call last):
Person.models.Person.Person.MultipleObjectsReturned: get() returned more than one Person -- it returned 2!


Get
---


Try Get
-------


Get or Create
-------------


Get or 404
----------
