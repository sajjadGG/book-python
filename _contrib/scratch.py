"""
>>> from dataclasses import dataclass
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
>>>
>>>
>>> class Timezone:
...     timezone: ZoneInfo
...
...     def __init__(self, name):
...         self.timezone = ZoneInfo(name)
...
...     def __get__(self, parent, *args):
...         return parent.utc.astimezone(self.timezone)
...
...     def __set__(self, parent, new_datetime):
...         local_time = new_datetime.astimezone(self.timezone)
...         parent.utc = local_time.astimezone(ZoneInfo('UTC'))
>>>
>>>
>>> @dataclass
... class Time:
...     utc = datetime.now(tz=ZoneInfo('UTC'))
...     warsaw = Timezone('Europe/Warsaw')
...     moscow = Timezone('Europe/Moscow')
...     est = Timezone('America/New_York')
...     pdt = Timezone('America/Los_Angeles')
>>>
>>>
>>> t = Time()
>>>
>>> t.utc = datetime(1961, 4, 12, 6, 7)  # Gagarin's launch to space
>>> print(t.utc)
1961-04-12 06:07:00
>>> print(t.moscow)
1961-04-12 09:07:00+03:00
>>> print(t.warsaw)
1961-04-12 09:06:59+01:00
>>> print(t.moscow)
1961-04-12 11:06:59+03:00
>>> print(t.est)
1961-04-12 03:06:59-05:00
>>> print(t.pdt)
1961-04-12 00:06:59-08:00
>>>
>>>
>>> t.warsaw = datetime(1969, 7, 21, 3, 56, 15)  # Armstrong's first Lunar step
>>> print(t.utc)
1969-07-21 02:56:15+00:00
>>> print(t.warsaw)
1969-07-21 03:56:15+01:00
>>> print(t.moscow)
1969-07-21 05:56:15+03:00
>>> print(t.est)
1969-07-20 22:56:15-04:00
>>> print(t.pdt)
1969-07-20 19:56:15-07:00
"""
