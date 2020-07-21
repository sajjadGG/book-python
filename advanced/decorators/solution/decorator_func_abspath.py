from pathlib import Path


def abspath(func):
    def wrapper(file):
        current_directory = Path().cwd()
        file = Path(current_directory, file)
        return func(file)
    return wrapper


@abspath
def display(file):
    print(f'Reading file {file}')


display('iris.csv')
# Reading file /home/python/iris.csv

display('/home/python/iris.csv')
# Reading file /home/python/iris.csv
