class Setosa:
    pass


class Versicolor:
    pass


class Virginica:
    pass


def factory(species):
    cls = {
        'setosa': Setosa,
        'versicolor': Versicolor,
        'virginica': Virginica,
    }.get(species, None)

    if not cls:
        raise NotImplementedError
    else:
        return cls


iris = factory('setosa')
print(iris)
# <class '__main__.Setosa'>
