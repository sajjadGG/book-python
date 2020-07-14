from os.path import dirname, join


def to_absolute_path(fn):
    def wrapper(filename):
        path = dirname(__file__)

        if path not in filename:
            filename = join(path, filename)

        return fn(filename)
    return wrapper


@to_absolute_path
def print_file(filename: str) -> str:
    print(f'{filename=}\n\n')

    with open(filename) as file:
        return file.read()


if __name__ == '__main__':
    result = print_file('iris.csv')
    print(result)
