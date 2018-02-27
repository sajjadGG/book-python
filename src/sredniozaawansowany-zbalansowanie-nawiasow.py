#!/usr/bin/env python3

'''
import re

NAWIASY = ['(', ')', '[', ']', '{', '}', '<', '>']
REGEX = '[' + '\\'.join(NAWIASY) + ']'


def zbalansowanie_nawiasow(dane):
    """
    >>> dane = "() [] () ([]()[])"
    >>> zbalansowanie_nawiasow(dane)
    True
    >>> dane = "( (] ([)]"
    >>> zbalansowanie_nawiasow(dane)
    False
    """
    same_nawiasy = re.findall(REGEX, dane)

    if not len(same_nawiasy) % 2:
        return False

    pozycja = 0
    for znak in dane:

        pozycja += 1
'''


BRACES_LIST = ['{', '}', '[', ']', '(', ')','<','>']


def zbalansowanie_nawiasow(reference : str):
    """
    >>> zbalansowanie_nawiasow("() [] () ([]()[])")
    True
    >>> zbalansowanie_nawiasow("( (] ([)]")
    False
    """
    parse_string = ''
    stack = []
    is_balanced = True

    for symbol in reference:
        if symbol in BRACES_LIST:
            parse_string.append(symbol)

    for brace in parse_string:
        if (BRACES_LIST.index(brace)%2):
            stack.append(BRACES_LIST.index(brace))
        else:
            #TODO: handle stack.pop() error
            if (stack.pop() != (BRACES_LIST.index(brace) - 1)):
                return False


    return is_balanced


if __name__ == "__main__":
    import doctest
    doctest.testmod()