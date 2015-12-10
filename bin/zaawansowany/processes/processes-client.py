#!/usr/bin/env python3

from multiprocessing.connection import Client
import logging
import pickle
from __init__ import Prostokat


rectangle = Prostokat(a=5, b=10)
rect = pickle.dumps(rectangle)

address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')

logging.warning('Sending objects')
conn.send([rect, 'a', 2.5, None, int, sum])

logging.warning('Sending close')
conn.send('close')

conn.close()

