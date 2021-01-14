from abc import ABCMeta, abstractmethod


class Path(metaclass=ABCMeta):
    def __new__(cls, path, *args, **kwargs):
        if path.startswith(r'C:\Users'):
            instance = object.__new__(WindowsPath)
        if path.startswith('/home'):
            return object.__new__(LinuxPath)
        if path.startswith('/Users'):
            return object.__new__(macOSPath)
        instance.__init__(path)
        return instance

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def dir_create(self):
        pass

    @abstractmethod
    def dir_list(self):
        pass

    @abstractmethod
    def dir_remove(self):
        pass


class WindowsPath(Path):
    def dir_create(self):
        pass

    def dir_list(self):
        pass

    def dir_remove(self):
        pass


class LinuxPath(Path):
    def dir_create(self):
        pass

    def dir_list(self):
        pass

    def dir_remove(self):
        pass


class macOSPath(Path):
    def dir_create(self):
        pass

    def dir_list(self):
        pass

    def dir_remove(self):
        pass


file = Path(r'C:\Users\MWatney\myfile.txt')
print(type(file))
# <class '__main__.WindowsPath'>

file = Path(r'/home/mwatney/myfile.txt')
print(type(file))
# <class '__main__.LinuxPath'>

file = Path(r'/Users/mwatney/myfile.txt')
print(type(file))
# <class '__main__.macOSPath'>
