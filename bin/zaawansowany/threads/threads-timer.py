#!/usr/bin/env python3

from threading import Timer


def hello():
    print("hello, world")

t = Timer(5.0, hello)
t.start()

print('hej')