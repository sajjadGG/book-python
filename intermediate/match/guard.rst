Match Guard
===========


Use Case - 0x01
---------------
* Game Controller

Test Setup:

>>> class Hero:
...     def make_damage(self): ...
...     def take_damage(self, dmg): ...
>>>
>>> hero = Hero()

Use Case:

>>> action = ['make_damage', 10]
>>>
>>> match action:
...     case ['make_damage', value] if value > 0:
...         hero.make_damage()
...     case ['take_damage', value]:
...         hero.take_damage(value)


