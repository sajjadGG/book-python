class Setosa:
    pass

class Versicolor:
    pass

class Virginica:
    pass


def iris_factory(species):
    if species == 'setosa':
        return Setosa
    elif species == 'versicolor':
        return Versicolor
    elif species == 'virginica':
        return Virginica
    else:
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
