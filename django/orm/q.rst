.. testsetup::

    # doctest: +SKIP_FILE


ORM Q
=====
>>> from django.db.models import Q

>>> fname = Q(firstname='Mark')
>>> lname = Q(lastname='Watney')
>>> Person.objects.get(fname & lname)
<Person: Mark Watney>

>>> mark = Q(firstname='Mark')
>>> watney = Q(lastname='Watney')
>>> Person.objects.filter(mark & watney)
<QuerySet [<Person: Mark Watney>]>

>>> fname = Q(firstname='Mark')
>>> lname = Q(lastname='Watney')
>>> Person.objects.get(fname & lname)
<Person: Mark Watney>

>>> Person.objects.filter(fname & lname)
<QuerySet [<Person: Mark Watney>]>

>>> mark = Q(firstname='Mark')
>>> watney = Q(lastname='Watney')
>>> melissa = Q(firstname='Melissa')
>>> lewis = Q(lastname='Lewis')
>>>
>>> mwatney = mark & watney
>>> mlewis = melissa & lewis
>>>
>>> Person.objects.filter(mwatney | mlewis)
<QuerySet [<Person: Mark Watney>, <Person: Melissa Lewis>]>

>>> astro1 = Q(firstname='Mark', lastname='Watney')
>>> astro2 = Q(firstname='Melissa', lastname='Lewis')
>>> Person.objects.filter(astro1 | astro2)
<QuerySet [<Person: Mark Watney>, <Person: Melissa Lewis>]>

>>> Person.objects.filter(astro1|astro2 | (fname&lname))
<QuerySet [<Person: Mark Watney>, <Person: Melissa Lewis>]>

>>> Person.objects.filter(astro1|astro2 | ~(fname&lname))
<QuerySet [<Person: Mark Watney>, <Person: Rick Martinez>, <Person: Melissa Lewis>, <Person: Jan Twardowski>, <Person: Mark Watney>, <Person: Jan X>, <Person: Mark W>]>

>>> Person.objects.filter( (astro1|astro2) & ~(fname&lname) )
<QuerySet [<Person: Melissa Lewis>]>

>>> mark = Q(Person__firstname='Mark')
>>> melissa = Q(Person__firstname='Melissa')
>>>
>>> Address.objects.filter(mark|melissa)
<QuerySet [<Address: Mark Watney - NASA Pkwy, Houston, Texas USA>, <Address: Melissa Lewis - Powstańców Wielkopolskich, Krakow, malopolskie Poland>]>

>>> str(Address.objects.filter(mark|melissa).query)
'SELECT "Person_address"."id", "Person_address"."Person_id", "Person_address"."type", "Person_address"."street", "Person_address"."house", "Person_address"."apartment", "Person_address"."postcode", "Person_address"."city", "Person_address"."region", "Person_address"."country" FROM "Person_address" INNER JOIN "Person_Person" ON ("Person_address"."Person_id" = "Person_Person"."id") WHERE ("Person_Person"."firstname" = Mark OR "Person_Person"."firstname" = Melissa)'


Union
-----


Alternative
-----------


Negation
--------


Multiple Queries
----------------
