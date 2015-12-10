#!/usr/bin/env python3

import ctypes

_hello = ctypes.CDLL('hello-ctypes.so')

_hello.say_hello.argtypes = [ctypes.c_char_p]

name = 'Matt asd'
buffer = ctypes.create_string_buffer(name.encode('ASCII'))

greeting = _hello.say_hello(buffer)
print(greeting)


