.. testsetup::

    # doctest: +SKIP_FILE


ORM Delete
==========


Delete
------
>>> SomeModel.objects.filter(id=id).delete()  # doctest: +SKIP

>>> instance = SomeModel.objects.get(id=id)  # doctest: +SKIP
>>> instance.delete()  # doctest: +SKIP


Try Delete
----------
