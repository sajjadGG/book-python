#!/usr/bin/env python3

import ctypes

_hello = ctypes.CDLL('hello-ctypes.so')
_hello.say_hello.argtypes = [ctypes.c_char_p]

name = 'Jose Jimenez'.encode('ASCII')
buffer = ctypes.create_string_buffer(name)
greeting = _hello.say_hello(buffer)
print(greeting)

time = _hello.what_time()
print(time)

