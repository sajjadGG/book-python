#!/usr/bin/env python3

import argparse
import sys
import logging
import warnings


"""
parser = argparse.ArgumentParser()
parser.add_argument('--file', default='/tmp/input.csv', type=argparse.FileType('r'))

try:
    parser.parse_args()
except SystemExit:
    print('Plik niet')
"""


def read(filename):
    warnings.warn('Ta funkcja niedługo ulegnie zmianie', PendingDeprecationWarning)

    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        logging.critical('Plik nie istnieje')
        sys.exit(2)


parser = argparse.ArgumentParser()
parser.add_argument('--file', default='/tmp/input.csv', type=read)
args = parser.parse_args()
print(args)

