class Setosa:
    pass

class Virginica:
    pass

class Versicolor:
    pass


def iris_factory(species):
    try:
        classname = species.capitalize()
        return globals()[classname]
    except KeyError:
        raise NotImplementedError


if __name__ == '__main__':
    iris = iris_factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

    iris = iris_factory('virginica')
    print(iris)
    # <class '__main__.Virginica'>

    iris = iris_factory('arctica')
    print(iris)
    # Traceback (most recent call last):
    # NotImplementedError
