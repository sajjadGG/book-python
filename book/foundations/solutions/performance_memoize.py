MEMOIZE = {}


# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         result = n * factorial(n-1)
#         return result


def factorial(n: int) -> int:
    if n in MEMOIZE:
        return MEMOIZE[n]

    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        MEMOIZE[n] = result
        return result



