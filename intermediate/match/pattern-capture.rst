Match Pattern Capture
=====================

A `capture pattern` looks like x and is equivalent to an identical
assignment target: it always matches and binds the variable with the
given (simple) name.


>>> def get(path):
...     print(f'Processing GET request for {path}')
>>>
>>> def post(path):
...     print(f'Processing POST request for {path}')
>>>
>>> def put(path):
...     print(f'Processing PUT request for {path}')
>>>
>>> def delete(path):
...     print(f'Processing DELETE request for {path}')
>>>
>>>
>>> def process_request(request):
...     match request.split():
...         case ['GET',    path, 'HTTP/2.0']: get(path)
...         case ['POST',   path, 'HTTP/2.0']: post(path)
...         case ['PUT',    path, 'HTTP/2.0']: put(path)
...         case ['DELETE', path, 'HTTP/2.0']: delete(path)
>>>
>>>
>>> process_request('POST /user/ HTTP/2.0')
Processing POST request for /user/
>>>
>>> process_request('GET /user/mwatney/ HTTP/2.0')
Processing GET request for /user/mwatney/
>>>
>>> process_request('PUT /user/mwatney/ HTTP/2.0')
Processing PUT request for /user/mwatney/
>>>
>>> process_request('DELETE /user/mwatney/ HTTP/2.0')
Processing DELETE request for /user/mwatney/


Use Case - 0x01
---------------
>>> class Astronaut:
...     def move_left(self, value):
...         print(f'Moving left by {value}')
...
...     def move_right(self, value):
...         print(f'Moving right by {value}')
...
...     def move_up(self, value):
...         print(f'Moving up by {value}')
...
...     def move_down(self, value):
...         print(f'Moving down by {value}')
>>>
>>>
>>> hero = Astronaut()
>>>
>>> def move(*how):
...     match how:
...         case ['left', value]:   hero.move_left(value)
...         case ['right', value]:  hero.move_right(value)
...         case ['up', value]:     hero.move_up(value)
...         case ['down', value]:   hero.move_down(value)
>>>
>>>
>>> move('left', 1)
Moving left by 1
>>>
>>> move('right', 2)
Moving right by 2
>>>
>>> move('up', 3)
Moving up by 3
>>>
>>> move('down', 4)
Moving down by 4

