import sys


class Setosa:
    pass


class Versicolor:
    pass


class Virginica:
    pass


def factory(species):
    try:
        CURRENT_MODULE = sys.modules[__name__]
        return getattr(CURRENT_MODULE, species.capitalize())
    except AttributeError:
        raise NotImplementedError


iris = factory('setosa')
print(iris)
# <class '__main__.Setosa'>
