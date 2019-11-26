ALPHABET = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'tree',
    '4': 'fower',
    '5': 'fife',
    '6': 'six',
    '7': 'seven',
    '8': 'ait',
    '9': 'niner',
    '-': 'minus',
    '.': 'and',
}


def aviation_numbers(number):
    """
    >>> aviation_numbers(1969)
    'one niner six niner'

    >>> aviation_numbers(31337)
    'tree one tree tree seven'

    >>> aviation_numbers(13.37)
    'one tree and tree seven'

    >>> aviation_numbers(31.337)
    'tree one and tree tree seven'

    >>> aviation_numbers(-1969)
    'minus one niner six niner'

    >>> aviation_numbers(-31.337)
    'minus tree one and tree tree seven'

    >>> aviation_numbers(-49.35)
    'minus fower niner and tree fife'
    """
    return ' '.join(ALPHABET[char] for char in str(number))


def convert(number):
    """
    >>> convert(1969)
    'one niner six niner'
    >>> TEST = [
    ...     1969,
    ...     31337,
    ...     13.37,
    ...     31.337,
    ...     -1969,
    ...     -31.337,
    ...     -49.35,
    ... ]
    >>> for number in TEST:
    ...     convert(number)
    'one niner six niner'
    'tree one tree tree seven'
    'one tree and tree seven'
    'tree one and tree tree seven'
    'minus one niner six niner'
    'minus tree one and tree tree seven'
    'minus fower niner and tree fife'
    """
    sentence = []

    for character in str(number):
        word = ALPHABET.get(character)
        sentence.append(word)

    return ' '.join(sentence)
