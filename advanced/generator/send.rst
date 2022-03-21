Generator Send
==============
* ``.send()`` method allows to pass value to the generator
* ``data = yield`` will receive this "sent" value


Example
-------
* After running you have to send ``None`` value to begin processing

>>> def run():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>>
>>> worker = run()
>>> worker.send(None)
>>>
>>> worker.send(0)
Processing 0
>>>
>>> worker.send(1)
Processing 1
>>>
>>> worker.send(2)
Processing 2

>>> from inspect import isgenerator, isgeneratorfunction
>>>
>>>
>>> def run():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>> worker = run()
>>> worker.send(None)
>>>
>>> worker.send(1)
Processing 1
>>>
>>> worker.send('hello')
Processing hello
>>>
>>> worker.send([1,2,3])
Processing [1, 2, 3]
>>>
>>> isgeneratorfunction(run)
True
>>> isgenerator(worker)
True


Why Send None?!
---------------
* After running you have to send ``None`` value to begin processing
* Sending anything other will raise ``TypeError``

>>> def run():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>>
>>> worker = run()
>>>
>>> type(worker)
<class 'generator'>
>>>
>>> worker.send('hello')
Traceback (most recent call last):
TypeError: can't send non-None value to a just-started generator


Send Upstream Cascade
---------------------
>>> def worker():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>> def run(gen):
...     gen.send(None)
...     while True:
...         x = yield
...         gen.send(x)
>>>
>>>
>>> result = run(worker())
>>> result.send(None)
>>>
>>> for x in range(0,3):
...     result.send(x)
Processing 0
Processing 1
Processing 2
