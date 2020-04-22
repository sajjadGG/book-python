from os.path import dirname, join


class ToAbsolutePath:
    def __init__(self, function):
        self._function = function

    def __call__(self, filename):
        path = dirname(__file__)

        if path not in filename:
            filename = join(path, filename)

        return self._function(filename)


def to_absolute_path(fn):
    def wrapper(filename):
        path = dirname(__file__)

        if path not in filename:
            filename = join(path, filename)

        return fn(filename)
    return wrapper


@ToAbsolutePath
def print_file(filename: str) -> str:
    print(f'{filename=}\n\n')

    with open(filename) as file:
        return file.read()


if __name__ == '__main__':
    output = print_file('iris.csv')
    print(output)
