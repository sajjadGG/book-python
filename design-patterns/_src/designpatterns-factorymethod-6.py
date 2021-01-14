class Setosa:
    pass


class Versicolor:
    pass


class Virginica:
    pass


def factory(species):
    try:
        classname = species.capitalize()
        return globals()[classname]
    except AttributeError:
        raise NotImplementedError


iris = factory('setosa')
print(iris)
# <class '__main__.Setosa'>
