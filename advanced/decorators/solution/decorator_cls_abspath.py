from pathlib import Path


class Abspath:
    def __init__(self, func):
        self._func = func

    def __call__(self, file):
        current_directory = Path().cwd()
        file = Path(current_directory, file)
        return self._func(file)


@Abspath
def display(file):
    print(f'Reading file {file}')


display('iris.csv')
# Reading file /home/python/iris.csv

display('/home/python/iris.csv')
# Reading file /home/python/iris.csv
