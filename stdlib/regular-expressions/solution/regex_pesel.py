import re

PESEL_REGEXP = r'^\d{11}$'


def is_valid_PESEL(PESEL):
    if re.match(PESEL_REGEXP, PESEL):
        return True
    else:
        return False


def is_woman(PESEL):
    """
    Check whether PESEL is woman's.

    If the second to last number is even,
    then PESEL is woman's, in other case
    PESEL is man's.
    """

    if int(PESEL[-2]) % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    if is_woman('12345678901'):
        print('Woman')
    else:
        print('Man')
