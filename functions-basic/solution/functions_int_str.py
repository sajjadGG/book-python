from typing import Union

NUMBER_DICT = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '.': 'and',
}


def int_to_str(number: Union[int, float]) -> str:
    """
    >>> int_to_str(1969)
    'one nine six nine'

    >>> int_to_str(31337)
    'three one three three seven'

    >>> int_to_str(13.37)
    'one three and three seven'

    >>> int_to_str(31.337)
    'three one and three three seven'
    """
    output = []

    for digit in str(number):
        output.append(NUMBER_DICT[digit])

    return ' '.join(output)
