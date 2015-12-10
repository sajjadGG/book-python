#!/usr/bin/env python3

import ctypes

ehlo = ctypes.CDLL('hello-ctypes.so')

ehlo.ehlo()

ehlo.greeting.argtypes = [ctypes.c_char_p]
name = ctypes.create_string_buffer('Matt'.encode())
ehlo.greeting(name)

ehlo.number(10)

print(dir(ehlo))


i = ehlo.myint(15)
print(i)

