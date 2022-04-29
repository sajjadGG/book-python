.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Damage Make
======================
* ADR - Architecture Design Records


Problem
-------
* Dragon makes damage


Option 1
--------
>>> dragon.attack()
>>> dragon.hit()
>>> dragon.hurt()
>>> dragon.damage()
>>> dragon.wound()

* Bad: dragon <-> enemy
* Bad: not directed, all methods could mean making damage or receiving damage

Rationale:

Some method names has stronger emphasis on who is making damage to whom.
Consider this: ``dragon.hurt()`` - is that dragon who makes damage or takes
damage?

.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy


Option 2
--------
>>> dragon.deal_damage()
>>> dragon.hurt_someone()
>>> dragon.make_damage()

* Good: dragon ---> enemy
* Bad: to specific ``.hurt_someone()``, ``.deal_damage()``


Option 3
--------
>>> dragon.take_damage()

* Bad: dragon <--- enemy


Option 4
--------
>>> dragon.damage(ENEMY)
>>> dragon.attack(ENEMY)
>>> dragon.hit(ENEMY)
>>> dragon.wound(ENEMY)
>>> dragon.make_damage(ENEMY)
>>> dragon.take_damage(ENEMY)

* Good: dragon ---> enemy
* Bad: MVC

.. figure:: img/dragon-firkraag-01.jpg
.. figure:: img/oop-architecture-mvc.png
.. figure:: img/oop-architecture-mvc-example.png

Problem:

>>> class BankAccount:
...     def transfer(destination_account, amount):
...         destination_account.deposit(amount)

* Bad: other bank of will not share their source code with you, to make a transfer


Option 5
--------
>>> hero.health -= dragon.damage()

* Good: simple
* Good: can use ``@property`` for validation if needed
* Bad: encapsulation


Option 6
--------
>>> hero.wound(dragon.hit())

* Bad: readability
* Bad: requires knowledge of API
* Bad: this is responsibility of a controller


Option 7
--------
>>> dragon.get_damage()

* Good: readability
* Good: easy to add validation if needed
* Bad: name ``get_damage()`` indicate a getter of ``damage`` field


Decision
--------
>>> dmg = dragon.make_damage()

* Good: dragon ---> enemy
