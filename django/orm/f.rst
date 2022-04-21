.. testsetup::

    # doctest: +SKIP_FILE


ORM F
=====
>>> from django.db.models import F
>>>
>>> Person.objects.all().update(age=F('age')+1)
