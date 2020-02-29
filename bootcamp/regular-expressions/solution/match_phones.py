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
