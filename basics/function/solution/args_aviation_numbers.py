CONVERSION = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'tree',
    4: 'fower',
    5: 'fife',
    6: 'six',
    7: 'seven',
    8: 'ait',
    9: 'niner',
}

CONVERSION = {str(k):v for k,v in CONVERSION.items()}
CONVERSION['-'] = 'minus'
CONVERSION['.'] = 'and'


def translate(number):
    """
    >>> translate(1969)
    'one niner six niner'

    >>> translate(31337)
    'tree one tree tree seven'

    >>> translate(13.37)
    'one tree and tree seven'

    >>> translate(31.337)
    'tree one and tree tree seven'

    >>> translate(-1969)
    'minus one niner six niner'

    >>> translate(-31.337)
    'minus tree one and tree tree seven'

    >>> translate(-49.35)
    'minus fower niner and tree fife'
    """
    return ' '.join(CONVERSION[c] for c in str(number))

## Alternative solution
#
# def translate(number):
#     """
#     >>> TEST = [
#     ...     1969,
#     ...     31337,
#     ...     13.37,
#     ...     31.337,
#     ...     -1969,
#     ...     -31.337,
#     ...     -49.35,
#     ... ]
#     >>> for number in TEST:
#     ...     translate(number)
#     'one niner six niner'
#     'tree one tree tree seven'
#     'one tree and tree seven'
#     'tree one and tree tree seven'
#     'minus one niner six niner'
#     'minus tree one and tree tree seven'
#     'minus fower niner and tree fife'
#     """
#     sentence = []
#
#     for character in str(number):
#         word = CONVERSION.get(character)
#         sentence.append(word)
#
#     return ' '.join(sentence)
