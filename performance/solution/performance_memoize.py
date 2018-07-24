CACHE = {}


# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         result = n * factorial(n-1)
#         return result


def factorial(n: int) -> int:
    if n in CACHE:
        return CACHE[n]

    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        CACHE[n] = result
        return result



