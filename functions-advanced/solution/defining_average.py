def average(*numbers):
    """
    >>> average(1)
    1.0
    >>> average(1, 3)
    2.0
    >>> average()
    """
    if numbers:
        return sum(numbers) / len(numbers)

## Alternative
def average(*numbers):
    """
    >>> average(1)
    1.0
    >>> average(1, 3)
    2.0
    >>> average()
    Traceback (most recent call last):
        ...
    ValueError: Not enough arguments
    """
    if not numbers:
        raise ValueError('Not enough arguments')

    return sum(numbers) / len(numbers)
