#!/usr/bin/env python3

class Address:

    def __init__(self, host, port):
        self.host = host
        self.port = port


addr = Address(host='127.0.0.1', port=1337)







a = dir(addr)
print('Listowanie za pomocą dir():\n"{}\n\n"'.format(a))


a = addr.__dict__
print('Listowanie za pomoca __dict__:\n{}\n\n'.format(a))


a = [x for x in dir(addr) if not x.startswith('__')]
print('Listowanie pól klasy:\n{}\n\n'.format(a))



print('Dane do podlaczenia to {host}:{port}'.format(**addr.__dict__))


