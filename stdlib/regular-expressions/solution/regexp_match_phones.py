import re

MOBILE = r'(\+\d\d \d\d\d \d\d\d \d\d\d)'
WORK = r'(\+\d\d \d\d \d\d\d \d\d\d\d)'
PATTERN = f'^{MOBILE}|{WORK}$'


def is_valid_phone(number):
    if re.match(PATTERN, number):
        return True
    else:
        return False


numery = [
    '+48 (12) 355 5678',
    '+48 123 555 678',
    '123 555 678',
    '+48 12 355 5678',
    '+48 123-555-678',
    '+48 123 555 6789',
    '+1 (123) 555-6789',
    '+1 (123).555.6789',
    '+1 800-python',
    '+48123555678',
    '+48 123 555 678 wew. 1337',
    '+48 123555678,1',
    '+48 123555678,1,2,3',
]

for numer in numery:
    print(is_valid_phone(numer), numer)




## Alternative solution
import re


PATTERN = r'^'                      # Start String
PATTERN += r'\+\d{2} ('             # Country Code
PATTERN += r'(\d{2} \d{3} \d{4})'   # Work Phone
PATTERN += r'|'                     # Or
PATTERN += r'(\d{3} \d{3} \d{3})'   # Mobile
PATTERN += r')$'                    # End String


def is_valid_phone(number):
    """
    >>> is_valid_phone('+48 (12) 355 5678')
    False
    >>> is_valid_phone('+48 123 555 678')
    True
    >>> is_valid_phone('123 555 678')
    False
    >>> is_valid_phone('+48 12 355 5678')
    True
    >>> is_valid_phone('+48 123-555-678')
    False
    >>> is_valid_phone('+48 123 555 6789')
    False
    >>> is_valid_phone('+1 (123) 555-6789')
    False
    >>> is_valid_phone('+1 (123).555.6789')
    False
    >>> is_valid_phone('+1 800-python')
    False
    >>> is_valid_phone('+48123555678')
    False
    >>> is_valid_phone('+48 123 555 678 wew. 1337')
    False
    >>> is_valid_phone('+48 123555678,1')
    False
    >>> is_valid_phone('+48 123555678,1,2,3')
    False
    """
    if re.match(PATTERN, number):
        return True
    else:
        return False
