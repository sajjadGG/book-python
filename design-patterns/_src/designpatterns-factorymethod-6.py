class Setosa:
    pass


class Versicolor:
    pass


class Virginica:
    pass


def factory(species):
    return {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'virginica': Virginica,
    }.get(species, None)


iris = factory('setosa')
print(iris)
# <class '__main__.Setosa'>
