.. testsetup::

    # doctest: +SKIP_FILE


ORM Annotate
============

SetUp
-----
>>> from django.db.models.functions import Concat
>>> from django.db.models import Value

>>> Person.objects.all().values('firstname', 'lastname')
<QuerySet [{'firstname': 'Mark', 'lastname': 'Watney'}, {'firstname': 'Rick', 'lastname': 'Martinez'}, {'firstname': 'Melissa', 'lastname': 'Lewis'}, {'firstname': 'Mark', 'lastname': 'Watney'}, {'firstname': 'Mark', 'lastname': 'W'}]>

>>> Person.objects.all().annotate(fullname=Concat('firstname', 'lastname'))
<QuerySet [<Person: Mark Watney>, <Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.all().annotate(fullname=Concat('firstname', 'lastname')).values('fullname')
<QuerySet [{'fullname': 'MarkWatney'}, {'fullname': 'RickMartinez'}, {'fullname': 'MelissaLewis'}, {'fullname': 'MarkWatney'}, {'fullname': 'MarkW'}]>

>>> Person.objects.all().annotate(fullname=Concat('firstname', '', 'lastname')).values('fullname')
Traceback (most recent call last):
django.core.exceptions.FieldError: Cannot resolve keyword '' into field. Choices are: address, age, attachment, born, created_author, created_author_id, created_date, email, firstname, gender, height, homepage, id, is_adult, job, lastname, modified_author, modified_author_id, modified_date, notes, phone_country_code, phone_number, picture, salary, weight

>>> Person.objects.all().annotate(fullname=Concat('firstname', Value(''), 'lastname')).values('fullname')
<QuerySet [{'fullname': 'MarkWatney'}, {'fullname': 'RickMartinez'}, {'fullname': 'MelissaLewis'}, {'fullname': 'MarkWatney'}, {'fullname': 'MarkW'}]>

>>> Person.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
<QuerySet [{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'MarkWatney'}, {'fullname': 'Mark W'}]>

>>> Person.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
<QuerySet [{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'MarkWatney'}, {'fullname': 'Mark W'}]>

>>> result = Person.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values('fullname')
>>> list(result)
[{'fullname': 'Mark Watney'}, {'fullname': 'Rick Martinez'}, {'fullname': 'Melissa Lewis'}, {'fullname': 'MarkWatney'}, {'fullname': 'Mark W'}]

>>> result = Person.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values_list('fullname')
>>> result
<QuerySet [('Mark Watney',), ('Rick Martinez',), ('Melissa Lewis',), ('Mark Watney',), ('Mark W',)]>

>>> result = Person.objects.all().annotate(fullname=Concat('firstname', Value(' '), 'lastname')).values_list('fullname', flat=True)
>>> result
<QuerySet ['Mark Watney', 'Rick Martinez', 'Melissa Lewis', 'Mark Watney', 'Mark W']>

>>> list(result)
['Mark Watney', 'Rick Martinez', 'Melissa Lewis', 'Mark Watney', 'Mark W']
