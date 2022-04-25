.. testsetup::

    # doctest: +SKIP_FILE


ORM Filter
==========
>>> Person.objects.filter(firstname='Mark')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', lastname='Watney')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(firstname='Mark', lastname__startswith='W')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', lastname__startswith='W')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', lastname__startswith='w')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', lastname__istartswith='w')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', lastname__istartswith='W')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', created_date__year='2021')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', created_date__gt='2021-09-07')
/src/myproject/.venv/lib/python3.10/site-packages/django/db/models/fields/__init__.py:1416: RuntimeWarning: DateTimeField Person.created_date received a naive datetime (2021-09-07 00:00:00) while time zone support is active.
  warnings.warn("DateTimeField %s received a naive datetime (%s)"
<QuerySet [<Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark', created_date__gt='2021-09-07 00:00:00+00:00')
<QuerySet [<Person: Mark W>]>

>>> Person.objects.filter(age__lt=18)
<QuerySet []>

>>> Person.objects.filter(age__lt=50)
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(age__lte=50)
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(age__gt=50)
<QuerySet []>

>>> Person.objects.filter(age__gte=50)
<QuerySet []>

>>> Person.objects.filter(lastname__contains='ney')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__icontains='ney')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(born='1970-01-01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(born__gt='1970-01-01')
<QuerySet []>

>>> Person.objects.filter(born__gte='1970-01-01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(born__lt='1970-01-01')
<QuerySet []>

>>> Person.objects.filter(born__lte='1970-01-01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(birthday__range=('1900-01-01', '2001-01-01'))
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(born__in=('1970-01-01', '1969-07-21'))
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(birthday__year='2000')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(birthday__month='2000')
<QuerySet []>

>>> Person.objects.filter(birthday__month='01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(birthday__day='01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(birthday__year='2000', birthday__month='01')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__in=[])
<QuerySet []>

>>> Person.objects.filter(lastname__in=['Watney', 'Lewis'])
<QuerySet [<Person: Melissa Lewis>, <Person: Mark Watney>]>

>>> DATA = [1,2,3]
>>> Person.objects.filter(pk__in=DATA)
<QuerySet [<Person: Mark Watney>, <Person: Rick Martinez>, <Person: Melissa Lewis>]>

>>> Person.objects.filter(id__in=DATA)
<QuerySet [<Person: Mark Watney>, <Person: Rick Martinez>, <Person: Melissa Lewis>]>

>>> str(Person.objects.filter(id__in=DATA).query)
'SELECT "Person_Person"."id", "Person_Person"."created_date", "Person_Person"."created_author_id", "Person_Person"."modified_date", "Person_Person"."modified_author_id", "Person_Person"."firstname", "Person_Person"."lastname", "Person_Person"."salary", "Person_Person"."job", "Person_Person"."born", "Person_Person"."age", "Person_Person"."gender", "Person_Person"."is_adult", "Person_Person"."weight", "Person_Person"."height", "Person_Person"."email", "Person_Person"."homepage", "Person_Person"."phone_country_code", "Person_Person"."phone_number", "Person_Person"."picture", "Person_Person"."attachment", "Person_Person"."notes" FROM "Person_Person" WHERE "Person_Person"."id" IN (1, 2, 3)'

>>> Person.objects.filter(groups__name__in=['astronauts', 'scientists'])
<QuerySet [<Person: Mark Watney>, <Person: Alex Vogel>, <Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Mark Watney>, <Person: Alex Vogel>]>

>>> Person.objects.filter(groups__name__in=['astronauts', 'scientists']).distinct()
<QuerySet [<Person: Mark Watney>, <Person: Alex Vogel>, <Person: Rick Martinez>, <Person: Melissa Lewis>]>

>>> Person.objects.filter(born__gte='1969-07-21', born__lte='1970-01-01')
<QuerySet [<Person: Mark Watney>]>

>>> str(Address.objects.filter(Person__lastname__contains='ney').query)
'SELECT "Person_address"."id", "Person_address"."Person_id", "Person_address"."type", "Person_address"."street", "Person_address"."house", "Person_address"."apartment", "Person_address"."postcode", "Person_address"."city", "Person_address"."region", "Person_address"."country" FROM "Person_address" INNER JOIN "Person_Person" ON ("Person_address"."Person_id" = "Person_Person"."id") WHERE "Person_Person"."lastname" LIKE %ney% ESCAPE \'\\\''

>>> str(Address.objects.filter(Person__lastname__startswith='Wat').query)
'SELECT "Person_address"."id", "Person_address"."Person_id", "Person_address"."type", "Person_address"."street", "Person_address"."house", "Person_address"."apartment", "Person_address"."postcode", "Person_address"."city", "Person_address"."region", "Person_address"."country" FROM "Person_address" INNER JOIN "Person_Person" ON ("Person_address"."Person_id" = "Person_Person"."id") WHERE "Person_Person"."lastname" LIKE Wat% ESCAPE \'\\\''

>>> Person.objects.filter(firstname='Mark')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark').exclude(lastname='W')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects \
...        .filter(firstname='Mark') \
...        .filter(created_date__gte='2021-09-07 00:00:00+00:00') \
...        .exclude(lastname='W') \
...        .distinct() \
...        .order_by('lastname', 'firstname')


>>> from datetime import datetime, timezone
>>>
>>>
>>> Person.objects \
...        .filter(firstname='Mark') \
...        .filter(created_date__lte=datetime.now(timezone.utc)) \
...        .exclude(lastname='W') \
...        .distinct() \
...        .order_by('lastname', 'firstname')
<QuerySet [<Person: Mark Watney>]>


>>> Person.objects.filter(firstname='Mark')[1]
<Person: Mark W>

>>> Person.objects.filter(firstname='Mark')[1:]
<QuerySet [<Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark')[1:5]
<QuerySet [<Person: Mark W>]>

>>> Person.objects.filter(firstname='Mark')[:5]
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>


>>> q = Person.objects
>>> q = q.filter(firstname='Mark')
>>> q = q.filter(created_date__lte=datetime.now(timezone.utc))
>>> q = q.exclude(lastname='W')
>>> q = q.distinct()
>>> q = q.order_by('lastname', 'firstname')
>>> q
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__endswith='ney')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__iendswith='ney')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__startswith='Wat')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(lastname__istartswith='Wat')
<QuerySet [<Person: Mark Watney>]>

>>> Person.objects.filter(age__isnull=True)
<QuerySet [<Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Mark Watney>, <Person: Mark W>]>

>>> Address.objects.filter(Person__age__isnull=True)
<QuerySet [<Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>

>>> Person.objects.filter(firstname='Mark')
<QuerySet [<Person: Mark Watney>, <Person: Mark W>]>

>>> Address.objects.filter(Person__in=Person.objects.filter(firstname='Mark'))
<QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>]>

>>> str(Address.objects.filter(Person__in=Person.objects.filter(firstname='Mark')).query)
'SELECT "Person_address"."id", "Person_address"."Person_id", "Person_address"."type", "Person_address"."street", "Person_address"."house", "Person_address"."apartment", "Person_address"."postcode", "Person_address"."city", "Person_address"."region", "Person_address"."country" FROM "Person_address" WHERE "Person_address"."Person_id" IN (SELECT U0."id" FROM "Person_Person" U0 WHERE U0."firstname" = Mark)'

>>> Person.objects.filter(lastname='XYZ').exists()
False

>>> Person.objects.filter(lastname='Watney').exists()
True

>>> Person.objects.all().last()
<Person: Mark W>

>>> Person.objects.all().first()
<Person: Mark Watney>

>>> Address.objects.filter(Person__lastname='Watney')
<QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>]>

>>> str(Address.objects.filter(Person__lastname='Watney').query)
'SELECT "Person_address"."id", "Person_address"."Person_id", "Person_address"."type", "Person_address"."street", "Person_address"."house", "Person_address"."apartment", "Person_address"."postcode", "Person_address"."city", "Person_address"."region", "Person_address"."country" FROM "Person_address" INNER JOIN "Person_Person" ON ("Person_address"."Person_id" = "Person_Person"."id") WHERE "Person_Person"."lastname" = Watney'
