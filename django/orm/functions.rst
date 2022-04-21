.. testsetup::

    # doctest: +SKIP_FILE


ORM Functions
=============
>>> from django.db.models import Avg, Sum, Min, Max, Count

>>> Person.objects.count()
7

>>> Person.objects.filter(firstname='Mark').count()
2

>>> Person.objects.all().aggregate(Avg('age'))
{'age__avg': 30.0}

>>> Person.objects.all().aggregate(Avg('age'))
{'age__avg': 34.0}

>>> Person.objects.all().aggregate(Max('age'))
{'age__max': 45}

>>> Person.objects.all().aggregate(Min('age'))
{'age__min': 27}

>>> Person.objects.all().aggregate(Sum('age'))
{'age__sum': 102}

>>> Person.objects.all().aggregate(Sum('salary'))
{'salary__sum': Decimal('1024')}

>>> Person.objects.all().aggregate(Avg('age'), Min('age'), Max('age'))
{'age__avg': 34.0, 'age__min': 27, 'age__max': 45}

>>> below_30 = Count('age', filter=Q(age__lte=30))
>>> above_30 = Count('age', filter=Q(age__gt=30))
>>>
>>> Person.objects.annotate(above_30=above_30).annotate(below_30=below_30).values('above_30', 'below_30')
<QuerySet [{'above_30': 0, 'below_30': 1}, {'above_30': 1, 'below_30': 0}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 1}, {'above_30': 0, 'below_30': 0}, {'above_30': 0, 'below_30': 0}]>


Concat
------
